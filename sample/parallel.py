import time
start_time = time.time()
from multiprocessing import Process, Value, Lock
def cal(start, end, sum_cal, lock):
    local_sum = 0
    for i in range(start, end+1):
        local_sum += i
    with lock:
        sum_cal.value +=local_sum
if __name__ == '__main__':
    n =  100000000
    sum_cal = Value('l', 0)
    lock = Lock()
    half = int(n/2)
    p1 = Process(target=cal, args=(1, half, sum_cal, lock))
    p2 = Process(target=cal, args=(half+1, n, sum_cal, lock))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    total = sum_cal.value
    end_time = time.time()
    print("計算結果:",total,"\n並列化後の処理時間: ", end_time - start_time)
#並列化後の処理時間:2.640056848526001秒
