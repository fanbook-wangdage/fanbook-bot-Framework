import subprocess

def test_example_function():
    try:
        # 30秒不退出视为成功
        result = subprocess.run('python3 main.py', timeout=30)
    except subprocess.TimeoutExpired:
        print("成功")

