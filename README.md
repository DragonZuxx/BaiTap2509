** Câu 1 : Sử dụng Set trong collection để tìm tập giao và tập hợp giữa 2 tập hợp (tự tạo ra 2 tập hợp, mỗi tập hợp 2.000.000 một số Integer ngẫu nhiên, không giống nhau. 2 tập hợp phải có trên 5% số phần tử giao nhau).Hãy tính tổng thời gian thực hiện tìm cả tập giao và tập hợp và tìm cách tối ưu nhất để thời gian tính toán này nhỏ nhất có thể. **


** Câu 2 : Cho một văn bản như trong file “input 2.zip”. Hãy đọc file và đếm số lần xuất hiện của từng từ (Sử dụng stringtokenizer để tách từ, Các từ này được tách với nhau bằng các dấu sau “ .,!=+-”) rồi ghi vào file output.txt. **


** Câu 3 : Lập trình đếm từ đa luồng cho bài 2 với dữ liệu vào là một folder chứa nhiều file text được nén trong file “input 3.zip” bằng cách sử dụng luồng. Hãy xử lý song song các file và tìm top 10 từ xuất hiện nhiều nhất, và top 10 từ xuất hiện ít nhất của toàn bộ dữ liệu có trong folder. Lưu ý, chỉ được chạy tối đa 6 luồng cùng lúc. **


** Câu 4 : Tạo ra một class Point với 2 tọa độ nguyên x và y. Sinh ngẫu nhiên 30.000 point khác nhau, nằm trong 3 Set. Set thứ nhất có size 8.000, chứa các điểm có cách điểm A(800, 800) một độ dài không quá 400 đơn vị, Set tiếp theo có size = 10.000 chứa các điểm cách điểm B(4000,800) không quá 500 đơn vị, và 12.000 điểm cuối cùng cách điểm C(2400, 2400) không quá 600 đơn vị. Trộn ngẫu nhiên 30.000 điểm này, sau đó ghi ra file output4.txt. Lưu ý: sử dụng hàm Set để kiểm tra một điểm đã tồn tại trong tập hợp đó hay chưa (kiểm tra kỹ lại check 2 điểm có tọa độ giống nhau). **


** Câu 5 : Trong file maze.txt có chứa bản đồ mê cung, hãy implement hàm solve dựa trên một phương pháp tìm đường nào đó để tìm đường đi đến điểm đánh dấu ở giữa bản đồ. Hãy chọn các phương pháp có độ phức tạp (số bước thực hiện) càng nhỏ càng tốt và đánh dấu đường đi bằng cách thay số 0 bằng số 2 trên ma trận mê cung. Lưu ý, bài tập này có xét cách viết code, comment, viết python doc, đặt tên biến/hàm, tổ chức project …**


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

   ```python
   import re

   def validate_url(url):
       pattern = r'^(http|https)://(www\.)?([a-zA-Z0-9]+)\.[a-z]{2,6}(/[^\s]*)?$'
       return bool(re.match(pattern, url))
   ```

2. **Giao diện người dùng**:
   - Sử dụng vòng lặp `while` để yêu cầu người dùng nhập URL liên tục cho đến khi họ chọn thoát.
   - Kiểm tra điều kiện thoát khi người dùng nhập "done" hoặc để trống và nhấn "Enter".

   ```
   while True:
       url = input("Nhập URL để kiểm tra (hoặc gõ 'done' hoặc bấm 'Enter' để thoát): ")

       # Kiểm tra điều kiện thoát
       if url.lower() == 'done' or url == '':
           print("Thoát chương trình.")
           break
   ```

3. **Kiểm tra tính hợp lệ**:
   - Sử dụng hàm `validate_url` để xác thực URL nhập vào.
   - Cung cấp phản hồi cho người dùng dựa trên kết quả kiểm tra.

   ```
       if validate_url(url):
           print("URL hợp lệ.")
       else:
           print("URL không hợp lệ. Vui lòng nhập lại.")
   ```

4. **Chạy chương trình**:
   - Lưu mã vào một tệp Python và chạy chương trình.
   - Nhập các URL khác nhau để kiểm tra tính hợp lệ và nhận phản hồi.
Đoạn code:
      ![image](https://github.com/user-attachments/assets/e658e3c7-de96-4597-be79-57c5f472ea76)

Kết Quả:
     ![image](https://github.com/user-attachments/assets/53c4e043-1b05-4b22-9231-bccdc74a303d)




