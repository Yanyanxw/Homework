import requests
from pyquery import PyQuery as pq

url = 'http://www.baidu.com/s'

def getName(*name):
    if not name:
        name = input("What's your name:")
    payload = {'ie':'utf-8','wd':name}
    r = requests.get(url,params=payload)
    return pq(r.text)
def printResult():
    doc = getName("谢婉嫣")
    rlist = doc("h3.t").items()
    n = 0;
    for i in rlist:
        n = n + 1
        index = "%02d" % n
        print("No."+ " >>>>>>>>>\r\n\r\n" + "Head:" + i("a").text() + "\n" + "Link:" + i("a").attr("href") + "\r\n")

if __name__ == '__main__':
 printResult()
