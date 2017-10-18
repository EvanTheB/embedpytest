#include "stdio.h"
#include "unistd.h"
#include <sys/select.h>
#include <sys/time.h>

extern void py_tick(const char *line);
extern void py_init(void);

int value = 0;

void print_value(void)
{
    printf("%d\n", value);
}

int main(void)
{
    fd_set fds;
    py_init();

    char buffer[1024];
    while(1)
    {
        FD_ZERO(&fds);
        FD_SET(0, &fds);
        struct timeval t = {1,0};
        select(1, &fds, NULL, NULL, &t);

        if (FD_ISSET(0, &fds)){
            int cnt = read(0, buffer, 1023);
            buffer[cnt] = '\0';
            py_tick(buffer);
        }

        print_value();
    }
}
