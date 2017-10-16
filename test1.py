import cffi

ffibuilder = cffi.FFI()

# the API exported by the python stuff
ffibuilder.embedding_api("""
    void repl(void);
""")

# declare things that the python code wants to use?
# wrappers are generated
ffibuilder.cdef("""
    extern int value;
    void print_value(void);
""")

# verbatim copied to the output c
# need both this and cdef
ffibuilder.set_source("test1_gen", """
    extern int value;
    void print_value(void);
""")

# init time once only code, called on first api function call
# the cdef and set_source stuff is in lib
ffibuilder.embedding_init_code("""
    from test1_gen import ffi, lib
    import code

    @ffi.def_extern()
    def repl():
        code.InteractiveConsole(locals=globals()).interact()
""")

ffibuilder.compile(verbose=True)


# >>> from cffi import FFI
# >>> ffi = FFI()
# >>> ffi.cdef("""
# ...     int printf(const char *format, ...);   // copy-pasted from the man page
# ... """)
# >>> C = ffi.dlopen(None)                     # loads the entire C namespace
# >>> arg = ffi.new("char[]", "world")         # equivalent to C code: char arg[] = "world";
# >>> C.printf("hi there, %s.\n", arg)         # call printf
# hi there, world.
# 17                                           # this is the return value
# >>>
