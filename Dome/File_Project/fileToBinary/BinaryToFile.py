with open("copy.txt", "r") as f:
    content = f.read().strip()
byte_list = [int(x) for x in content.split('/') if x]
byte_data = bytearray(byte_list)
with open("restored_file.bin", "wb") as f:
    f.write(byte_data)
print("文件已还原")

