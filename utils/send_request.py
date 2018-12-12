from utils.dict_2_str import dict_2_str

def sendbody( url, body):
    import httplib2, json
    http = httplib2.Http(timeout=30)
    response = {}
    content = {}
    headers = {'Content-type': 'application/json;charset=utf8'}
    if len(body):
        list = dict_2_str(body)
        url = url + '?' + list
    try:
        response, content = http.request(url, 'POST')
        content = content.decode('utf-8')
    except httplib2.ServerNotFoundError as e:
        content["code"] = "Error"
        content["message"] = str(e)
    except Exception as e:
        content["code"] = "Error"
        content["message"] = str(e)
    return response, content

def send(url):
    import httplib2,json
    http = httplib2.Http(timeout=30)
    response={}
    content={}
    print(url)
    headers = {'Content-type': 'application/json;charset=utf8'}
    try:
        response, content = http.request(url,'POST')
        content = content.decode('utf-8')
    except httplib2.ServerNotFoundError as e:
        content["code"] = "Error"
        content["message"] = str(e)
    except Exception as e:
        content["code"] = "Error"
        content["message"] = str(e)
    return response,content


if __name__ == '__main__':
    print(send('https://github.com/search/count?q=selenium&type=Users'))
    print(sendbody('https://github.com/search/count',body={"q":"selenium","type":"Users"}))
