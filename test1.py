import sys
import cffi

cfile_name = sys.argv[1]

ffibuilder = cffi.FFI()

# the API exported by the python code
ffibuilder.embedding_api("""
    void repl(void);
""")

# declare things that the python code wants to use
# wrappers are generated
# without this init_code lib has nothing
ffibuilder.cdef("""
    extern int value;
    void print_value(void);
""")

# verbatim copied to the output c
# need both this and cdef
# without this the c file wont compile (cdef wrappers refer to undeclared objects)
ffibuilder.set_source("{}".format(cfile_name), """
    extern int value;
    void print_value(void);
""")

# init time once only code, called on first api function call
# the cdef and set_source stuff is in lib
ffibuilder.embedding_init_code("""
    from {} import ffi, lib
    import code

    @ffi.def_extern()
    def repl():
        code.InteractiveConsole(locals=globals()).interact()
""".format(cfile_name))

ffibuilder.compile(verbose=True)
