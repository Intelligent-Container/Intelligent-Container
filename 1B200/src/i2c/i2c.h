/*
 * i2c.h
 *
 * created: 2023/5/12
 *  author: 
 */

#ifndef _I2C_H
#define _I2C_H

void I2C1_init(void);
void Get_HDC_ID(void);
void HDC_Get_Temp_Hum(float *temp, float *hum);
void LED8_ON(void);
void LED8_OFF(void);

#endif // _I2C_H

