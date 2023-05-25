#include <stdio.h>

char *reverse(char *s)
{
    char *bp, *ep, c;
    int l;
    bp = s;
    while (*s)
    {
        s++;
    }
    l = s - bp;
    ep = bp + l - 1;

    for (int i = 0; i < (l - 1) / 2; i++)
    {
        c = *ep;
        *ep = *bp;
        *bp = c;
        bp++;
        ep--;
    }

}

int main(){
    char d[12] = "slovo";
    reverse(d);
    printf("%s\n",d);

    return 0;
}
