from pathlib import Path
import os
filename = input("请输入文件名:")
stpath = input("请输入起始路径:")
print("loading...")
path = Path(stpath)
with open("Search Results.txt", "w+", encoding="utf-8") as f:
    for item in path.rglob(filename):
        f.write(f"找到文件: {item}\n")
        f.write(f"绝对路径: {item.resolve()}\n")
        print(f"找到文件: {item}")
        print(f"绝对路径: {item.resolve()}")
os.system('"Search Results.txt"')
