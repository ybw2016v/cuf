
void usercode(float * p1,float * vx,float * vy,float * vz,float *z0,int xar, int yar,int zar,float m,int i)
{


    static int x1[]=[18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21];
    static int y1[]=[2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6, 6, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 11, 11, 12, 12, 13, 13, 14, 14, 14, 14, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 16, 16, 16, 16, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 16, 16, 16, 16, 16, 16, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 13, 13, 13, 13, 13, 13, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 15, 15, 15, 15, 15, 15];
    static int z1[]=[7, 8, 11, 12, 5, 6, 13, 14, 4, 5, 14, 15, 4, 15, 3, 4, 15, 16, 3, 16, 3, 16, 3, 16, 3, 16, 3, 4, 15, 16, 4, 15, 5, 14, 6, 7, 12, 13, 6, 7, 8, 9, 10, 11, 12, 13, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 3, 4, 5, 6, 7, 12, 13, 14, 15, 16, 2, 3, 4, 5, 6, 13, 14, 15, 16, 17, 2, 3, 4, 5, 14, 15, 16, 17, 2, 3, 4, 5, 14, 15, 16, 17, 1, 2, 3, 4, 15, 16, 17, 18, 2, 3, 4, 15, 16, 17, 18, 2, 3, 4, 5, 14, 15, 16, 17, 2, 3, 4, 5, 14, 15, 16, 17, 2, 3, 4, 5, 6, 13, 14, 15, 16, 17, 3, 4, 5, 6, 7, 8, 11, 12, 13, 14, 15, 16, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 8, 9, 10, 11, 6, 7, 8, 9, 10, 11, 12, 13, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 3, 4, 5, 6, 7, 12, 13, 14, 15, 16, 2, 3, 4, 5, 6, 13, 14, 15, 16, 17, 2, 3, 4, 5, 14, 15, 16, 17, 2, 3, 4, 5, 14, 15, 16, 17, 18, 1, 2, 3, 4, 15, 16, 17, 18, 1, 2, 3, 4, 5, 14, 15, 16, 17, 18, 2, 3, 4, 5, 14, 15, 16, 17, 2, 3, 4, 5, 14, 15, 16, 17, 2, 3, 4, 5, 6, 13, 14, 15, 16, 17, 3, 4, 5, 6, 7, 8, 11, 12, 13, 14, 15, 16, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 7, 8, 9, 10, 11, 12, 8, 9, 10, 11, 6, 7, 8, 9, 10, 11, 12, 13, 14, 4, 5, 6, 7, 12, 13, 14, 15, 3, 4, 5, 6, 14, 15, 16, 3, 4, 5, 14, 15, 16, 2, 3, 4, 15, 16, 17, 2, 3, 4, 15, 16, 17, 2, 3, 4, 15, 16, 17, 2, 3, 4, 15, 16, 17, 2, 3, 4, 15, 16, 17, 3, 4, 5, 15, 16, 3, 4, 5, 14, 15, 16, 4, 5, 6, 13, 14, 15, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 7, 8, 9, 10, 11, 12];
    int longdog=439;
    for (int i = 0; i  < longdog; i ++)
    {
        //p1[x1[i]*xar+y1[i]*yar+z1[i]*zar]=
        //vx[x1[i]*xar+y1[i]*yar+z1[i]*zar]=
        //vy[x1[i]*xar+y1[i]*yar+z1[i]*zar]=
        //vz[x1[i]*xar+y1[i]*yar+z1[i]*zar]=
        //z0[x1[i]*xar+y1[i]*yar+z1[i]*zar]=
    }
    

}
        