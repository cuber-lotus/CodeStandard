import os
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from subprocess import run
import sys


def find_suffix_files(root_dir, suffixes):
    file_list = []
    for root, dirs, files in os.walk(root_dir):
        if any(excluded in root for excluded in ["build", "3rdparty"]):
            continue
        file_list.extend(
            os.path.join(root, file) for file in files if file.endswith(tuple(suffixes))
        )
    return file_list


def format_file(file_path):
    try:
        run(["clang-format", "-i", file_path], check=True)
    except Exception as e:
        print(f"Error formatting file: {file_path}, {e}")


def display_progress(current, total, bar_length=40):
    """打印简单的进度条"""
    progress = current / total
    bar_filled = int(bar_length * progress)
    bar = f"[{'#' * bar_filled}{'-' * (bar_length - bar_filled)}]"
    percentage = progress * 100
    sys.stdout.write(f"\r{bar} {current}/{total} ({percentage:.2f}%)")
    sys.stdout.flush()


def main():
    # 获取项目根目录（假设脚本在项目 `script` 文件夹下）
    script_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(script_dir)

    # 需要处理的文件后缀
    suffix_list = [".h", ".hpp", ".cpp", ".cc", ".c"]

    # 查找所有匹配文件
    print("Scanning for files...")
    all_files = find_suffix_files(root_dir, suffix_list)

    # 使用多线程格式化文件
    print("Formatting files...")
    total_files = len(all_files)
    completed_files = 0

    # 进度条初始化
    # display_progress(0, total_files)

    def format_and_update(file_path):
        nonlocal completed_files
        format_file(file_path)
        completed_files += 1
        display_progress(completed_files, total_files)

    # 开始并行格式化文件
    with ThreadPoolExecutor() as executor:
        executor.map(format_and_update, all_files)

    print("\nFormatting completed successfully!")


if __name__ == "__main__":
    print("Script Start:", datetime.now())
    main()
    print("Script End:", datetime.now())
