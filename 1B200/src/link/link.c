/*
 * link.c
 *
 * created: 2023/5/11
 *  author: 
 */


#include<stdio.h>
#include<string.h>

#include "src\link\link.h"

_Bool sign = 1;

//月份填充


// 为数据添加格式
char form(char *data){
    sign = !sign;
    strcpy(quote1,"\"");
    strcat(quote1,data);
    if (sign == 0)
    {
        strcat(quote1,"\":");
    }
    else
    {
        strcat(quote1,"\",");
    }
    return* quote1;
}

//输出格式化后的字符串到result
char* link(char* t1,char* t2,char* t3){
    int i;
    char data[100],value[100];
    //char index[]= {'head','batt'};
    //初始化数据
    char A[100]="start",B[100]="00:01:1B:FF:FF:FF",C[10]="514",D[20],E[18],F[100]="8",G[8]="666",H[3]="end";
    //index入库
    //报头
    struct index index0;
    strcpy(index0.keyname,"A");
    //MAC地址
    struct index index1;
    strcpy(index1.keyname,"B");
    //电池电量
    struct index index2;
    strcpy(index2.keyname,"C");
    //年月日
    struct index index3;
    strcpy(index3.keyname,"D");
    //时分秒
    struct index index4;
    strcpy(index4.keyname,"E");
    //传感器数据
    struct index index5;
    strcpy(index5.keyname,"F");
    //校验位
    struct index index6;
    strcpy(index6.keyname,"G");
    //停止位
    struct index index7;
    strcpy(index7.keyname,"H");

    strcpy(D,t1);
    strcpy(E,t2);
    strcpy(F,t3);
    for(i = 0;i<=7;i++)
    {
        char temp[256];
        switch (i)
        {
        case 0:
            strcpy(data,index0.keyname);
            strcpy(index0.keyvalue,A);
            form(data);
            strcat(result,quote1);
            strcpy(value,index0.keyvalue);
            form(value);
            strcat(result,quote1);
            break;
        case 1:
            strcpy(data,index1.keyname);
            strcpy(index1.keyvalue,B);
            form(data);
            strcat(result,quote1);
            strcpy(value,index1.keyvalue);
            form(value);
            strcat(result,quote1);
            break;
        case 2:
            strcpy(data,index2.keyname);
            strcpy(index2.keyvalue,C);
            form(data);
            strcat(result,quote1);
            strcpy(value,index2.keyvalue);
            form(value);
            strcat(result,quote1);
            break;
        case 3:
            strcpy(data,index3.keyname);
            strcpy(index3.keyvalue,D);
            sprintf(temp,"\"%s\":%s,",data,index3.keyvalue);
            strcat(result,temp);
            // strcpy(data,index3.keyname);
            // strcpy(index3.keyvalue,D);
            // form(data);
            // strcat(result,quote1);
            // strcpy(value,index3.keyvalue);
            // // form(value);
            // // strcat(result,quote1);
            break;
        case 4:
            strcpy(data,index4.keyname);
            strcpy(index4.keyvalue,E);
            sprintf(temp,"\"%s\":%s,",data,index4.keyvalue);
            strcat(result,temp);
            break;
        case 5:
            strcpy(data,index5.keyname);
            strcpy(index5.keyvalue,F);
            sprintf(temp,"\"%s\":%s,",data,index5.keyvalue);
            strcat(result,temp);
            break;
        case 6:
            strcpy(data,index6.keyname);
            strcpy(index6.keyvalue,G);
            form(data);
            strcat(result,quote1);
            strcpy(value,index6.keyvalue);
            form(value);
            strcat(result,quote1);
            break;
        case 7:
            strcpy(data,index7.keyname);
            strcpy(index7.keyvalue,H);
            form(data);
            strcat(result,quote1);
            strcpy(value,index7.keyvalue);
            form(value);
            strcat(result,quote1);
            //内容封装完毕，首尾插入花括号
            // strncpy(temp,result,strlen(result)-1);
            // strcat(temp,"\0");
            // sprintf(result,"'{%s}'\n",temp);
            strcpy(temp,"'{");
            strncat(temp,result,strlen(result)-1);
            strcat(temp,"}'");
            strcpy(result,temp);
            memset(temp,0,sizeof(temp));
            //printf("%s",result);
            break;
        default:
            break;
        }
    }
    return result;
}
