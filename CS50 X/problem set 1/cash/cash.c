#include<stdio.h>
#include<cs50.h>

int main(void)
{
    int owed=0;
    int count=0;
    do
    {
        owed=get_int("Change owed: ");
    }
    while(owed<=0);
    while(owed>=25)
    {
        count+=1;
        owed-=25;
    }
    while(owed>=10)
    {
        count+=1;
        owed-=10;
    }
    while(owed>=5)
    {
        count+=1;
        owed-=5;
    }
    while(owed>=1)
    {
        count+=1;
        owed-=1;
    }
    printf("%d\n",count);
    return 0;
}
