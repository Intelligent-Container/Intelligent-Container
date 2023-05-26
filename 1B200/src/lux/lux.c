/*
 * lux.c
 *
 * created: 2023/5/12
 *  author:
 */

#include "lux.h"
#include "ls1x_i2c_bus.h"
#include "ls1b_gpio.h"
#include <stdint.h>
#include <math.h>


#define TSL2561FN_ADDRESS 0X29 // 器件地址
#define TSL2561FN_Write 0      // 写命令
#define TSL2561FN_Read 1       // 读命令

#define ID 0x8a        // 器件编号ID寄存器地址
#define CONTROL 0x80   // 控制寄存器地址
#define TIMING 0x81    // 定时寄存器地址
#define DATA0LOW 0x8c  // 通道0低字节地址
#define DATA0HIGH 0x8d // 通道0高字节地址
#define DATA1LOW 0x8e  // 通道1低字节地址
#define DATA1HIGH 0x8f // 通道1高字节地址
#define LED9_IO 51

/************************************************************************
** 功能：  向TSL2561FN写入数据
** 参数：
           @reg_buf:寄存器地址
           @buf:数据缓缓存区
           @len:写数据长度
** 返回值：0,成功;-1,失败.
*************************************************************************/
static char TSL_WR_Data(unsigned char reg_addr, unsigned char *buf, int len)
{
    int ret = 0;

    // 起始信号
    ret = ls1x_i2c_send_start(busI2C1, NULL);
    if (ret < 0)
    {
        printf("send_start error!!!\r\n");
        return -1;
    }

    // 发送从机地址和写命令
    ret = ls1x_i2c_send_addr(busI2C1, TSL2561FN_ADDRESS, TSL2561FN_Write);
    if (ret < 0)
    {
        printf("send_addr error!!!\r\n");
        return -1;
    }

    // 发送寄存器地址
    ret = ls1x_i2c_write_bytes(busI2C1, &reg_addr, 1);
    if (ret < 0)
    {
        printf("write_bytes_reg error!!!\r\n");
        return -1;
    }

    // 发送数据
    ret = ls1x_i2c_write_bytes(busI2C1, buf, len);
    if (ret < 0)
    {
        printf("write_bytes error!!!\r\n");
        return -1;
    }

    // 发送停止信号
    ret = ls1x_i2c_send_stop(busI2C1, NULL);
    if (ret < 0)
    {
        printf("send_stop error!!!\r\n");
        return -1;
    }

    delay_ms(10);
    return ret;
}

/************************************************************************
** 功能：  从TSL2561FN读出数据
** 参数：
           @reg_buf:寄存器的地址
           @buf:数据缓缓存区
           @len:写数据长度
** 返回值：0,成功;-1,失败.
*************************************************************************/
static char TSL_RD_Data(unsigned char reg_addr, unsigned char *buf, int len)
{
    int ret = 0;

    // 起始信号
    ret = ls1x_i2c_send_start(busI2C1, NULL);
    if (ret < 0)
    {
        printf("send_start error!!!\r\n");
        return -1;
    }

    // 发送从机地址和写命令
    ret = ls1x_i2c_send_addr(busI2C1, TSL2561FN_ADDRESS, TSL2561FN_Write);
    if (ret < 0)
    {
        printf("send_addr_W error!!!\r\n");
        return -1;
    }

    // 发送寄存器地址
    ret = ls1x_i2c_write_bytes(busI2C1, &reg_addr, 1);
    if (ret < 0)
    {
        printf("write_bytes_reg error!!!\r\n");
        return -1;
    }

    // 发送停止信号
    ret = ls1x_i2c_send_stop(busI2C1, NULL);
    if (ret < 0)
    {
        printf("send_stop error!!!\r\n");
        return -1;
    }

    // 起始信号
    ret = ls1x_i2c_send_start(busI2C1, NULL);
    if (ret < 0)
    {
        printf("send_start error!!!\r\n");
        return -1;
    }

    // 发送从机地址和读命令
    ret = ls1x_i2c_send_addr(busI2C1, TSL2561FN_ADDRESS, TSL2561FN_Read);
    if (ret < 0)
    {
        printf("send_addr_R error!!!\r\n");
        return -1;
    }

    // 读取数据
    ls1x_i2c_read_bytes(busI2C1, buf, len);
    if (ret < 0)
    {
        printf("read_bytes_Data error!!!\r\n");
        return -1;
    }

    // 发送停止信号
    ret = ls1x_i2c_send_stop(busI2C1, NULL);
    if (ret < 0)
    {
        printf("send_stop error!!!\r\n");
        return -1;
    }

    delay_ms(10);
    return 0;
}

/************************************************************************
 ** 功能：获取TSL2561FN设备的ID
 ** 说明：零件编号ID识别:字段值0000 = TSL2560，字段值0001 = TSL2561
 *************************************************************************/
void TSL_init(void)
{
    unsigned char Device_ID;
    unsigned char TSL_Start = 0x03;    // 设置TSL2561为开启状态
    unsigned char TIM16X_402MS = 0x12; // 积分时间402毫秒,增益16倍

    gpio_enable(LED9_IO, DIR_OUT);
    gpio_write(LED9_IO, 1);

    TSL_WR_Data(CONTROL, &TSL_Start, 1);   // 设置TSL2561开启状态
    TSL_WR_Data(TIMING, &TIM16X_402MS, 1); // 设置积分时间和增益倍数
    TSL_RD_Data(ID, &Device_ID, 1);        // 获取TSL2561的ID
    printf("TSL2561FN的设备ID为：%#x\r\n", Device_ID);
}

/************************************************************************
** 功能：读取光照强度
** 说明：强度大于1000时，LED9亮，反之，LED9灭
*************************************************************************/
float TSL2561FN_RD_Data(void)
{
    unsigned char Data0Low, Data0High, Data1Low, Data1High;
    float Channel0, Channel1;
    float data = 0; // 光强
    float res = 0;
    TSL_RD_Data(DATA0LOW, &Data0Low, 1);
    delay_us(80);
    TSL_RD_Data(DATA0HIGH, &Data0High, 1);
    Channel0 = 256 * Data0High + Data0Low; // 通道0

    TSL_RD_Data(DATA1LOW, &Data1Low, 1);
    delay_us(80);
    TSL_RD_Data(DATA1HIGH, &Data1High, 1);
    Channel1 = 256 * Data1High + Data1Low; // 通道1

    res = Channel1 / Channel0;
    if ((res > 0) && (res <= 0.50))
        data = 0.0304 * Channel0 - 0.062 * Channel0 * pow(res, 1.4);
    else if (res <= 0.61)
        data = 0.0224 * Channel0 - 0.031 * res * Channel0;
    else if (res <= 0.80)
        data = 0.0128 * Channel0 - 0.0153 * res * Channel0;
    else if (res <= 1.30)
        data = 0.00146 * Channel0 - 0.00112 * res * Channel0;
    else
        data = 0;

    return data;
}

void LED9_ON(void)
{
    gpio_write(LED9_IO, 0);
}

void LED9_OFF(void)
{
    gpio_write(LED9_IO, 1);
}
