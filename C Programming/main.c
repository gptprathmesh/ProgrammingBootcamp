#include <stdio.h>

void bl(int a)
{
    if (a == 0)
        printf("False\n");
    else
        printf("True\n");
}

int main()
{
    bl(2 + 3 == 8);
    return 0;
}