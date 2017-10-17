#include "stdio.h"
#include "unistd.h"

extern void py_tick(void);
extern void py_init(void);

int value = 0;

void print_value(void)
{
    printf("%d\n", value);
}

int main(void)
{
    py_init();
    while(1)
    {
        py_tick();
        print_value();
        sleep(5);
    }
}
