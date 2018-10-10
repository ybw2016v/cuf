#include <iostream>
using namespace std;
int main(int argc, char const *argv[])
{

    int i,count;      
    cudaDeviceProp prop;  
    cudaError_t cudaStatus=cudaGetDeviceCount(&count);  
    if(cudaStatus == cudaSuccess) 
    {  
        cout<<"共有设备数目："<<count<<"\n";  
        if(count>0)  
        {  
            for(i=0;i<=count;i++)
            {  
                cudaGetDeviceProperties(&prop,i);//获取设备的属性信息  
                cout<<"\n第"<<i+1<<"个设备信息：\n";  
                cout<<"设备名称："<<prop.name<<"\n";  
                cout<<"总内存："<<prop.totalGlobalMem/1048576<<"M\n";  
                cout<<"常量内存："<<prop.totalConstMem<<"字节\n";  
                cout<<"设备中处理器数目："<<prop.multiProcessorCount<<"个\n";  
                cout<<"每个线程块最多包含线程数目："<<prop.maxThreadsPerBlock<<"个\n";     
                cout<<"一个线程格中可包含的线程块数目：I="<< prop.maxGridSize[0]  
                    <<" J="<<prop.maxGridSize[1]<<" K="<<prop.maxGridSize[2]<<"\n";  
                cout<<"多维线程块中可以包含的最大线程数目：I="<< prop.maxThreadsDim[0]  
                    <<" J="<<prop.maxThreadsDim[1]<<" K="<<prop.maxThreadsDim[2]<<"\n";  
            }          
        }  
    else  
    {  
        cout<<"没有获取到设备信息！请检查计算机是否具有支持CUDA的显卡设备以及CUDA驱动程序版本是否需要更新！\n";  
    }     
}return 0;
}
