
# 读取 txt 文件内容
def read_txt( txt):
    fr = open(txt, 'r')
    content = fr.readlines()
    content1 = []
    for subcontent in content:
        subcontent = subcontent.strip('\n')
        content1.append(subcontent)
    fr.close()
    return content1, len(content1)

# 读取 txt 文件某行内容
def read_line_txt( txt, line):
    import linecache
    linecache.checkcache(txt)
    content = linecache.getline(txt, line).strip('\n')
    return content

# 写入 txt 文件
def write_to_txt( filename,textlist) :
    txtfile=open(filename,'w')
    for text in textlist :
        txtfile.write(text+'\n')
    txtfile.close()

if __name__ == '__main__':
    import os
    # write_to_txt(os.path.join(os.getcwd(),'test.txt'),['col1l,col12,col13','col2l,col22,col23,col24','col3l,col32,col33','col4l,col42,col43','','col6l,col62,col63'])
    # print(read_txt(os.path.join(os.getcwd(),'test.txt')))
    print(read_line_txt(os.path.join(os.getcwd(),'test.txt'),3))