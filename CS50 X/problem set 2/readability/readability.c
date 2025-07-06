#include <ctype.h>
#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string text=get_string("Text: ");
    float word=1;
    float sentences=0;
    float letters=0;
    for(int i=0;i<strlen(text);i++)
    {
        if (isalpha(text[i]))
        {
            letters+=1;
        }
        else if (text[i]==' ')
        {
            word+=1;
        }
        else if (text[i]=='.'||text[i]=='?'||text[i]=='!')
        {
            sentences+=1;
        }
    }
    float L=letters/word*100;
    float S=sentences/word*100;
    int index = round(0.0588 * L - 0.296 * S - 15.8);
    if(index<1)
    {
        printf("Before Grade 1\n");
    }
    else if(index>16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n",index);
    }
    return 0;
}
