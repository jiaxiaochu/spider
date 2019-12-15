# import openpyxl
# import datetime
# import numpy as np
# import random
#
# zts = int(input())
# zts = zts + 1
# zrs = int(input())
# zrs = zrs + 1
#
# wb = openpyxl.load_workbook("sample.xlsx")
# ws = wb.worksheets[0]
# for col in ws.iter_cols(min_row=2, min_col=2, max_row=zrs, max_col=zts):
#     print(col)
#     for cell in col:
#         if col == 1 or 2:
#             continue
#         else:
#             a = np.random.randint(1, 3)
#             cell.value = a
#
# wb.save("sample.xlsx")

import os

size = os.path.getsize('./sample.xlsx')
if size == 0:
    print("文件是空的")
else:
    print("文件不是空的")


infilename = r'D:\sample.xlsx'
workbook = xlrd.open_workbook(infilename)
df = workbook.sheet_by_name('sheetname')
num_rows = df.nrows - 1  # 我这里是第一行不要，所以跳过了
num_cols = df.ncols
t = 0
im_data = np.zeros((num_rows, num_cols))
for curr_row in range(1, num_rows+1):
    for curr_col in range(num_cols):
        rawVal = df.cell(curr_row, curr_col).value
        # 判断该单元格数值是否为字符串，当然如果你的excel中本来就有字符串格式数据，这里可以更改为判断是否为空字符串，稍微修改一下即可
        if isinstance(rawVal, str):
            im_data[curr_row - 1, curr_col] = np.nan
        else:
            im_data[curr_row - 1, curr_col] = float(rawVal)
