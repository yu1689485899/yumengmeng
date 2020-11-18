'''
上传文件，一般都是post接口，用files参数上传文件
'''
import requests

url = "http://www.httpbin.org/post"
'''
files参数，字典的格式,'name':file-tuple
file-tuple可以是2-tuple('filename','fileobj')、3-tuple('filename','fileobj','content_tpye')、4-tuple
'''
with open("d:/text.txt", encoding='utf-8') as f:
    file = {"file1": ("text.txt", f, "text/plain")}  # 后边的参数表示文件类型 text/plain ，image/png
    r = requests.post(url, files=file)
    print(r.text)
with open("c:/p.jpg", mode='rb') as f:
    pmg = {"pmg1": ("p.jpg", f, "image/jpg")}
    r = requests.post(url, files=pmg)
    print(r.text)

with open("d:/text.txt", encoding='utf-8-sig') as f:
    with open("c:/p.jpg", mode='rb') as f1:
        pmg = {"pmg1": ("p.jpg", f1, "image/jpg"),
               "file1": ("text.txt", f, "text/plain")}
        r = requests.post(url, files=pmg)
        print(r.text)
