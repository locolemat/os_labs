#include <stdio.h>

#define START 300;
#define FORMATTING "%4d\t%6.1f\n"

main(){
	for (int fahr = START fahr >=0; fahr--)
		printf(FORMATTING, fahr, (5.0/9.0) * (fahr - 32));
}
