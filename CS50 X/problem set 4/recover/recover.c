#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(int argc, char *argv[])
{
    uint8_t *buffer = malloc(512);
    char file_name[8];
    int image_count=0;
    FILE *card=NULL;
    FILE *new_file=NULL;
    if (argc==2)
    {
        card = fopen(argv[1], "rb");
        if (card==NULL)
        {
            printf("can't open card");
            return 1;
        }
        while(fread(buffer, 1, 512, card)==512)
        {
            if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
            {
                if (new_file != NULL)
                {
                    fclose(new_file);
                }
                sprintf(file_name, "%03i.jpg", image_count);
                new_file = fopen(file_name, "wb");
                image_count++;
            }
            if (new_file != NULL)
            {
                fwrite(buffer, 1, 512, new_file);
            }
        }
    }
    else
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }
    free(buffer);
    if (new_file != NULL)
    {
        fclose(new_file);
    }
    fclose(card);
    printf("contagem = %i\n", image_count);
    return 0;
}
