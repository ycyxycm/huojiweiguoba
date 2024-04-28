import os
import subprocess


def build_and_upload_package():
    res1=subprocess.run(["python3", "setup.py", "sdist", "bdist_wheel"], cwd=os.path.dirname(os.path.abspath(__file__)))
    print('build',res1)
    res2=subprocess.run(["twine", "upload", "dist/*"], cwd=os.path.dirname(os.path.abspath(__file__)))
    print('upload',res2)


if __name__ == "__main__":
    build_and_upload_package()
