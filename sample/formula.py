import time
start_time = time.time()
total = int(100000000*(1+100000000)/2)
end_time = time.time()
print("計算結果:",total,"\nアルゴリズムの変更後の処理時間: ", end_time - start_time)
#forループの処理時間:1.1920928955078125e-06秒
