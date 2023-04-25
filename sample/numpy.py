import numpy
import time
start_time = time.time()


total = numpy.sum(numpy.arange(1, 100000001))
end_time = time.time()
print("計算結果:",total,"\nnumpyの処理時間: ", end_time - start_time)
#forループの処理時間:0.5025210380554199秒
