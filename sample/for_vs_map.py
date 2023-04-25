import time
import numpy as np
'''
n = 10000
li = [1,2,3]
sum_of_squares = 0

start_time = time.time()
for i in range(1, n+1):
    a = i**li[0]
    b = i**li[1]
    c= i**li[2]
    total = a + b + c
    sum_of_squares += total
end_time = time.time()
print("forループの処理時間: ", end_time - start_time)


start_time = time.time()

def map_sample():
    i**


end_time = time.time()
print("sum関数の処理時間: ", end_time - start_time)
'''
 

'''
start_time = time.time()
for i in range(1,n+1):
    sum_of_squares += i**2
print(sum_of_squares)
end_time = time.time()

print("forループの処理時間: ", end_time - start_time)

start_time = time.time()
print(sum(map(lambda i:i**2, range(1,n+1))))
end_time = time.time()
print("sum関数の処理時間: ", end_time - start_time)
'''







n = 100000000

'''
start_time = time.time()
sum_of_squares = 0
for i in range(1,n+1):
    sum_of_squares += i
end_time = time.time()
print("forループの処理時間: ", end_time - start_time)

start_time = time.time()
sum_of_squares = 0
sum(map(lambda i: sum_of_squares + i, range(1,n+1)))
end_time = time.time()
print("mapの処理時間: ", end_time - start_time)


start_time = time.time()
sum_ans = sum(list(range(1,n+1)))
end_time = time.time()
print("sumの処理時間: ", end_time - start_time)

start_time = time.time()
np_ans = np.sum(np.arange(1,n+1))
end_time = time.time()
print("numの処理時間: ", end_time - start_time)

start_time = time.time()
al_ans = int(n*(1+n)/2)
end_time = time.time()
print("アルゴリズムの最適化処理時間: ", end_time - start_time)
'''
from multiprocessing import Process, Value, Lock
import ctypes
start_time = time.time()
def cal(start, end, sum_cal, lock):
    local_sum = 0
    for i in range(start, end+1):
        local_sum += i
    with lock:
        sum_cal.value += ctypes.c_long(local_sum)

if __name__ == '__main__':
    n =  100000000
    sum_cal = Value('i', 0)
    lock = Lock()

    half = int(n/2)

    p1 = Process(target=cal, args=(1, half, sum_cal, lock))
    p2 = Process(target=cal, args=(half+1, n, sum_cal, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    total_sum = sum_cal.value
    end_time = time.time()

    print(total_sum,end_time - start_time)

    


'''
#print(sum_of_squares)
print(sum_ans)
print(np_ans)
print(al_ans)
'''