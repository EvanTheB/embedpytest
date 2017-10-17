all: main_pypy main2 main3

main_pypy: test1.c test1_pypy_gen.c
	gcc -o $@ $^ -I./pypy2-v5.9.0-linux64/include -lpypy-c -pthread -L./pypy2-v5.9.0-linux64/bin

main2: test1.c test1_2_gen.c
	gcc -o $@ $^ -I/usr/include/python2.7/ -lpython2.7 -pthread

main3: test1.c test1_3_gen.c
	gcc -o $@ $^ -I/usr/include/python3.5/ -lpython3.5m -pthread

main_bpython: test_bpython.c test_bpython_gen.c
	gcc -o $@ $^ -I/usr/include/python2.7/ -lpython2.7 -pthread

main_thread: test_thread.c test_thread_gen.c
	gcc -o $@ $^ -I/usr/include/python2.7/ -lpython2.7 -pthread

test1_pypy_gen.c: test1.py
	./pypy2-v5.9.0-linux64/bin/pypy test1.py test1_pypy_gen

test1_2_gen.c: test1.py
	python test1.py test1_2_gen

test1_3_gen.c: test1.py
	python3 test1.py test1_3_gen

test_bpython_gen.c: test_bpython.py
	python test_bpython.py test_bpython_gen

test_thread_gen.c: test_thread.py
	python test_thread.py test_thread_gen

.PHONY: clean
clean:
	-rm *_gen.c *_gen.o *_gen.so main*
