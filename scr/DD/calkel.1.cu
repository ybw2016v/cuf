#include <stdio.h>
#include <stdlib.h>

extern "C"
{
    int cal(float *P1,float *VX,float *VZ,float *Z0,int xar,int yar,int xm,int ym,int n,int n2,float m,int flag);
}


__global__ void cul1(float * p1j,float * vx1j,float * vz1j,float *z0j,int xr, int yr,float m)
{
    // 计算kel1，用于进行梯度运算。
    // printf("%f \n",m);
    int i,j;
    i=threadIdx.x+1;
    j=blockIdx.x+1;
    vx1j[j*yr+i*xr]-=(p1j[j*yr+i*xr]-p1j[j*yr+(i-1)*xr])/z0j[j*yr+i*xr]/m;
    vz1j[j*yr+i*xr]-=(p1j[(j+1)*yr+i*xr]-p1j[j*yr+(i)*xr])/z0j[j*yr+i*xr]/m;
}


__global__ void cul2(float * p1j,float * vx1j,float * vz1j,float *z0j,int xr, int yr,float m) 
{
    // 计算kel2，用于计算压强。
    int i,j;
    i=threadIdx.x+1;
    j=blockIdx.x+1;
    p1j[j*yr+i*xr]-=(vx1j[j*yr+(i+1)*xr]-vx1j[j*yr+i*xr]+vz1j[j*yr+i*xr]-vz1j[(j-1)*yr+i*xr])*z0j[j*yr+i*xr]/m;
}

int cal(float *P1,float *VX,float *VZ,float *Z0,int xar,int yar,int xm,int ym,int n,int n2,float m,int flag)
{
    // printf("%f %f %f\n",m,P1[400],Z0[400]);
    int size;
    float * p1=NULL;
    float * vx=NULL;
    float * vz=NULL;
    float * z0=NULL;
    
    xar=xar/sizeof(float);
    yar=yar/sizeof(float);
    size=(ym*yar)*sizeof(float);
    // printf("%d %d \n",xar,yar);
    // printf("%d %d %d %d\n",xar,yar,xm,ym);
    // printf("%d \n",size);
    // cudaMallocManaged((void**)&p1, size);
    
    cudaMallocManaged((void**)&p1, size);
    cudaMallocManaged((void**)&vx, size);
    cudaMallocManaged((void**)&vz, size);
    cudaMallocManaged((void**)&z0, size);
    cudaDeviceSynchronize();
    // printf("%hd \n",p1);
    memcpy(p1,P1,size);
    
    memcpy(p1,P1,size);
    memcpy(vx,VX,size);
    memcpy(vz,VZ,size);
    memcpy(z0,Z0,size);
    // printf("%s \n", "OK");
    cudaDeviceSynchronize();
    for (int i = n; i < n2; i++)
    {
        p1[200*xar+200*yar]=sin(0.008*i);
        cul1<<<ym-2,xm-2>>>(p1,vx,vz,z0,xar,yar,m);
        cudaDeviceSynchronize();
        cul2<<<ym-2,xm-2>>>(p1,vx,vz,z0,xar,yar,m);
        cudaDeviceSynchronize();
    }
    cudaDeviceSynchronize();
    // for(int i = 0; i<ym; i++)
    // {
        
    //     for(int j = 0; j <xm; j++)
    //     {
    //         printf("%f ",Z0[j*xar+i*yar]);
    //     }
    //     printf("\n");
        
    // }
    memcpy(P1,p1,size);
    memcpy(VX,vx,size);
    memcpy(VZ,vz,size);

    cudaFree(p1);
    cudaFree(vx);
    cudaFree(vz);
    cudaFree(z0);
    
    return 0;
}

