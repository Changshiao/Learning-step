#include<cs50.h>
#include<stdio.h>

int main(void)
{
    int hight=0;
    do
    {
        hight=get_int("Hight: ");
    }
    while(hight<=0);
    if (hight)
    {
        for(int i=0;i<hight;i++)
        {
            for(int j=1;j<hight-i;j++)
            {
                printf(" ");
            }
            for(int f=0;f<i+1;f++)
            {
                printf("#");
            }
            printf("\n");
        }
    }
    return 0;
}
