

/*

2D专用
例如
void usercode(float * p1j,float * vx1j,float * vz1j,float *z0j,int xr, int yr,float m)
{

}
3D专用
void usercode(float * p1,float * vx,float * vy,float * vz,float *z0,int xar, int yar,int zar,float m,int i)
｛
     p1[64*xar+64*yar+64*zar]=sin(0.1*i);
｝

*/

void usercode(float * p1,float * vx,float * vy,float * vz,float *z0,int xar,  int yar,int zar,float m,int i)
{
    p1[64*xar+64*yar+64*zar]=sin(0.1*i);
    // return 0;
}


// void usercode(float * p1,float * vx1,float * vz1,float *z0j,int xar, int yar,float m,int i)
// {
//     p1[4*xar+4*yar]=sin(0.1*i);
// }