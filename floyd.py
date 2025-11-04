import numpy as np
from io import StringIO  

np.set_printoptions(
    suppress=True,    #tắt scientific notation
    precision=2,      #làm tròn 2 chữ số thập phân 
    floatmode='maxprec_equal'  # in số không dư .0 nếu không cần 
    )

def Floyd(matrix):
    mat = [row[:] for row in matrix]
    n = len(mat)

    for k in range(n):
        for c in range(n):
            for r in range(n):
                # Nếu self-loop âm → giữ nguyên, không update
                if c == r and mat[c][r] < 0:
                    continue
                if mat[c][k] == float('inf') or mat[k][r] == float('inf'):
                    continue
                mat[c][r] = min(mat[c][r], mat[c][k] + mat[k][r])
    return mat

matran1=[]
matran2=[]

def nhap():
    r=int(input("Nhập số hàng(cột) của ma trận: "))
    if r==0:
        print("Số hàng(cột) không hợp lệ!")
        print("Vui lòng nhập lại!")
        return nhap()
    for i in range(r):
        hang=list(map(float,input(f"Hàng {i+1}: ").split()))
        if len(hang)!=r:
            print("Dữ liệu đã bị sai")
            hang=list(map(float,input(f"Hàng {i+1}: ").split()))
        matran1.append(hang)
    print("Ma trận vừa nhập:")
    print_matrix(matran1)

def read_csv():
    print("Dán dữ liệu CSV vào đây :")
    global matran1  

    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    data = "\n".join(lines)

    try:
        # Load dạng string trước để tự kiểm tra
        raw = np.genfromtxt(StringIO(data), delimiter=',', dtype=str)

        # Kiểm tra dữ liệu có phải số không
        for i, row in enumerate(raw):
            for j, val in enumerate(row):
                try:
                    float(val)
                except ValueError:
                    print(f" Lỗi: Giá trị không phải số tại hàng {i+1}, cột {j+1}: '{val}'")
                    print(" Vui lòng nhập lại dữ liệu hợp lệ!")
                    return  read_csv()

        # Nếu ok thì convert sang float
        matran1 = raw.astype(float)
        print(" Dữ liệu hợp lệ! Ma trận:")
        print_matrix(matran1)

    except Exception as e:
        print("⚠️ Định dạng file CSV không hợp lệ.")
        print("Chi tiết lỗi:", e)

def print_matrix(mat):
    col_width = max(len(f"{val:.2f}") for row in mat for val in row) + 2
    
    print("\n Ma trận khoảng cách tối ưu:")
    for row in mat:
        print("".join(f"{val:<{col_width}.2f}" for val in row))


o=int(input("Bạn muốn nhập tay(1) hay nhập CSV(2)?   "))
if o==1:
    nhap()
elif o==2:
    read_csv()

matran2=Floyd(matran1)

print("Ma trận khoảng cách tối ưu là:")
print_matrix(matran2)
