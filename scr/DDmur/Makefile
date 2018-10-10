all:culib.so
culib.so:calkel.cu
	nvcc calkel.cu -shared --compiler-options "-g -fPIC"  -o calkel.so