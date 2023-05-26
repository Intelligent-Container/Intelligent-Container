/*
 * link.h
 *
 * created: 2023/5/11
 *  author: 
 */

#ifndef _LINK_H
#define _LINK_H

#ifdef __cplusplus
extern "C" {
#endif

char t1[100];
char t2[100];
char t3[200];
char quote1[100];
char result[256];

char* link(char* t1,char* t2,char* t3);

//定义键值对结构体
struct index{
    char keyname[16];
    char keyvalue[100];
};

#ifdef __cplusplus
}
#endif

#endif // _LINK_H

