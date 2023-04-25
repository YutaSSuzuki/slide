import time
start_time = time.time()
total = sum(list(range(1,100000001)))
end_time = time.time()
print("計算結果:",total,"\nsumの処理時間: ", end_time - start_time)
#forループの処理時間:4.457662105560303秒
