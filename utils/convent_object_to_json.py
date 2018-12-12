class Test(object):
    def __init__(self):
        self.attribute1 = 1
        self.attribute2 = 2.00
        self.attribute3 = True
        self.attribute4 = "abc"


class TestContext(object):
    def __init__(self,lastname='default',firstname='default'):
        self.lastname = lastname
        self.firstname = firstname


def hBody(j):
    import json
    body = json.dumps(j, default=lambda j: j.__dict__, sort_keys=True,skipkeys= True)
    return body


if __name__ == '__main__':
    print(hBody(Test()))    #  {"attribute1": 1, "attribute2": 2.0, "attribute3": true, "attribute4": "abc"}

    test = Test()
    test.person = hBody(TestContext('Jerry','li'))   # json 内嵌json
    print(hBody(test))    #   {"attribute1": 1, "attribute2": 2.0, "attribute3": true, "attribute4": "abc", "person": "{\"firstname\": \"li\", \"lastname\": \"Jerry\"}"}

    test = Test()
    test.person = [hBody(TestContext('John','Lennon')),hBody(TestContext('Paul','Mccany')),hBody(TestContext('Tom','Shilby'))]   # json 内嵌 json 数组
    print(hBody(test))    #   {"attribute1": 1, "attribute2": 2.0, "attribute3": true, "attribute4": "abc", "person": ["{\"firstname\": \"Lennon\", \"lastname\": \"John\"}", "{\"firstname\": \"Mccany\", \"lastname\": \"Paul\"}", "{\"firstname\": \"Shilby\", \"lastname\": \"Tom\"}"]}