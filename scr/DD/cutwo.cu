#include <stdio.h>
#include <stdlib.h>
#include <math.h>
struct soc
{
    float *va;
    int xplace;
    int yplace;
};


__device__ float * p0=NULL;
__device__ float * p1=NULL;
__device__ float * vx1=NULL;
__device__ float * vz1=NULL;
__device__ float * z0=NULL;

 float * P1=NULL;
float * VX1=NULL;
float * VZ1=NULL;
__device__ int xin=0;
__device__ int yin=0;
int xma=0;
int yma=0;
__device__ int size=0;
__device__ int m=8;
int SIZE=0;
int XIN=0;
int YIN=0;




extern "C" 
{
    int cucaldog(float * date,int xar,int yar,int xm,int ym);
    int sdogkel(int n);
    int sdoginit(float *pP1, float * pVX1,float * pVZ1,float *Z0,int xar,int yar,int xm,int ym,int n);
    // int soinit(float *f);
}

__global__ void zeroinit(float * date,int xr,int yr);
__global__ void jisuan1(float * p1j,float *vx1j,float* vz1j,float * z0j,int xr,int yr);
__global__ void jisuan2(float * p1j,float *vx1j,float* vz1j,float * z0j,int xr,int yr);
__global__ void jisuan3();
__global__ void sou(int x,int y,int n,float * p1j,float *vx1j,float* vz1j,float * z0j);
__global__ void zeroinit(float * date,int xr,int yr);
__global__ void kkp();
int sdoginit(float *pP1, float * pVX1,float * pVZ1,float *Z0,int xar,int yar,int xm,int ym,int n)
{
    xar=xar/sizeof(float);
    yar=yar/sizeof(float);
    xma=xm;
    
    yma=ym;
    
    XIN=xar;
    YIN=yar;
    // printf("%d %d\n",xin,yar);
    // cudaMemcpy(&xin,&XIN,sizeof(int),cudaMemcpyHostToDevice);
    memcpy(&xin,&XIN,sizeof(int));
    // cudaMemcpy(&yin,&YIN,sizeof(int),cudaMemcpyHostToDevice);
    memcpy(&yin,&YIN,sizeof(int));
    // printf("%d %d\n",xin,yar);
    SIZE=(ym*yar)*sizeof(float);
    memcpy(&size,&SIZE,sizeof(int));
    // printf("**%d\n",cudaMallocManaged((void**)&p1,SIZE));
    cudaMallocManaged((void**)&p1,SIZE);
    cudaMallocManaged((void**)&vx1, SIZE);
    cudaMallocManaged((void**)&vz1, SIZE);
    VX1=pVX1;
    VZ1=pVZ1;
    P1=pP1;
    cudaMallocManaged((void**)&z0,SIZE);
    cudaDeviceSynchronize();
    //     for(int i = 0; i<ym; i++)
    // {
        
    //     for(int j = 0; j <xm; j++)
    //     {
    //         printf("%f ",p1[j*xar+i*yar]);
    //     }
    //     printf("\n");
        
    // }
    memcpy(z0,Z0,SIZE);
    // memcpy(p1,pP1,size);


    // cudaMemcpy(p1,pP1,size,cudaMemcpyHostToDevice);
    zeroinit<<<ym,xm>>>(p1,xin,yin);
    zeroinit<<<ym,xm>>>(vx1,xin,yin);
    zeroinit<<<ym,xm>>>(vz1,xin,yin);
    cudaDeviceSynchronize();
    // memcpy(pP1,p1,SIZE);
    for (int time = 0; time < n; time++)
    {
        // sou<<<1,1>>>(8,4,n,p1,vx1,vz1,z0);

        // cudaDeviceSynchronize();
        p1[200*xar+200*yar]+=sin(0.03*n);
        jisuan1<<<yma-2,xma-2>>>(p1,vx1,vz1,z0,xin,yin);
        cudaDeviceSynchronize();
        jisuan2<<<yma-2,xma-2>>>(p1,vx1,vz1,z0,xin,yin);
        cudaDeviceSynchronize();
        
    }
    // p1[4*xar+4*yar]=1;
    memcpy(pP1,p1,SIZE);
    // cudaDeviceSynchronize();
    return 0;
}
__global__ void zeroinit(float * date,int xr,int yr) 
{
    int i,j;
    i=threadIdx.x;
    j=blockIdx.x;
    // printf("%d-%d :%f\n",i,j, date[j*yr+i*xr]);
    // printf("%d %d;",xr,yr);
    date[j*yr+i*xr]=0;
    // printf("%s \n","OK!dog" );
    
    
}


__global__ void kkp() 
{
    int i,j;
    i=threadIdx.x;
    j=blockIdx.x;
    printf("%d-%d :\n",i,j);
}


