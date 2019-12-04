import requests
import json
import random
import sys
import datetime
import time
from imp import reload
import traceback


reload(sys)
url = 'http://jwgl.dhu.edu.cn/dhu/caslogin.jsp '


data1 = {'courseCode':'150581'}
data2 = {'sEcho':'1','iColumns'='10','sColumns':',','iDisplayStart':'0','iDisplayLength':'-1',
'mDataProp_0':'cttId','mDataProp_1':'classNo','mDataProp_2':'maxCnt','mDataProp_3':'applyCnt','mDataProp_4':'enrollCnt',
'mDataProp_5':'priorMajors','mDataProp_6':'techName','mDataProp_7':'cttId','mDataProp_8':'cttId','mDataProp_9':'cttId',
'iSortCol_0':'0',
'sSortDir_0':'asc','iSortingCols':'1',
'bSortable_0':'false','bSortable_1':'false','bSortable_2':'false','bSortable_3':'false','bSortable_4':'false',
'bSortable_5':'false','bSortable_6':'false','bSortable_7':'false','bSortable_8':'false','bSortable_9':'false',
'courseCode':'150541'
}
data3 = {'cttId':'234854','needMaterial':'false'}

cookies = {
	'array':'jwgl_01',
	'array':'jwgl_01',
	'JSESSIONID':'59250C856AE8AED93FFAC0FEF2961DE4'
}
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

while True:
    try:
    
    try:    
        jscontent3 = requests.session().post('http://jwgl.dhu.edu.cn/dhu/selectcourse/scSubmit',
                                            headers=head,
                                            data=data,
                                            cookies=cookies,
                                            ).text
        jsDict3 = json.loads(jscontent3)
    except Exception as e:
        print(e)
        pass
    print(jsDict3)
    
    time.sleep(5)
