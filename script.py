import os
import subprocess
import time


def build_and_upload_package_mac():
    res1 = subprocess.run(["python3", "setup.py", "sdist", "bdist_wheel"],cwd=os.path.dirname(os.path.abspath(__file__)))
    print('build', res1)
    res2 = subprocess.run(["twine", "upload", "dist/*"], cwd=os.path.dirname(os.path.abspath(__file__)))
    print('upload', res2)
def build_and_upload_package_win():
    # 获取当前脚本所在的目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    print("当前脚本所在的目录：", script_dir)
    # time.sleep(111)
    # 构建 Python 包
    build_command = ["python", "setup.py", "sdist", "bdist_wheel"]
    build_result = subprocess.run(build_command, cwd=script_dir)

    if build_result.returncode == 0:
        print("包构建成功！")
    else:
        print(f"包构建失败，返回码: {build_result.returncode}")
        return

    # 上传 Python 包到 PyPI
    upload_command = ["twine", "upload", "dist/*"]
    upload_result = subprocess.run(upload_command, cwd=script_dir)

    if upload_result.returncode == 0:
        print("包上传成功！")
    else:
        print(f"包上传失败，返回码: {upload_result.returncode}")

if __name__ == "__main__":
    # build_and_upload_package_mac()
    build_and_upload_package_win()