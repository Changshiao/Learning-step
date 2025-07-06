#include<stdio.h>
#include<cs50.h>
#include<string.h>
#include<ctype.h>

bool check_string(string key)
{
    if(strlen(key)!=26)
    {
        printf("Key must contain 26 characters");
        return false;
    }
    for(int i=0;i<26;i++)
    {
        if(!isalpha(key[i]))
        {
            return false;
        }
        for(int j=i+1;j<26;j++)
        {
            if (key[i]==key[j])
            {
                return false;
            }
        }
    }
    return true;
}

int get_target(char cat)
{
    int target;
    if (isupper(cat))
    {
        target=cat-'A';
    }
    else
    {
        target=cat-'a';
    }
    return target;
}

int main(int argc, string key[])
{
    if (argc!=2)
    {
        printf("Usage: ./caesar key");
        return 1;
    }
    if (check_string(key[1]))
    {
        string plaintext=get_string("plaintext:  ");
        string ciphertext = plaintext;
        for(int i=0;i<strlen(plaintext);i++)
        {
            if (isalpha(plaintext[i]))
            {
                int num=get_target(plaintext[i]);
                if(islower(plaintext[i]))
                {
                    ciphertext[i] = tolower(key[1][num]);
                }
                else
                {
                    ciphertext[i] = toupper(key[1][num]);
                }
            }
        }
        printf("ciphertext: %s\n",ciphertext);
    }
    else
    {
        return 1;
    }
    return 0;
}
