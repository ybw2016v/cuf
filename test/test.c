
void usercode(float * p1,float * vx1,float * vz1,float *z0j,int xar, int yar,float m,int i)
{
    int judog=0;
    for (judog = 0; judog < 41; judog++)
    {
        p1[100*xar+(80+judog)*yar]=sin(0.1*i-sin(0.0025*i+1.57)*judog/(4.0));
    }
    // p1[100*xar+80*yar]=sin(0.1*i);
    // p1[100*xar+84*yar]=sin(0.1*i-1);
    // p1[100*xar+88*yar]=sin(0.1*i-2);
    // p1[100*xar+92*yar]=sin(0.1*i-3);
}