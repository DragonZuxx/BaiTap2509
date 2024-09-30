import random
import time

# Tạo 2 tập hợp với 2 triệu số Integer ngẫu nhiên không trùng lặp
set1 = set(random.sample(range(1, 10000000), 2000000))
set2 = set(random.sample(range(1, 10000000), 2000000))

set2.update(random.sample(list(set1), 100000))

#Tính tổng thời gian tìm tập giao và hợp
start_time = time.time()
intersection = set1 & set2
union = set1 | set2
end_time = time.time()

print(f"Thời gian tính toán: {end_time - start_time} giây")

