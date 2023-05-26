/*
 * press.h
 *
 * created: 2023/5/12
 *  author: 
 */

#ifndef _SPL06_007_H
#define _SPL06_007_H

#include <stdint.h>

uint8_t SPL06_init(void);
void SPL06_Meas_Read_results(float *_Temp, float *_Press, float *_Eleva);
void Get_SPL06_ID(void);
void LED10_ON(void);
void LED10_OFF(void);
void SPL06_Get_Prs(float *_Press, float *_Eleva);
void SPL06_Get_Temp(float *_Temp);

#endif // _SPL06_007_H


