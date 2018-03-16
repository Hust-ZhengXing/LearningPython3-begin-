# A simple timer
import time

start = time.clock()
for i in range(1, 1001):
    for j in range(1, 1001):
        print(i * j)

end = time.clock()

print(end - start)
