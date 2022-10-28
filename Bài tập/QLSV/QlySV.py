import math
from main.SinhVien import SinhVien
class QuanLySinhVien:
    listSinhVien = []
    #Hàm nhập thông tin sinh viên
    def initsinhvien(self):
        svId = genarateID()
        name = input('Họ và tên: ')
        sex = input('Giới tính: ')
        age = int(input('Tuổi: '))
        diemtoan = int(input('Điểm toán: '))
        diemly = int(input('Điểm lý: '))
        diemhoa = int(input('Điểm hóa: '))
        sv = SinhVien(svId, name, sex, age, diemtoan, diemly, diemhoa)
        self.tinhDTB(sv)
        self.xeploaihocluc(sv)
        self.listSinhVien().appen(sv)
    #Hàm tạo id tăng dần
    def genarateID(self):
        maxId = 1
        if (self.soluongsinhvien() > 0):
            maxId = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if (maxId < sv._id):
                    maxId = sv._id
            maxId = maxId + 1
        return maxId
    def soLuongSinhVien(self):
        return self.listSinhVien.__len__()
    def updateSinhVien(self,ID):
        # Tìm kiếm sinh viên trong danh sách listSinhVien
        sv:SinhVien = self.findByID(ID)
        # Nếu sinh viên tồn tại thì cập nhập thông tin sinh viên
        if (sv != None):
            # nhập thông tin sinh viên
            name = input("Nhap ten sinh vien: ")
            sex = input("Nhap gioi tinh sinh vien: ")
            age = int(input("Nhap tuoi sinh vien: "))
            diemToan = float(input("Nhap diem toan: "))
            diemLy = float(input("Nhap diem Ly: "))
            diemHoa = float(input("Nhap diem Hoa: "))
            # cập nhật thông tin sinh viên
            sv._name = name
            sv._sex = sex
            sv._age = age
            sv._diemToan = diemToan
            sv._diemLy = diemLy
            sv._diemHoa = diemHoa
            self.tinhDTB(sv)
            self.xepLoaiHocLuc(sv)
        else: 
            print("Không có sinh viên có ID = {} trong list", format(ID))
    #Hàm sắp xếp danh sách id sinh viên tăng dần
    def sortByID(self):
        self.listSinhVien.sort(key = lambda x: x._id, reverse = False)
    #Hàm sắp xếp danh sách sinh viên theo tên
    def sortByName(self):
        self.listSinhVien.sort(key = lambda x: x._name, reverse = False)
    #Hàm sắp xếp theo điểm trung bình
    def sortByDTB(self):
        self.listSinhVien.sort(key = lambda x: x._diemTB, reverse=False)
    #Hàm tìm kiếm sinh viên theo id
    #Trả về tên
    def findByID(self,ID):
        searchResult = None
        if (soLuongSinhVien() > 0):
            for sv in self.listSinhVien :
                if (sv._id == ID):
                    searchResult = sv
        return searchResult
    #Hàm tìm kiếm sinh viên theo tên
    #Hàm trả về danh sách sinh viên
    def findByName(self,keyword):
        listSV = []
        if ( soLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                if (keyword.upper() in sv._name.upper()):
                    listSV.append(sv)
        return listSV
    #Hàm xóa sinh viên theo ID
    def deleteByID(self,ID):
        isDelete = False
        sv = self.findByID(ID)
        if (sv != None):
            self.listSinhVien.remove(ID)
            isDelete = True
        return isDelete
    #Hàm tính điểm trung bình cho sv
    def tinhDTB(self,sv:SinhVien):
        diemTB = (sv._diemtoan + sv._diemly + sv._diemhoa)/3
        sv._diemTB = math.ceil(diemTB*100)/100
    #Hàm xếp loại học lực
    def xepLoaiHocLuc(self, sv:SinhVien):
        if (sv._diemTB >= 8):
            sv._hocLuc = "Gioi"
        elif (sv._diemTB >= 6.5):
            sv._hocLuc = "Kha"
        elif (sv._diemTB >= 5):
            sv._hocLuc = "Trung Binh"
        else:
            sv._hocLuc = "Yeu"
    #Hàm hiển thị
    def showSinhVien(self,listSV):
        # hien thi tieu de cot
        print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8} {:<8} {:<8} {:<8}"
              .format("ID", "Name", "Sex", "Age", "Toan", "Ly", "Hoa", "Diem TB", "Hoc Luc"))
        # hien thi danh sach sinh vien
        if (listSV.__len__() > 0):
            for sv in listSV:
                print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8} {:<8} {:<8} {:<8}" 
                      .format(sv._id, sv._name, sv._sex, sv._age, sv._diemToan, sv._diemLy, 
                              sv._diemHoa,sv._diemTB, sv._hocLuc))
        print("\n")

    # Hàm trả về danh sách sinh viên hiện tại
    def getListSinhVien(self):
        return self.listSinhVien


            
