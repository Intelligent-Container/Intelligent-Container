/*
 * uart.c
 *
 * created: 2023/5/11
 *  author: 
 */



#include "uart.h"
#include "ls1b.h"
#include "ls1b_gpio.h"
#include "ns16550.h"
#include "stdio.h"
#include "string.h"
#include "uart.h"

void UART4_Config_Init(void)
{
    unsigned int BaudRate = 115200;
    ls1x_uart_init(devUART4,(void *)BaudRate); //初始化串口
    ls1x_uart_open(devUART4,NULL); //打开串口
}

void UART4_Test(char* buff){
    //发送数据
    ls1x_uart_write(devUART4,buff,strlen(buff),NULL);
}

void UART5_Config_Init(void)
{
    unsigned int BaudRate = 115200;
    ls1x_uart_init(devUART5,(void *)BaudRate); //初始化串口
    ls1x_uart_open(devUART5,NULL); //打开串口
}

void UART5_Test(char* buff){
    //发送数据
    ls1x_uart_write(devUART5,buff,strlen(buff),NULL);
}