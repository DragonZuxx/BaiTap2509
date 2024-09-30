from collections import deque

def read_maze(file_path):
    """Đọc mê cung từ file và trả về ma trận."""
    with open(file_path, 'r') as file:
        maze = [list(map(int, line.strip().split())) for line in file]  # Đọc từng dòng và chuyển thành danh sách số nguyên
    return maze

def print_maze(maze):
    """In mê cung ra màn hình."""
    for row in maze:
        print(' '.join(map(str, row)))  # Chuyển từng hàng thành chuỗi và in ra
    print()

def write_maze_to_file(maze, file_path):
    """Ghi mê cung vào file."""
    with open(file_path, 'w') as file:
        for row in maze:
            file.write(' '.join(map(str, row)) + '\n')  # Ghi từng hàng vào file, mỗi hàng trên 1 dòng

def is_valid_move(maze, x, y):
    """Kiểm tra xem có thể di chuyển đến (x, y) không."""
    return (0 <= x < len(maze) and  # Kiểm tra xem x có nằm trong giới hạn của hàng không
            0 <= y < len(maze[0]) and  # Kiểm tra xem y có nằm trong giới hạn của cột không
            maze[x][y] != 1)  # Kiểm tra xem ô (x, y) có phải là vật cản không

def find_start(maze):
    """Tìm vị trí bắt đầu trong mê cung (vị trí đầu tiên có giá trị 0)."""
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 0:  # Tìm vị trí có giá trị 0
                return (i, j)  # Nếu tìm thấy, trả về tọa độ (hàng, cột)
    return None  # Không tìm thấy điểm bắt đầu hợp lệ

def find_end(maze):
    """Tìm vị trí kết thúc trong mê cung (vị trí có giá trị 2)."""
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 2:  # Tìm vị trí có giá trị 2
                return (i, j)  # Nếu tìm thấy, trả về tọa độ (hàng, cột)
    return None  # Không tìm thấy điểm kết thúc

def solve(maze):
    """Tìm đường đi trong mê cung từ điểm bắt đầu tới điểm kết thúc."""
    start = find_start(maze)  # Tìm điểm bắt đầu
    end = find_end(maze)  # Tìm điểm kết thúc

    if start is None or end is None:
        print("Không tìm thấy điểm bắt đầu hoặc điểm kết thúc hợp lệ.")
        return False

    # Các hướng di chuyển: lên, xuống, trái, phải
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Khởi tạo hàng đợi cho BFS
    queue = deque([start])  # Bắt đầu từ điểm bắt đầu
    parent = {start: None}  # Dùng để theo dõi đường đi

    while queue:
        current = queue.popleft()  # Lấy điểm đầu tiên trong hàng đợi

        # Nếu đến điểm kết thúc, quay lại đường đi
        if current == end:
            while current is not None:
                if maze[current[0]][current[1]] == 0:
                    maze[current[0]][current[1]] = 2  # Đánh dấu đường đi (đặt là 3)
                current = parent[current]
            return True  # Tìm thấy đường đi

        for direction in directions:
            next_x, next_y = current[0] + direction[0], current[1] + direction[1]
            next_position = (next_x, next_y)

            # Kiểm tra xem có thể di chuyển đến vị trí tiếp theo không
            if is_valid_move(maze, next_x, next_y) and next_position not in parent:
                parent[next_position] = current  # Ghi nhớ điểm trước đó
                queue.append(next_position)  # Thêm vị trí vào hàng đợi

    print("Không tìm thấy đường đi.")
    return False  # Không tìm thấy đường đi

if __name__ == "__main__":
    maze = read_maze('maze.txt')  # Đọc mê cung từ file
    print("Mê cung ban đầu:")
    print_maze(maze)  # In mê cung ban đầu

    if solve(maze):  # Gọi hàm solve để tìm đường đi
        print("Mê cung sau khi tìm đường đi:")
        write_maze_to_file(maze, 'output 5.txt')  # Ghi mê cung sau khi tìm đường vào file
        print("Đã ghi kết quả vào file output 5.txt.")
    else:
        print("Không tìm thấy đường đi.")  # Thông báo nếu không tìm thấy đường đi
