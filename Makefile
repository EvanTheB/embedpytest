main: test1.c test1_gen.c
	gcc -o main test1.c test1_gen.c -I/usr/include/python2.7/ -lpython2.7 -pthread

test1_gen.c: test1.py
	python test1.py
