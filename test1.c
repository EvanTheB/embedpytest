#include "PyPy.h"
#include <stdio.h>
#include <stdlib.h>

static char source[] = "print 'hello from pypy'";

int main(void)
{
    int res;

    rpython_startup_code();
    /* Before PyPy 5.5, you may need to say e.g. "/opt/pypy/bin" instead
     * of NULL. */
    res = pypy_setup_home(NULL, 1);
    if (res) {
        printf("Error setting pypy home!\n");
        return 1;
    }

    res = pypy_execute_source((char*)source);
    if (res) {
        printf("Error calling pypy_execute_source!\n");
    }
    return res;
}
