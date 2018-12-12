def md5(value):
    import hashlib
    m = hashlib.md5()
    m.update(str(value).encode('utf-8'))
    value = m.hexdigest()
    return value


def test_md5():
    string_list = 'this is a test'
    string_list_md5 = md5(string_list)
    print(string_list_md5)



if __name__ == '__main__':
    test_md5()