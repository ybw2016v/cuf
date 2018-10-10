#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int cucal(float * date,int xar,int yar,int xm,int ym);
int floa6432(float * n32,double * o64,int size)
{
    for (int i = 0; i < size; i++)
    {
        n32[i]=(float)o64[i];
    }
    return 0;
}

float * macf(float* p,int size)
{

    p=(float *)malloc(size*sizeof(float));
    return p;
}

int floatprint(float * p,int xar,int yar,int xm,int ym)
{
    xar=xar/sizeof(float);
    yar=yar/sizeof(float);
    for(int i = 0; i < ym; i++)
    {
        for (int j = 0; j < xm; j++)
        {
            printf("%f ",p[j*xar+i*yar]);
            p[j*xar+i*yar]=(float)sin(i+j);
        }
        printf("\n");
    }
    
    return 0;
}

int cucalpig(float * date,int xar,int yar,int xm,int ym)
{
    cucaldog(date,xar, yar, xm,ym);
    return 0;
}