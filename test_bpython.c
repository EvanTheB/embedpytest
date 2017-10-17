#include "stdio.h"

extern void repl(void);

int value = 0;

void print_value(void)
{
    printf("%d\n", value);
}

int main(void)
{
    print_value();
    repl();
}
