#include "stdio.h"
#include "pthread.h"
#include <unistd.h>
#include <string.h>
#include <errno.h>

extern void repl(void);

int value = 0;

void print_value(void)
{
    printf("%d\n", value);
}

static void *python_thread(void *vargs)
{
    repl();
}

int main(void)
{
    pthread_t tid;

    if (pthread_create (&tid, NULL, python_thread, NULL) != 0)
        printf ("CREATE_THREAD failed: %s\n", strerror(errno));

    while(1)
    {
        print_value();
        sleep(5);
    }
}
