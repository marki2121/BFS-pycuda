import numpy
import time

from graf_generator import graf_gen
from BFS import BFS

import pycuda.autoinit
import pycuda.driver as drv
from pycuda.compiler import SourceModule

size = int(input("Koliko elemenata ima graf\n>"))

a = numpy.ones((size, size), dtype="int32")
b = numpy.array([], dtype="int32")
c = numpy.array([], dtype="int32")
d = numpy.zeros((size), dtype="int32")

a = graf_gen(a, size)

#CPU dio
time1 = time.time()
c = BFS(a, b, c, d, size)
time2 = time.time()

print("\nCPU:")
print("Odgovor: " + str(c))
print("Vrijeme CPU izvođenja: " + str(time2 - time1) + " sec")

#GPU dio
a_gpu = a
b_gpu = numpy.array([], dtype=numpy.int32)
c_gpu = numpy.array([], dtype=numpy.int32)
d_gpu = numpy.zeros((size), dtype=numpy.int32)
e_gpu = numpy.zeros((size), dtype=numpy.int32)
f_gpu = numpy.zeros((size), dtype=numpy.int32)

mod = SourceModule(open("main.cu").read())
magic = mod.get_function("BFS")

block = size / 1024

if (block > 1):
    if(block % 2 != 0):
        block = int(block) + 1
    size = 1024
else:
    block = 1 

provjera = True
b_gpu = numpy.append(b_gpu, numpy.array([0]))

time1 = time.time()

while provjera:
    while(numpy.size(b_gpu) > 0):
        pov = a_gpu[b_gpu[0]]

        magic(drv.In(pov), drv.InOut(d_gpu), drv.InOut(e_gpu), drv.InOut(f_gpu), block=(int(size), 1, 1), grid=(int(block), 1))
        
        tmp = e_gpu[e_gpu != 0]

        for i in range(numpy.size(tmp)):
            if(f_gpu[tmp[i]] == 0):
                f_gpu[tmp[i]] = 1
                b_gpu = numpy.append(b_gpu, numpy.array([tmp[i]]))

        c_gpu = numpy.append(c_gpu, numpy.array([b_gpu[0]]))
        b_gpu = numpy.delete(b_gpu, 0)
    
    if(numpy.size(b_gpu) < 1):
        provjera = False

time2 = time.time()

print("\nGPU:")
print("Odgovor: " + str(c_gpu))
print("Vrijeme: " + str(time2 - time1) + " sec")

