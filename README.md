** Câu 1 : Sử dụng Set trong collection để tìm tập giao và tập hợp giữa 2 tập hợp (tự tạo ra 2 tập hợp, mỗi tập hợp 2.000.000 một số Integer ngẫu nhiên, không giống nhau. 2 tập hợp phải có trên 5% số phần tử giao nhau).Hãy tính tổng thời gian thực hiện tìm cả tập giao và tập hợp và tìm cách tối ưu nhất để thời gian tính toán này nhỏ nhất có thể. **

---
Cách làm của đề bài

1. **Tạo hai tập hợp ngẫu nhiên không trùng lặp**:
   - Sử dụng hàm `random.sample` để tạo ra hai tập hợp `set1` và `set2` với mỗi tập chứa 2 triệu số nguyên ngẫu nhiên, không lặp lại trong khoảng từ 1 đến 10 triệu.
   - Cả hai tập hợp này phải đảm bảo có ít nhất 5% phần tử giao nhau, vì vậy bạn cần thêm 100.000 phần tử từ `set1` vào `set2` để đạt yêu cầu này (5% của 2 triệu = 100.000 phần tử).

2. **Tính toán tập giao và tập hợp**:
   - Tập giao (`intersection`): Là tập hợp chứa những phần tử chung có mặt trong cả `set1` và `set2`. Được tính bằng toán tử `&` (phép giao) trong Python.
   - Tập hợp (`union`): Là tập hợp chứa tất cả các phần tử của cả hai tập hợp, không trùng lặp. Được tính bằng toán tử `|` (phép hợp).

3. **Đo thời gian thực hiện**:
   - Đo thời gian từ lúc bắt đầu đến khi hoàn tất việc tính toán tập giao và tập hợp bằng cách sử dụng hàm `time.time()`.

4. **In kết quả**:
   - Sau khi hoàn tất tính toán, chương trình in ra số phần tử trong tập giao và tập hợp, cũng như tổng thời gian tính toán cho cả quá trình.

