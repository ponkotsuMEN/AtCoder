import numpy
n = int(input())
a = numpy.array(list(map(int, input().split())))
b = numpy.array(list(map(int, input().split())))

if numpy.dot(a, b) == 0:
    print("Yes")
else:
    print("No")