int soinit(float **pP0,int num,int tmax,int *xpl,int *ypl)
{
    for (int i = 0; i < num; i++)
    {
        ;
    }
    return 0;
}

int sdogkel(int n)
{
    int sxp,syp;
    sxp=(int)(xma/2);
    syp=(int)(yma/2);

    for (int i = 0; i < n; i++)
    {
        // sou<<<1,1>>>(sxp,syp,n);
        // jisuan1<<<yma-2,xma-2>>>();
        cudaDeviceSynchronize();
        // jisuan2<<<yma-2,xma-2>>>();
        printf("%d \n",i);
    }
    cudaDeviceSynchronize();
    cudaMemcpy(P1,p1,SIZE,cudaMemcpyDeviceToHost);
    printf("%s \n","00" );
    kkp<<<2,2>>>();
    jisuan3<<<yma-2,xma-2>>>();
    cudaDeviceSynchronize();
    printf("%s \n","00" );
    printf("%d \n",SIZE);
        for(int i = 0; i<yma; i++)
    {
        
        for(int j = 0; j <xma; j++)
        {
            printf("%f ",P1[j*XIN+i*YIN]);
        }
        printf("%d\n",i);
        
    }
    // printf("****");
    cudaMemcpy(P1,p1,SIZE,cudaMemcpyDeviceToHost);
    // memcpy(VX1,vx1,SIZE);
    // memcpy(VZ1,vz1,SIZE);
    return 0;
}

__global__ void jisuan1(float * p1j,float *vx1j,float* vz1j,float * z0j,int xr,int yr) 
{
    // printf("%s \n","OKdog!");
    int i,j;
    // printf("%s ","vx1[j*yin+i*xin]");
    i=threadIdx.x+1;
    j=blockIdx.x+1;
    vx1j[j*yr+i*xr]-=(p1j[j*yr+i*xr]-p1j[j*yr+(i-1)*xr])/z0j[j*yr+i*xr]/m;
    vz1j[j*yr+i*xr]-=(p1j[(j+1)*yr+i*xr]-p1j[j*yr+(i)*xr])/z0j[j*yr+i*xr]/m;
    // printf("%s ","vx1[j*yin+i*xin]");
}

__global__ void jisuan2(float * p1j,float *vx1j,float* vz1j,float * z0j,int xr,int yr) 
{
    int i,j;
    i=threadIdx.x+1;
    j=blockIdx.x+1;
    p1j[j*yr+i*xr]-=(vx1j[j*yr+(i+1)*xr]-vx1j[j*yr+i*xr]+vz1j[j*yr+i*xr]-vz1j[(j-1)*yr+i*xr])*z0j[j*yr+i*xr]/m;
    // printf("%f ",p1j[j*yr+i*xr]);
    // if (j==1)
    // {
    //     printf("*%d\n",yr);
    // }
    
    

}

__global__ void sou(int x,int y,int n,float * p1j,float *vx1j,float* vz1j,float * z0j) 
{
    p1j[y*yin+x*xin]+=(float)sin(float(n)/30);
}

__global__ void jisuan3() 
{
    printf("%s \n","OKdog!");
    int i,j;
    i=threadIdx.x+1;
    j=blockIdx.x+1;
    printf("%f ",vx1[j*yin+i*xin]);
}


















__global__ void calkel(float * date,int xr,int yr) 
{
    int i,j;
    i=threadIdx.x;
    j=blockIdx.x;
    // printf("%d-%d :%f\n",i,j, date[j*yr+i*xr]);
    date[j*yr+i*xr]=(float)(i+j)*(i-j);
    
}
int cucaldog(float * date,int xar,int yar,int xm,int ym)
{
    int size;
    float * num=NULL;
    xar=xar/sizeof(float);
    yar=yar/sizeof(float);
    size=(ym*yar)*sizeof(float);
    // printf("%f \n",date[(xm-1)*yar+(ym-1)*xar-1]);
    // for(int i = 0; i < ym; i++)
    // {
    //     for (int j = 0; j < xm; j++)
    //     {
    //         printf("%f@%d ",date[j*xar+i*yar],j*xar+i*yar);
    //         // p[j*xar+i*yar]=(float)sin(i+j);
    //     }
    //     printf("\n");
    // }
    cudaMallocManaged((void**)&num, size);
    // cudaMemcpy(num, date, size, cudaMemcpyHostToDevice);
    // printf("***%d \n",xar*yar);
    memcpy(num, date,size);
    calkel<<<ym,xm>>>(num,xar,yar);
    cudaDeviceSynchronize();
    memcpy(date,num,size);
    cudaFree(num);
    return 0;
}
