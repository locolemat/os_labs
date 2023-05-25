#include "lib/reverse.h"
#include <stdio.h>

#define MAX_SIZE 1000
int main(){
    char c, d[MAX_SIZE] = "";
    for (int i = 0; (c = getchar()) != EOF; i++)
        d[i] = c;
    reverse(d);
    printf("%s\n",d);

    return 0;
}
