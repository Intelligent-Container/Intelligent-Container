import requests
import time
proxies = {"http": None, "https": None}
# 向虚拟机中运行的python web服务发送请求，获取需要下载的文件内容
# response = requests.get('http://192.168.43.3:5000/download', proxies=proxies)
response = requests.get('http://192.168.43.3:5000/download')
#将获取的文件内容保存在本地电脑上
filename = time.strftime("D%Y_%m_%d", time.localtime()) + '.xls'
#path = 'C:/Users/19160830821/Desktop/'+filename
with open(filename, 'wb') as f:
    f.write(response.content)