import numpy as np

a = np.array([1, 2, 3])  # Tạo array có rank=1
print(type(a))  # Hàm type() trong numpy cho ta biết kiểu của a.
print(a)  # In ra "array([1, 2, 3])"
print(a.shape)  # In ra "(3,)"
# Lệnh này in ra "(3,)", cho ta biết a "cấu hình" của
# a có 1 hàng, 3 cột
print(a[0], a[1], a[2])  # In ra "1 2 3"
# Thay đổi giá trị của phần tử thứ nhất (phần tử có index=0) trong a
a[0] = 5
