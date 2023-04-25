import time
start_time = time.time()
total = 0
for i in range(1,100000001):
    total += i
end_time = time.time()
print("計算結果:",total,"\nsumの処理時間: ", end_time - start_time)
#forループの処理時間: 8.668177366256714秒

