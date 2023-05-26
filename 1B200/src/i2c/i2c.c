/*
 * i2c.c
 *
 * created: 2023/5/12
 *  author:
 */

#include "i2c.h"
#include "ls1b_gpio.h"
#include "ls1x_i2c_bus.h"
#include <stdint.h>

#define HDC2080_ADDRESS 0x40
#define HDC2080_Write 0
#define HDC2080_Read 1

#define Temp_Hum_addr 0x00 // 温湿度寄存器的起始地址
#define Meas_Conf_addr 0x0f
#define Device_addr 0xfe

#define LED8_IO 52

/************************************************************************
** 功能：  向HDC2080写入数据
** 参数：
          @reg_buf:寄存器地址
          @buf:数据缓缓存区
          @len:写数据长度
** 返回值：0,成功;-1,失败.
*************************************************************************/
static char HDC_WR_Data(unsigned char reg_addr, unsigned char *buf, int len)
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
    ret = ls1x_i2c_send_addr(busI2C1, HDC2080_ADDRESS, HDC2080_Write);
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

    return ret;
}

/************************************************************************
** 功能：  从HDC2080读出数据
** 参数：
           @reg_buf:寄存器的地址
           @buf:数据缓缓存区
           @len:写数据长度
** 返回值：0,成功;-1,失败.
*************************************************************************/
static char HDC_RD_Data(unsigned char reg_addr, unsigned char *buf, int len)
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
    ret = ls1x_i2c_send_addr(busI2C1, HDC2080_ADDRESS, HDC2080_Write);
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
    ret = ls1x_i2c_send_addr(busI2C1, HDC2080_ADDRESS, HDC2080_Read);
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

    return 0;
}

/************************************************************************
** 功能：  初始化I2C1
** 说明：初始化I2C1时要先将GPIO38/39复用为I2C1功能
*************************************************************************/
void I2C1_init(void)
{
    // 将GPIO38/39复用为普通功能
    gpio_disable(38);
    gpio_disable(39);

    // 将GPIO38/39复用为I2C1功能
    LS1B_MUX_CTRL0 |= 1 << 24;

    // 初始化I2C1控制器
    ls1x_i2c_initialize(busI2C1);
}

/************************************************************************
 ** 功能：获取HDC设备的ID
 ** 说明：读出数值为0x07d0则检测到了设备
 *************************************************************************/
void Get_HDC_ID(void)
{
    unsigned char Device_ID[2];

    gpio_enable(LED8_IO, DIR_OUT);
    gpio_write(LED8_IO, 1);

    HDC_RD_Data(Device_addr, Device_ID, 2);
    printf("HDC2080的设备ID为：%#x%x\r\n", Device_ID[1], Device_ID[0]);
}

/************************************************************************
 ** 功能：  获取温湿度值
 ** 说明：
 *************************************************************************/
void HDC_Get_Temp_Hum(float *temp, float *hum)
{
    unsigned char data_buf[4] = {0}; // 第两个字节分别为温度，高两字节为湿度
    unsigned char HDC_Conf = 0x01;   // 开始测量
    uint16_t temp_data, hum_data;

    // 开始测量
    HDC_WR_Data(Meas_Conf_addr, &HDC_Conf, 1);
    delay_us(10);
    // 读取数据
    HDC_RD_Data(Temp_Hum_addr, data_buf, 4);

    temp_data = ((uint16_t)data_buf[1] << 8) | data_buf[0];
    hum_data = ((uint16_t)data_buf[3] << 8) | data_buf[2];

    *temp = temp_data / 65535.0 * 165 - 40;
    *hum = hum_data / 65535.0 * 100;
}

// void LED8_ON(void)
// {
//     gpio_write(LED8_IO, 0);
// }

// void LED8_OFF(void)
// {
//     gpio_write(LED8_IO, 1);
// }
