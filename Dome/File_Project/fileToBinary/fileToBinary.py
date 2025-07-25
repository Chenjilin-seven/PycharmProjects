import os
filename = input("请输入文件名: ")
with open(filename, "rb") as f:
    file_data = f.read()
binary_str = '/'.join(str(byte) for byte in file_data)
with open("copy.txt", "w") as f:
    f.write(binary_str)
print("文件已成功转换为编码并写入 copy.txt")
os.system("start copy.txt")
#C:\Users\cjl\Pictures\Screenshots\屏幕截图 2024-11-09 162920(1).png