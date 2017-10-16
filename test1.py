import cffi

ffibuilder = cffi.FFI()

ffibuilder.embedding_api("""
    void repl(void);
""")

ffibuilder.embedding_init_code("""
    from test1_gen import ffi
    import code

    @ffi.def_extern()
    def repl():
        code.InteractiveConsole(locals=globals()).interact()
""")

ffibuilder.set_source("test1_gen", "")

ffibuilder.compile(verbose=True)
