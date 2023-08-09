import os
import glob

def get_all_file_names(folder_path):
    file_names = []
    # 使用 glob 模块匹配文件夹下的所有文件
    files = glob.glob(os.path.join(folder_path, '*'))
    for file in files:
        if os.path.isfile(file):
            file_names.append("![a](/assets/hunan/" + os.path.basename(file)+")")
    return file_names


names = get_all_file_names(".")
for na in names:
    print(na)