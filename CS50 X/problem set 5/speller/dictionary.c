// Implements a dictionary's functionality
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <stdbool.h>
#include "dictionary.h"
#include <string.h>
#include <strings.h>

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;
// TODO: Choose number of buckets in hash table
const unsigned int N = 26;
unsigned int count = 0;
// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    int hashword=hash(word);
    node* cur=table[hashword];
    while (cur!=NULL)
    {
        if(strcasecmp(cur->word,word)!=0)
        {
            cur=cur->next;
        }
        else
        {
            return true;
        }
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    return toupper(word[0]) - 'A';
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    FILE *file = fopen(dictionary, "r");
    char words[LENGTH + 1];

    if (file == NULL)
    {
        return false;
    }

    while (fscanf(file, "%s", words) != EOF)
    {
        node *hashnode = malloc(sizeof(node));
        if (hashnode == NULL)
        {
            fclose(file);
            return false;
        }

        int hashnum = hash(words);
        strcpy(hashnode->word, words);
        hashnode->next = NULL;
        if (table[hashnum] == NULL)
        {
            table[hashnum] = hashnode;
        }
        else
        {
            hashnode->next = table[hashnum];
            table[hashnum] = hashnode;
        }

        count++;
    }

    fclose(file);
    return true;
}


// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return count;
}

// Unloads dictionary from memory, returning true if successful, else false
void free_node(node* hashtable)
{
    if(hashtable->next!=NULL)
    {
        free_node(hashtable->next);
    }
    free(hashtable);
}
bool unload(void)
{
    // TODO
    for(int i=0;i<N;i++)
    {
        if(table[i]!=NULL)
            free_node(table[i]);
    }
    return true;
}
