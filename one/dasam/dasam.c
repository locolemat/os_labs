/* Death And Suffering to All Mankind - конченный hello world*/

#define SUFFER p++; goto
#include <signal.h>
void assembly(char c)
{
      register char* arg2 asm("rsi") = &c;
      asm("mov $1, %rax; mov $1, %rdi; mov $14, %rdx; syscall;");
}


void sigsegv_handler()
{
    assembly("Поинтер к успеху шёл, но не получилось, не фартануло");
    raise(SIGTERM);
}

main()
{
    char *p;
    signal(SIGSEGV, sigsegv_handler);
    label1: if (*p != 0150)
    {
        SUFFER label1;
    }
    assembly(*p);
    label2: if (*p != 0145)
    {
        SUFFER label2;
    }
    assembly(*p);
    int count1, count2;
    label4: if (count2 - count1 < 2)
    {
        label3: if (*p != 0154)
        {
            SUFFER label3;
        }
        count2++;
        assembly(*p);
        goto label4;
    }

    label5: if (*p != 0157)
    {
        SUFFER label5;
    }
    assembly(*p);
}
