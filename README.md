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

### Kết quả
Chương trình hoạt động hiệu quả, cung cấp phản hồi ngay lập tức về tính hợp lệ của các URL được nhập. Qua đó, người dùng có thể dễ dàng kiểm tra các URL theo tiêu chí đã định.


