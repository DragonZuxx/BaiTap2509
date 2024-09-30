import random
import time

# Tạo 2 tập hợp với 2 triệu số Integer ngẫu nhiên không trùng lặp
set1 = set(random.sample(range(1, 10000000), 2000000))
set2 = set(random.sample(range(1, 10000000), 2000000))

# Đảm bảo ít nhất 5% phần tử giao nhau
set2.update(random.sample(list(set1), 100000))

# Tính tổng thời gian tìm tập giao và hợp
start_time = time.time()
intersection = set1 & set2  # Tìm tập giao
union = set1 | set2         # Tìm tập hợp
end_time = time.time()

# Đếm số phần tử giao nhau và hợp
num_intersections = len(intersection)
num_union = len(union)


print(f"Số phần tử giao nhau: {num_intersections}")
print(f"Số phần tử hợp: {num_union}")
print(f"Thời gian tính toán: {end_time - start_time} giây")
