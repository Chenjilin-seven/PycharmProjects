import os
from shutil import move
desktop_path = os.path.expanduser("~/Desktop/start_my_py.bat")
bat_content = "@echo off\nC:/Users/cjl/PyCharmMiscProject/.venv/Scripts/python.exe C:/Users/cjl/PyCharmMiscProject/Dome/File_Project/Start Menu/Start Menu.py"
with open(desktop_path, "w") as f:
    f.write(bat_content)
print("脚本已写入桌面：", desktop_path)
startup_path = os.path.expandvars(r"%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\start_my_py.bat")
try:
    move(desktop_path, startup_path)
    print("已成功移动到启动目录，实现开机自启。")
except PermissionError:
    print("⚠️ 权限不足，无法移动。请手动将桌面上的 start_my_py.bat 文件复制到以下路径：")
    print(startup_path)
# cjlllll