import numpy as np

# 读取文件数据
file_path = "result/2025-04-20-1.txt"

numeric_columns = []
with open(file_path, "r", encoding="utf-8") as file:
    i = 0
    for line in file:
        if i == 0:
            i += 1
            continue
        parts = line.strip().split("$")[1:]  # 去掉第 0 列（文本列）
        if len(parts) != 5:
            continue
        numeric_values = list(map(float, parts))  # 转换为浮点数
        numeric_columns.append(numeric_values)
        i += 1

# 计算均值
numeric_columns = np.array(numeric_columns)
column_means = np.mean(numeric_columns, axis=0)

# 输出结果
print("每列的均值:", column_means)
