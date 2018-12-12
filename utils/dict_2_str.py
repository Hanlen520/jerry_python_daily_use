def dict_2_str(dictin):
    tmplist = []
    for k, v in dictin.items():
        if v == '' and k == 'userId':
            pass
        else:
            tmp = "%s=%s" % (str(k), str(v))
            tmplist.append(tmp)
    return '&'.join(tmplist)