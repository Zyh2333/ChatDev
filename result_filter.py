import os
import shutil

file_path = "result/2025-05-02-2.txt"

delete_folders = []
output_dir = "WareHouse"
with open(file_path, "r", encoding="utf-8") as file:
    i = 0
    for line in file:
        if i == 0:
            i += 1
            continue
        splits = line.split("$")
        if len(splits) == 6:
            all_folders = []
            all_logs = []
            name = splits[0]
            dirs = os.listdir(output_dir)
            for dir in dirs:
                if name in dir and os.path.isdir(os.path.join(output_dir, dir)):
                    all_folders.append(dir)
                elif name in dir and not os.path.isdir(os.path.join(output_dir, dir)):
                    all_logs.append(dir)
            if len(all_folders) > 1:
                delete_folders = sorted(all_folders)[:-1]
                print(delete_folders)
                # for delete_folder in delete_folders:
                #     if os.path.exists(os.path.join(output_dir, delete_folder)):
                #         shutil.rmtree(os.path.join(output_dir, delete_folder))
            if len(all_logs) > 1:
                delete_logs = sorted(all_logs)[:-1]
                print(delete_logs)
                # for delete_log in delete_logs:
                #     if os.path.exists(os.path.join(output_dir, delete_log)):
                #         os.remove(os.path.join(output_dir, delete_log))
