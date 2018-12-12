import os
# 拼接多个目录：
print(os.path.join(os.getcwd(),'level1','level2','level3'))

# 拼接文件：
print(os.path.join(os.getcwd(),'level1','level2','filename.txt'))