/*
 * uart.h
 *
 * created: 2023/5/11
 *  author: 
 */

#ifndef _UART_H
#define _UART_H

#ifdef __cplusplus
extern "C" {
#endif

void UART4_Config_Init(void);
void UART4_Test(char* buff);

void UART5_Config_Init(void);
void UART5_Test(char* buff);

#ifdef __cplusplus
}
#endif

#endif // _UART_H

