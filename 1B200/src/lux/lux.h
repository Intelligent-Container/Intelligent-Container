/*
 * lux.h
 *
 * created: 2023/5/12
 *  author: 
 */

#ifndef _LUX_H
#define _LUX_H

#ifdef __cplusplus
extern "C" {
#endif

void TSL_init(void);
float TSL2561FN_RD_Data(void);
void LED9_ON(void);
void LED9_OFF(void);

#ifdef __cplusplus
}
#endif

#endif // _LUX_H

