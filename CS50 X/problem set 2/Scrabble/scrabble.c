#include<stdio.h>
#include<cs50.h>
#include<string.h>
#include<ctype.h>

int get_point(string pl)
{
    int point=0;
    int value[26]={1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10};
    for(int i=0;i<strlen(pl);i++)
    {
        if (isupper(pl[i]))
        {
            point=point+value[pl[i]-'A'];
        }
        if (islower(pl[i]))
        {
            point=point+value[pl[i]-'a'];
        }
        else
        continue;
    }
    return point;
}


int main(void)
{
    string player1=get_string("player1: ");
    string player2=get_string("player2: ");
    int point1,point2;
    point1=get_point(player1);
    point2=get_point(player2);
    if(point1>point2)
    {
        printf("Player 1 wins!\n");
    }
    if(point1<point2)
    {
        printf("Player 2 wins!\n");
    }
    if(point1+=point2)
    {
        printf("Tie!\n");
    }
}
