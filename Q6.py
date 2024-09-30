class KhachHang:
    def __init__(self, makhachhang, gioitinh, tuoi):
        self.customer_id = makhachhang
        self.gender = gioitinh
        self.age = tuoi

class Salesperson:
    def __init__(self, manhanvien, gioitinh, ngaylamviec, cadangky):
        self.employee_id = manhanvien
        self.gender = gioitinh
        self.work_date = ngaylamviec
        self.shift = cadangky

class Stocker:
    def __init__(self, manhanvien, gioiting, ngaylamviec, thamnien):
        self.employee_id = manhanvien
        self.gender = gioiting
        self.work_date = ngaylamviec
        self.experience = thamnien

class Product:
    def __init__(self, masanpham, tensanpham, theloai, giatien):
        self.product_id = masanpham
        self.product_name = tensanpham
        self.category = theloai
        self.price = giatien

class Invoice:
    def __init__(self, mahoadon, manhanvienbanhang, makhachhang, danhsachmathang, tongtien, ngaymua):
        self.invoice_id = mahoadon
        self.salesperson_id = manhanvienbanhang
        self.customer_id = makhachhang
        self.product_list = danhsachmathang
        self.total_price = tongtien
        self.purchase_date = ngaymua