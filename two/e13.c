#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define LENGTH 100
int main(){
    FILE *fp;
    char line[255];
    char digits[12];
    unsigned long sum = 0;

    fp = fopen("./e13.txt", "r");

    for (int i = 0; i < LENGTH; i++){
        fgets(line, 255, fp);
        strncpy(digits, line, 11);
        sum += atol(digits);
    }

    printf("%ld", sum);

    fclose(fp);
    return 0;
}
