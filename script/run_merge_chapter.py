"""
Author channel: https://space.bilibili.com/8172252
"""

import os


class PathFactory:
    cur_dir = os.path.split(os.path.realpath(__file__))[0]

    # 根据目标的相对路径 -> 生成绝对路径
    def get_target_path(target_realpath: str):
        return os.path.abspath(os.path.join(PathFactory.cur_dir, target_realpath))

    # 根据资源的相对路径
    # 先获取资源 dir 再获取该 dir 下的文件
    # 再过滤后排序
    def get_sources_path_list(soruces_realpath: str, filter_key: str):
        # 生成path
        soruces_abspath = os.path.abspath(
            os.path.join(PathFactory.cur_dir, soruces_realpath)
        )
        # 过滤出该 path 下的文件
        file_path_list = [
            name for name in os.listdir(soruces_abspath) if filter_key in name
        ]
        # 重新拼接成绝对路径
        file_path_list = [
            os.path.join(soruces_abspath, name) for name in file_path_list
        ]
        file_path_list.sort()
        return file_path_list


def append_source_to_target(source_path: str, target_path: str):
    file_data = []
    with open(source_path, "r", encoding="utf-8") as file:
        file_data = file.readlines()
    with open(target_path, "a", encoding="utf-8") as file:
        # 过滤掉第一行的 "[toc]"
        # 尾部增加一个空行
        file.writelines(file_data[1:] + ["\n"])

    print(source_path, " ===> success")


if __name__ == "__main__":
    # get sources path list
    file_path_list = PathFactory.get_sources_path_list("../chapter", ".md")
    # get target path
    target_path = PathFactory.get_target_path("../CodeStandard.md")
    # remove old file
    if os.path.exists(target_path):
        os.remove(target_path)

    # content prefix
    with open(target_path, "a", encoding="utf-8") as file:
        file.write("# 代码规范\n")
        file.write("[toc]\n")

    # each chapter by sort
    for source_path in file_path_list:
        append_source_to_target(source_path, target_path)

    # content suffix
    with open(target_path, "a", encoding="utf-8") as file:
        file.write("---\n")
        file.write("---\n")
        file.write("---\n")
        file.write("# END\n")
