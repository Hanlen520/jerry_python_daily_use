# 压缩文件
def gzFile(filename):
    import gzip
    destGzFile1 = filename + '.gz'
    sourceGzFile = gzip.open(destGzFile1, 'wb')
    gzip.GzipFile(filename=filename, mode='wb', compresslevel=9, fileobj=sourceGzFile)

if __name__ == '__main__':
    import os
    testFile = os.path.join(os.getcwd(),'test1.txt')
    from utils import read_write_txt
    read_write_txt.write_to_txt(testFile,['this is a test'])
    gzFile(testFile)