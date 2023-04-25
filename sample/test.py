import time
start_time = time.time()
n = 100000000
import numpy as np
np_ans = np.sum(np.arange(1,n+1))
end_time = time.time()
print("numの処理時間: ", end_time - start_time)