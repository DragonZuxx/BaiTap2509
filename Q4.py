import random
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def __repr__(self):
        return f"({self.x}, {self.y})"

# Hàm tạo điểm ngẫu nhiên gần một điểm cho trước
def generate_points(center, radius, size):
    points = set()
    while len(points) < size:
        x = random.randint(center[0] - radius, center[0] + radius)
        y = random.randint(center[1] - radius, center[1] + radius)
        if Point(x, y).distance(Point(*center)) <= radius:
            points.add((x, y))
    return points

# Tạo các set điểm
set_A = generate_points((800, 800), 400, 8000)
set_B = generate_points((4000, 800), 500, 10000)
set_C = generate_points((2400, 2400), 600, 12000)

# Trộn các điểm và ghi vào file
all_points = list(set_A | set_B | set_C)
random.shuffle(all_points)

try:
    with open('output4.txt', 'w') as f:
        for point in all_points:
            f.write(f"{point}\n")
    print("Ghi vào file thành công!")
except Exception as e:
    print(f"Có lỗi xảy ra khi ghi vào file: {e}")
