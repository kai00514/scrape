# vim:fileencoding=utf-8
import requests
import random
import shutil
import bs4
import ssl
import os
ssl._create_default_https_context = ssl._create_unverified_context
output = "out"


def image(data):
    Res = requests.get("https://www.google.com/search?hl=jp&q=" + data + "&btnG=Google+Search&tbs=0&safe=off&tbm=isch")
    Html = Res.text
    Soup = bs4.BeautifulSoup(Html,'lxml')
    links = Soup.find_all("img")
    link = random.choice(links).get("src")
    return link
def download_img(url, file_name):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(file_name+".png", 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)

def code(): # キーワードの各文字をランダムにして帰してるだけ
    code = ""
    for i in range(10):
        code += random.choice("tabacco")
        print("code",code)

    print("code",code)
    return code


    

# ---------- main-process ----------

if __name__ == "__main__":

    while True:
        #num = input("Number of searching")
        num = 100
        #data = input("Word of searching")
        data = "tabacco"
        for _ in range(int(num)):
            link = image(data) # キーワードをimage関数に渡す
            print(link)
            #print(f_name)
            j_path = os.path.join(output,"image{}".format(v))
            v += 1
            
            download_img(link, code())
        print("OK")
