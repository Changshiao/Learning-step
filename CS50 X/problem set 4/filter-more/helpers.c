#include "helpers.h"
#include<math.h>

// Convert image to grayscale
void grayscale(int height, int width,RGBTRIPLE image[height][width])
{
    for (int row=0 ;row<height ;row++)
    {
        for(int column=0; column<width; column++)
        {
            int average=round((image[row][column].rgbtBlue+image[row][column].rgbtGreen+image[row][column].rgbtRed)/3.0);
            image[row][column].rgbtBlue=average;
            image[row][column].rgbtGreen=average;
            image[row][column].rgbtRed=average;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
       for (int row=0 ;row<height ;row++)
    {
        for(int column=0; column<width; column++)
        {
            if (column<width/2)
            {
                RGBTRIPLE swap=image[row][column];
                image[row][column]=image[row][width-1-column];
                image[row][width-1-column]=swap;
            }
        }
    }
}


// Blur image
RGBTRIPLE get_average(int row,int column,int height,int width,RGBTRIPLE image[][width])
{
    RGBTRIPLE pixel;
    pixel.rgbtBlue=0;
    pixel.rgbtRed=0;
    pixel.rgbtGreen=0;
    float count=0;
    float rgbtBlue=0,rgbtRed=0,rgbtGreen=0;
    for(int i=-1;i<2;i++)
    {
        for(int j=-1;j<2;j++)
        {
            if (row+i>=0&&column+j>=0&&row+i<height&&column+j<width)
            {
                rgbtBlue+=image[row+i][column+j].rgbtBlue;
                rgbtRed+=image[row+i][column+j].rgbtRed;
                rgbtGreen+=image[row+i][column+j].rgbtGreen;
                count++;
            }
        }

    }
    pixel.rgbtBlue = round(rgbtBlue / count);
    pixel.rgbtRed = round(rgbtRed / count);
    pixel.rgbtGreen = round(rgbtGreen / count);
    return pixel;
}

void blur(int height, int width, RGBTRIPLE image[height][width])
{
    for (int row=0;row<height;row++)
    {
        for (int column=0;column<width;column++)
        {
            image[row][column]=get_average(row,column,height,width,image);
        }
    }
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];

    int gx[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
    int gy[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int gxBlue = 0;
            int gyBlue = 0;
            int gxGreen = 0;
            int gyGreen = 0;
            int gxRed = 0;
            int gyRed = 0;

            for (int r = -1; r < 2; r++)
            {
                for (int c = -1; c < 2; c++)
                {
                    if (i + r < 0 || i + r > height - 1)
                    {
                        continue;
                    }
                    if (j + c < 0 || j + c > width - 1)
                    {
                        continue;
                    }

                    gxBlue += image[i + r][j + c].rgbtBlue * gx[r + 1][c + 1];
                    gyBlue += image[i + r][j + c].rgbtBlue * gy[r + 1][c + 1];
                    gxGreen += image[i + r][j + c].rgbtGreen * gx[r + 1][c + 1];
                    gyGreen += image[i + r][j + c].rgbtGreen * gy[r + 1][c + 1];
                    gxRed += image[i + r][j + c].rgbtRed * gx[r + 1][c + 1];
                    gyRed += image[i + r][j + c].rgbtRed * gy[r + 1][c + 1];
                }
            }

            int blue = round(sqrt(gxBlue * gxBlue + gyBlue * gyBlue));
            int green = round(sqrt(gxGreen * gxGreen + gyGreen * gyGreen));
            int red = round(sqrt(gxRed * gxRed + gyRed * gyRed));

            temp[i][j].rgbtBlue = (blue > 255) ? 255 : blue;
            temp[i][j].rgbtGreen = (green > 255) ? 255 : green;
            temp[i][j].rgbtRed = (red > 255) ? 255 : red;
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtBlue = temp[i][j].rgbtBlue;
            image[i][j].rgbtGreen = temp[i][j].rgbtGreen;
            image[i][j].rgbtRed = temp[i][j].rgbtRed;
        }
    }

    return;
}
