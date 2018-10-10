#include <stdio.h>
#include <stdlib.h>

extern "C"
{
    int cal(float *P1,float *VX,float *VZ,float *Z0,float *LX,float *LZ,int xar,int yar,int xm,int ym,int n,int n2,float m,int flag);
    void usercode(float * p1,float * vx,float * vy,float * vz,float *z0,int xar, int yar,int zar,float m,int i);
}
void usercode(float * p1,float * vx1,float * vz1,float *z0j,int xar, int yar,float m,int i);


__global__ void cul1(float * p1j,float * vx1j,float * vz1j,float *z0j,float *lx,float *ly,int xr, int yr,float m)
{
    // 计算kel1，用于进行梯度运算。
    // printf("%f \n",m);
    int i,j;
    i=threadIdx.x;
    j=blockIdx.x;
    if((i>=1)&&(j<gridDim.x-1))
    {
        vx1j[j*yr+i*xr]-=(p1j[j*yr+i*xr]-p1j[j*yr+(i-1)*xr])/z0j[j*yr+i*xr]/m;
        vz1j[j*yr+i*xr]-=(p1j[(j+1)*yr+i*xr]-p1j[j*yr+i*xr])/z0j[j*yr+i*xr]/m;
    }
    if(j==1)
    {
        if (i>0&&j<blockDim.x-1)
        {
            lx[i]=p1j[(j)*yr+i*xr];
        }
        else 
        {
            lx[i]=0;
        }
        
    }
    if(j==gridDim.x-2)
    {
        lx[blockDim.x+i]=p1j[(j)*yr+i*xr];
    }
    if (i==1)
    {

        ly[j]=p1j[(j)*yr+i*xr];
    }
    if (i==blockDim.x-2)
    {
        ly[gridDim.x+j]=p1j[(j)*yr+i*xr];
    }

}


__global__ void cul2(float * p1j,float * vx1j,float * vz1j,float *z0j,float *lx,float *ly,int xr, int yr,float m) 
{
    // 计算kel2，用于计算压强。
    int i,j;
    i=threadIdx.x;
    j=blockIdx.x;
    if (j==0)
    {
        float dog;
        dog=lx[i]-(vx1j[(j+1)*yr+(i+1)*xr]-vx1j[(j+1)*yr+i*xr]+vz1j[(j+1)*yr+i*xr]-vz1j[(j)*yr+(i)*xr])*z0j[j*yr+i*xr]/m;
        p1j[j*yr+i*xr]=lx[i]+(1.0-m)/(1.0+m)*(dog-p1j[j*yr+i*xr]);    
    }

    if(j==gridDim.x-1)
    {
        float dog;
        dog=lx[blockDim.x+i]-(vx1j[(j-1)*yr+(i+1)*xr]-vx1j[(j-1)*yr+i*xr]+vz1j[(j-1)*yr+i*xr]-vz1j[(j-2)*yr+(i)*xr])*z0j[j*yr+i*xr]/m;
        p1j[j*yr+i*xr]=lx[blockDim.x+i]+(1.0-m)/(1.0+m)*(dog-p1j[j*yr+i*xr]); 
    }
    if (i==0)
    {
        float dog;
        dog=ly[j]-(vx1j[j*yr+(i+2)*xr]-vx1j[j*yr+(i+1)*xr]+vz1j[j*yr+(i+1)*xr]-vz1j[(j-1)*yr+(i+1)*xr])*z0j[j*yr+i*xr]/m;
        p1j[j*yr+i*xr]=ly[j]+(1.0-m)/(1.0+m)*(dog-p1j[j*yr+i*xr]);    

    }
    if (i==blockDim.x-1)
    {
        float dog;
        dog=lx[gridDim.x+j]-(vx1j[j*yr+(i)*xr]-vx1j[j*yr+(i-1)*xr]+vz1j[j*yr+(i-1)*xr]-vz1j[(j-1)*yr+(i-1)*xr])*z0j[j*yr+i*xr]/m;
        p1j[j*yr+i*xr]=lx[blockDim.x+j]+(1.0-m)/(1.0+m)*(dog-p1j[j*yr+i*xr]);
    }
    if((i<blockDim.x-1)&&(i>0)&&(j>0)&&(j<gridDim.x-1))
    {
    p1j[j*yr+i*xr]-=(vx1j[j*yr+(i+1)*xr]-vx1j[j*yr+i*xr]+vz1j[j*yr+i*xr]-vz1j[(j-1)*yr+i*xr])*z0j[j*yr+i*xr]/m;
    }

}

int cal(float *P1,float *VX,float *VZ,float *Z0,float *LX,float *LZ,int xar,int yar,int xm,int ym,int n,int n2,float m,int flag)
{
    // printf("%f %f %f\n",m,P1[400],Z0[400]);
    // printf("%s \n","OK");
    int size;
    float * p1=NULL;
    float * vx=NULL;
    float * vz=NULL;
    float * z0=NULL;
    float * lx=NULL;
    float * lz=NULL;

    
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
    cudaMallocManaged((void**)&lx, 2*xm*sizeof(float));
    cudaMallocManaged((void**)&lz, 2*ym*sizeof(float));
    
    cudaDeviceSynchronize();
    // printf("%hd \n",p1);
    memcpy(p1,P1,size);
    
    memcpy(p1,P1,size);
    memcpy(vx,VX,size);
    memcpy(vz,VZ,size);
    memcpy(z0,Z0,size);
    memcpy(lx,LX,2*xm*sizeof(float));
    memcpy(lz,LZ,2*ym*sizeof(float));
    // printf("%s \n", "OK");
    cudaDeviceSynchronize();
    for (int i = n; i < n2; i++)
    {
        usercode(p1,vx,vz,z0,xar,yar,m,i);
        //p1[200*xar+200*yar]=sin(0.08*i);
        cul1<<<ym,xm>>>(p1,vx,vz,z0,lx,lz,xar,yar,m);
        cudaDeviceSynchronize();
        cul2<<<ym,xm>>>(p1,vx,vz,z0,lx,lz,xar,yar,m);
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
    memcpy(LX,lx,2*xm*sizeof(float));
    memcpy(LZ,lz,2*ym*sizeof(float));
    cudaFree(p1);
    cudaFree(vx);
    cudaFree(vz);
    cudaFree(z0);
    cudaFree(lx);
    cudaFree(lz);
    
    return 0;
}

