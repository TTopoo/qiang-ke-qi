import re
import requests
import time
import random
import json
import sys
import threading

URLS = ['http://jwgl.dhu.edu.cn/dhu/selectcourse/accessJudge',
       'http://jwgl.dhu.edu.cn/dhu/selectcourse/initACC',
       'http://jwgl.dhu.edu.cn/dhu/selectcourse/scSubmit']

cookies = {
	'array':'jwgl_04',
	'JSESSIONID':'FFC873E36522C5220245CF578D5AD3EE'
}
'''
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'http://jwgl.dhu.edu.cn/dhu/selectcourse/toSH',
    'Origin': 'http://jwgl.dhu.edu.cn',
    'Host': 'jwgl.dhu.edu.cn',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Accept': 'application/json,text/javascript,*/*;q=0.01',
    'Accept-Encoding':'gzip,deflate'
}
'''
courseCode='124344'#039701#039771#039731
cttId='239880'#233633#233537#233559
while True:
    try:
        r = requests.post(url = URLS[0],
                            data = {'courseCode': courseCode},
                            cookies = cookies)
        if not b"true" in r.content:
            print(r.content.decode('utf-8'))
        r = requests.post(url = URLS[1],
                            data = "sEcho=1&iColumns=10&sColumns=&iDisplayStart=0&iDisplayLength=-1&mDataProp_0=cttId&mDataProp_1=classNo&mDataProp_2=maxCnt&mDataProp_3=applyCnt&mDataProp_4=enrollCnt&mDataProp_5=priorMajors&mDataProp_6=techName&mDataProp_7=cttId&mDataProp_8=cttId&mDataProp_9=cttId&iSortCol_0=0&sSortDir_0=asc&iSortingCols=1&bSortable_0=false&bSortable_1=false&bSortable_2=false&bSortable_3=false&bSortable_4=false&bSortable_5=false&bSortable_6=false&bSortable_7=false&bSortable_8=false&bSortable_9=false&\
                                    courseCode=%s" % courseCode,
                            cookies = cookies)
        r = requests.post(url = URLS[2],
                            data = {'cttId': cttId, 'needMaterial': 'false'},
                            cookies = cookies)
        print(r.content.decode('utf-8'))

        if b'success":true' in r.content:
            with open("qiangke_success.txt", "a") as f:
                f.write("{}  {} - {} : Success!!!\n".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), courseCode, cttId))
            print("[I] - !!! {} - {} : Success!!!".format(courseCode, cttId))
            exit(1)
        else:
            time.sleep(10)
    except KeyboardInterrupt:
        print("[W] - Ctrl+C Pressed. Exiting...")
        exit(-2)
    except Exception as e:
        print("[E] - Error Occured while doing qiangke.")
