all: calkel.so #twod.so cutwo.so
twod.so:twod.c
	gcc twod.c -lm -fopenmp -fPIC -shared -O3 -o twod.so
twod.o:twod.c
	gcc twod.c -lm -fopenmp -fPIC -shared -c -o twod.o
cutwo.so:cutwo.cu
	# nvcc cutwo.cu --compiler-options " -shared -fPIC" -c -o cutwo.o
	nvcc cutwo.cu -shared --compiler-options "-fPIC"  -o cutwo.so
# cutwo.so:cutwo.o twod.o 
# 	gcc cutwo.o twod.o -shared -o cutwo.so
calkel.so:calkel.cu
	nvcc calkel.cu -shared --compiler-options "-fPIC"  -o calkel.so