Kết quả:
- Số phần tử giao nhau: 480750
- Số phần tử hợp: 3599295
- Thời gian tính toán: 0.27490782737731934 giây
![image](https://github.com/user-attachments/assets/2c0ae5e6-96c8-43aa-b5e0-2c48ce5f0e13)




** Câu 2 : Cho một văn bản như trong file “input 2.zip”. Hãy đọc file và đếm số lần xuất hiện của từng từ (Sử dụng stringtokenizer để tách từ, Các từ này được tách với nhau bằng các dấu sau “ .,!=+-”) rồi ghi vào file output.txt. **

---
Để giải quyết bài tập này dựa trên đoạn code đã cung cấp, bạn cần thực hiện các bước như sau:

1. **Giải nén file .zip:**
   - Bạn cần đọc file nén (`input 2.zip`) và giải nén các file bên trong để sử dụng. 
   - Hàm `extract_zip` trong đoạn code dùng thư viện `zipfile` để thực hiện việc giải nén file .zip. 

   ![image](https://github.com/user-attachments/assets/333e37b2-3ffb-4a4d-a361-ec0a892577f3)


2. **Đọc và đếm số lần xuất hiện của từng từ:**
   - Sau khi giải nén, bạn cần đọc nội dung của tất cả các file `.txt` có trong thư mục giải nén và đếm số lần xuất hiện của từng từ. 
   - Hàm `read_and_count_words_in_txt_files` thực hiện điều này. Nó sử dụng `os.walk` để duyệt qua các file và `re.split()` để tách từ dựa trên các dấu phân cách (` .,!=+-`). 
   - `Counter` từ `collections` giúp đếm số lần xuất hiện của từng từ.

   ![image](https://github.com/user-attachments/assets/1c1b7186-a449-4e9a-97a0-df978b361317)


3. **Ghi kết quả vào file `output 2.txt`:**
   - Sau khi đã đếm được số lần xuất hiện của từng từ, bạn cần ghi kết quả vào file `output 2.txt`.
   - Hàm `write_word_counts_to_file` sẽ thực hiện việc này.

   ![image](https://github.com/user-attachments/assets/b03d9633-a781-426e-91ed-dc3ea074f7bd)


4. **Chạy chương trình:**
   - Hàm `main` sẽ gọi các hàm trên để giải nén file zip, đếm từ và ghi kết quả ra file. Đảm bảo rằng đường dẫn tới file zip và các file liên quan là chính xác.

   ![image](https://github.com/user-attachments/assets/27598593-5dd8-465d-8a95-bf7f4675500b)

Kết quả:
File output 2.txt phần code 

** Câu 3 : Lập trình đếm từ đa luồng cho bài 2 với dữ liệu vào là một folder chứa nhiều file text được nén trong file “input 3.zip” bằng cách sử dụng luồng. Hãy xử lý song song các file và tìm top 10 từ xuất hiện nhiều nhất, và top 10 từ xuất hiện ít nhất của toàn bộ dữ liệu có trong folder. Lưu ý, chỉ được chạy tối đa 6 luồng cùng lúc. **

---
1. **Giải nén tệp ZIP**: 
   - Hàm `extract_zip` sử dụng thư viện `zipfile` để giải nén tệp ZIP. Sau khi giải nén, bạn sẽ có một thư mục chứa nhiều tệp `.txt`, từ đó sẽ phân tích từng tệp trong các luồng song song.
   ![image](https://github.com/user-attachments/assets/a711ac1a-5c00-4ed2-8323-213809b6be6b)

2. **Đếm từ trong từng tệp**: 
   - Hàm `count_words_in_file` đọc từng tệp văn bản và đếm số lần xuất hiện của các từ. 
   - Để xử lý tốt các tệp có mã hóa khác nhau, bạn đã xử lý ngoại lệ bằng cách thử mở tệp với mã hóa `utf-8`, và nếu thất bại, thì thử mở với mã hóa `ISO-8859-1`.
   ![image](https://github.com/user-attachments/assets/336d02e3-4c1c-411a-9c1d-950c401c8180)

3. **Sử dụng đa luồng**: 
   - Sử dụng `ThreadPoolExecutor` với `max_workers=6` để đảm bảo chỉ tối đa 6 luồng (threads) hoạt động đồng thời.
   - Hàm `executor.submit(count_words_in_file, file)` sẽ gửi mỗi file vào một luồng để đếm từ trong file đó. 
   - Kết quả từ mỗi luồng được thu thập bằng cách duyệt qua các `future` và cập nhật vào `Counter` chính để lưu tổng số lần xuất hiện từ cho tất cả các file.
   ![image](https://github.com/user-attachments/assets/f7baa4d9-5579-4248-865b-29d790cfcb0a)

4. **Tìm top 10 từ xuất hiện nhiều nhất và ít nhất**: 
   - Sau khi đã có toàn bộ danh sách từ và số lần xuất hiện, hàm `get_top_words` được sử dụng để tìm ra 10 từ xuất hiện nhiều nhất và 10 từ xuất hiện ít nhất.
   ![image](https://github.com/user-attachments/assets/babfe490-e7b6-46b1-8b8c-08194d70041a)

5. **Ghi kết quả ra file**: 
   - Hàm `write_results_to_file` ghi kết quả các từ xuất hiện nhiều nhất và ít nhất vào một file kết quả có tên `output 3.txt`.
   ![image](https://github.com/user-attachments/assets/b0346278-b3ea-42c0-a914-d45ef7453fc8)

Kết quả:
File output 3.txt phần code 

** Câu 4 : Tạo ra một class Point với 2 tọa độ nguyên x và y. Sinh ngẫu nhiên 30.000 point khác nhau, nằm trong 3 Set. Set thứ nhất có size 8.000, chứa các điểm có cách điểm A(800, 800) một độ dài không quá 400 đơn vị, Set tiếp theo có size = 10.000 chứa các điểm cách điểm B(4000,800) không quá 500 đơn vị, và 12.000 điểm cuối cùng cách điểm C(2400, 2400) không quá 600 đơn vị. Trộn ngẫu nhiên 30.000 điểm này, sau đó ghi ra file output4.txt. Lưu ý: sử dụng hàm Set để kiểm tra một điểm đã tồn tại trong tập hợp đó hay chưa (kiểm tra kỹ lại check 2 điểm có tọa độ giống nhau). **

---
### Các bước thực hiện:

1. **Định nghĩa lớp Point**:
   - Tạo lớp `Point` với hai thuộc tính `x` và `y` đại diện cho tọa độ.
   - Thêm phương thức `distance` để tính khoảng cách giữa hai điểm.
   - Cung cấp phương thức `__repr__` để hiển thị điểm dưới dạng chuỗi.
   ![image](https://github.com/user-attachments/assets/1eae915c-3377-40e0-b835-6abbd68442a5)

2. **Hàm tạo điểm ngẫu nhiên**:
   - Tạo hàm `generate_points(center, radius, size)` để sinh ra một tập hợp các điểm.
   - Sử dụng vòng lặp để sinh ra tọa độ `x` và `y` ngẫu nhiên trong phạm vi cho phép (dựa trên tâm và bán kính).
   - Kiểm tra xem điểm đã tồn tại trong tập hợp hay chưa bằng cách sử dụng `set` để đảm bảo các điểm là duy nhất.
   ![image](https://github.com/user-attachments/assets/7200acde-759b-41bc-8a49-63408a1a4782)

3. **Tạo các tập hợp điểm**:
   - Tạo ba tập hợp điểm `set_A`, `set_B`, và `set_C` với các điều kiện khác nhau về vị trí và kích thước:
     - `set_A` chứa 8000 điểm nằm trong khoảng cách 400 đơn vị từ điểm A (800, 800).
     - `set_B` chứa 10000 điểm nằm trong khoảng cách 500 đơn vị từ điểm B (4000, 800).
     - `set_C` chứa 12000 điểm nằm trong khoảng cách 600 đơn vị từ điểm C (2400, 2400).
   ![image](https://github.com/user-attachments/assets/e879768b-645f-412d-ad85-b3e729159025)

4. **Trộn và ghi điểm vào file**:
   - Kết hợp các tập hợp điểm lại thành một danh sách `all_points` và sử dụng `random.shuffle()` để trộn ngẫu nhiên các điểm.
   - Ghi các điểm vào file `output4.txt` theo định dạng mong muốn.
   ![image](https://github.com/user-attachments/assets/77a0579a-3a5e-4a23-9360-6aec922ef94f)


Kết quả:
File output 4.txt phần code 

** Câu 5 : Trong file maze.txt có chứa bản đồ mê cung, hãy implement hàm solve dựa trên một phương pháp tìm đường nào đó để tìm đường đi đến điểm đánh dấu ở giữa bản đồ. Hãy chọn các phương pháp có độ phức tạp (số bước thực hiện) càng nhỏ càng tốt và đánh dấu đường đi bằng cách thay số 0 bằng số 2 trên ma trận mê cung. Lưu ý, bài tập này có xét cách viết code, comment, viết python doc, đặt tên biến/hàm, tổ chức project …**

---
### Các bước thực hiện:

1. **Đọc mê cung từ file**: Sử dụng hàm `read_maze` để đọc dữ liệu từ file `maze.txt` và lưu trữ nó dưới dạng ma trận.
   ![image](https://github.com/user-attachments/assets/f5f61fb4-6b4d-4c1a-8402-b9f8a530b801)
2. **In mê cung ra màn hình**: Sử dụng hàm `print_maze` để kiểm tra cấu trúc mê cung trước khi giải.
   ![image](https://github.com/user-attachments/assets/2b4055ed-3aaa-4088-9b2f-39c3f6121810)
3. **Tìm điểm bắt đầu và điểm kết thúc**:
   - Sử dụng hàm `find_start` để tìm tọa độ của ô bắt đầu (ô có giá trị 0).
   - Sử dụng hàm `find_end` để tìm tọa độ của ô kết thúc (ô có giá trị 2).
   ![image](https://github.com/user-attachments/assets/40ef9c97-caed-41b6-8942-477d1dfc9a08)
4. **Giải quyết mê cung bằng BFS**:
   - Sử dụng thuật toán tìm kiếm theo chiều rộng (BFS) để tìm đường đi từ ô bắt đầu đến ô kết thúc. 
   - Mỗi lần di chuyển hợp lệ, bạn cần ghi nhớ vị trí trước đó để có thể quay lại đường đi.
   - Khi đến ô kết thúc, bạn sẽ quay ngược lại và thay thế các ô 0 trên đường đi bằng ô 2.
   ![image](https://github.com/user-attachments/assets/1127281d-02eb-4bfc-b8f3-68b47b600b42)
5. **Ghi kết quả ra file**: Sau khi tìm đường thành công, sử dụng hàm `write_maze_to_file` để ghi ma trận mê cung đã được đánh dấu vào file `output 5.txt`.
   ![image](https://github.com/user-attachments/assets/89b910fa-f871-400b-853b-c7bfea317962)
Kết quả:
File output 5.txt phần code 

** Câu 6 : Thiết kế hướng đối tượng Tạo các đối tượng (class) cho một hệ thống xuất hóa đơn của một cửa hàng tạp hóa.Hệ thống bao gồm các đối tượng sau: 
Khách hàng (mã khách hàng, giới tính, độ tuổi) 
Nhân viên bán hàng (mã nv, giới tính, ngày làm việc, ca đăng ký) 
Nhân viên nhập hàng (mã nv, giới tính, ngày làm việc, thâm niên) 
Mặt hàng (mã hàng hóa, tên hàng hóa, phân loại, giá) 
Hóa đơn (mã hóa đơn, mã nv bán hàng, mã KH nếu có, danh sách mặt hàng, tổng giá, ngày mua) **
Báo cáo về đoạn code của hệ thống hóa đơn theo hướng đối tượng:

---
1. **Khách hàng (`KhachHang`)**:
- **Thuộc tính:**
  - `customer_id`: Mã khách hàng, giúp định danh duy nhất từng khách hàng.
  - `gender`: Giới tính của khách hàng.
  - `age`: Độ tuổi của khách hàng.
- **Chức năng**: 
  - Mô tả thông tin cơ bản về khách hàng như mã, giới tính và độ tuổi. Lớp này có thể mở rộng để lưu trữ thêm thông tin như địa chỉ hoặc phương thức thanh toán.

2. **Nhân viên bán hàng (`Salesperson`)**:
- **Thuộc tính:**
  - `employee_id`: Mã nhân viên, giúp định danh duy nhất mỗi nhân viên bán hàng.
  - `gender`: Giới tính của nhân viên bán hàng.
  - `work_date`: Ngày làm việc của nhân viên.
  - `shift`: Ca làm việc (sáng, chiều hoặc tối) của nhân viên.
- **Chức năng**: 
  - Lưu thông tin cơ bản về nhân viên bán hàng để liên kết họ với các hóa đơn bán hàng.

3. **Nhân viên nhập hàng (`Stocker`)**:
- **Thuộc tính:**
  - `employee_id`: Mã nhân viên, giúp định danh nhân viên nhập hàng.
  - `gender`: Giới tính của nhân viên nhập hàng.
  - `work_date`: Ngày làm việc của nhân viên nhập hàng.
  - `experience`: Thâm niên làm việc của nhân viên nhập hàng, có thể dùng để xác định mức lương hoặc các lợi ích khác.
- **Chức năng**: 
  - Lưu thông tin về nhân viên nhập hàng, giúp quản lý lịch làm việc và mức độ kinh nghiệm.

4. **Mặt hàng (`Product`)**:
- **Thuộc tính:**
  - `product_id`: Mã sản phẩm, giúp định danh duy nhất mỗi mặt hàng.
  - `product_name`: Tên của mặt hàng.
  - `category`: Phân loại mặt hàng (ví dụ: thực phẩm, đồ uống, gia dụng, v.v.).
  - `price`: Giá của mặt hàng.
- **Chức năng**: 
  - Lớp này cung cấp thông tin chi tiết về từng mặt hàng bán trong cửa hàng tạp hóa. Nó có thể được sử dụng để tính toán tổng giá trị của hóa đơn.

5. **Hóa đơn (`Invoice`)**:
- **Thuộc tính:**
  - `invoice_id`: Mã hóa đơn, định danh duy nhất mỗi hóa đơn.
  - `salesperson_id`: Mã nhân viên bán hàng thực hiện giao dịch.
  - `customer_id`: Mã khách hàng nếu có, có thể để trống nếu khách hàng không đăng ký tài khoản.
  - `product_list`: Danh sách các mặt hàng mà khách hàng đã mua.
  - `total_price`: Tổng số tiền của hóa đơn, tính bằng cách cộng tổng giá các mặt hàng.
  - `purchase_date`: Ngày mua hàng.
- **Chức năng**: 
  - Quản lý toàn bộ thông tin liên quan đến giao dịch, bao gồm nhân viên bán hàng, khách hàng, mặt hàng mua và tổng giá.

![image](https://github.com/user-attachments/assets/b4086ca5-9cf6-48d7-a272-e33e6a79a4a7)


** Câu 7 : Một url là url thỏa mãn các yếu tố (ví dụ 1 url hợp lệ: https://tiki.vn/dien-thoai-may-tinhbang/c1789?src=mega-menu): 
- Bắt đầu bằng http hoặc https 
- Có thể chứa www hoặc không  **
Dưới đây là mẫu báo cáo chi tiết về cách làm bài kiểm tra tính hợp lệ của URL, bao gồm các bước thực hiện:

---

### Mục tiêu
Mục tiêu của chương trình là:
- Xác định xem một URL có hợp lệ hay không dựa trên các tiêu chí đã cho.
- Cung cấp giao diện cho người dùng để nhập URL và nhận phản hồi về tính hợp lệ.

### Tiêu chí kiểm tra URL
URL được coi là hợp lệ nếu thỏa mãn các điều kiện sau:
1. Bắt đầu bằng `http://` hoặc `https://`.
2. Có thể chứa `www.` hoặc không.
3. Địa chỉ miền phải có tên miền là chuỗi ký tự (bao gồm chữ cái và số) và phần mở rộng từ 2 đến 6 ký tự (ví dụ: `.com`, `.vn`, `.net`).
4. Có thể có đường dẫn sau tên miền mà không chứa khoảng trắng.

### Các bước thực hiện
1. **Xây dựng hàm `validate_url`**:
   - Sử dụng biểu thức chính quy (regex) để kiểm tra định dạng của URL.
   - Định nghĩa hàm `validate_url(url)` với tham số là URL cần kiểm tra.

   ![image](https://github.com/user-attachments/assets/f799a382-c4f0-4f86-a2e6-09c8ce1a06dd)

2. **Giao diện người dùng**:
   - Sử dụng vòng lặp `while` để yêu cầu người dùng nhập URL liên tục cho đến khi họ chọn thoát.
   - Kiểm tra điều kiện thoát khi người dùng nhập "done" hoặc để trống và nhấn "Enter".

   ![image](https://github.com/user-attachments/assets/0f8bedf2-c4bf-4f7d-a2b4-9a5dd6edb58e)


3. **Kiểm tra tính hợp lệ**:
   - Sử dụng hàm `validate_url` để xác thực URL nhập vào.
   - Cung cấp phản hồi cho người dùng dựa trên kết quả kiểm tra.

   ![image](https://github.com/user-attachments/assets/cd9a0dbf-48da-45a5-8e30-cf979b1a9c43)


4. **Chạy chương trình**:
   - Lưu mã vào một tệp Python và chạy chương trình.
   - Nhập các URL khác nhau để kiểm tra tính hợp lệ và nhận phản hồi.

Đoạn code:
      ![image](https://github.com/user-attachments/assets/e658e3c7-de96-4597-be79-57c5f472ea76)

Kết Quả:
     ![image](https://github.com/user-attachments/assets/53c4e043-1b05-4b22-9231-bccdc74a303d)




