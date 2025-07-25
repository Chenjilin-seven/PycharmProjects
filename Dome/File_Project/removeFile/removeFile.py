from pathlib import Path
import os
fileList = []
filename = input("请输入要删除的文件名: ")
stpath = input("请输入搜索起始路径: ")
print("正在搜索，请稍候...")
path = Path(stpath)
for item in path.rglob(filename):
    print(f"找到文件: {item}")
    print(f"绝对路径: {item.resolve()}")
    fileList.append(item.resolve())
bl = input("确认要删除以上文件吗? (Y/N): ").strip().upper()
print(bl)
if bl == "Y":
    for file in fileList:
        try:
            os.remove(file)
            print(f"已删除: {file}")
        except Exception as e:
            print(f"删除失败: {file}，原因: {e}")
else:
    print("操作取消。")
