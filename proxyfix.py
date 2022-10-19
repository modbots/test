import random
import requests
import json
def proxyfix(a):
    b = a
    url = ["https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/http.txt",
    "https://www.proxyscan.io/download?type=http"
    "http://worm.rip/http.txt",
    "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http",
    "https://openproxylist.xyz/http.txt",
    "https://proxyspace.pro/http.txt",
    "https://proxyspace.pro/https.txt",
    "https://raw.githubusercontent.com/almroot/proxylist/master/list.txt",
    "https://raw.githubusercontent.com/aslisk/proxyhttps/main/https.txt",
    "https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/HTTP.txt",
    "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
    "https://raw.githubusercontent.com/hendrikbgr/Free-Proxy-Repo/master/proxy_list.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt",
    "https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt",
    "https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
    "https://raw.githubusercontent.com/RX4096/proxy-list/main/online/http.txt",
    "https://raw.githubusercontent.com/RX4096/proxy-list/main/online/https.txt",
    "https://raw.githubusercontent.com/saisuiu/uiu/main/free.txt",
    "https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/http.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt",
    "https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
    "https://rootjazz.com/proxies/proxies.txt",
    "https://sheesh.rip/http.txt",
    "https://spys.me/proxy.txt",
    "https://www.freeproxychecker.com/result/http_proxies.txt",
    "https://www.proxy-list.download/api/v1/get?type=http",
    "https://www.proxy-list.download/api/v1/get?type=https",
    "https://www.proxyscan.io/download?type=http"]
    purl =  random.choice(url)
    proxis = requests.get(purl).text
    proxis = proxis.splitlines()
    for proxy in proxis:
        print(f'checking {proxy}...')
        try:
            r = requests.get("https://translate.google.com/",proxies= {'http': proxy,'https': proxy}, timeout=5)
            stat = r.status_code
            if stat == 200:
                #return {'http': proxy,'https': proxy}
                f = open('proxy.json')
                getData = json.load(f)
                with open("proxy.json", "r") as jsonFile:
                    data = json.load(jsonFile)
                    data["proxy"] = str(proxy)
                with open("proxy.json", "w") as jsonFile:
                    json.dump(data, jsonFile)
                jsonFile.close()
                return {'http': proxy,'https': proxy}
                break
            else:
                pass
        except:
            pass
def proxycheck(proxy):
    try:
        r = requests.get("https://translate.google.com/",proxies= {'http': proxy,'https': proxy}, timeout=5)
        stat = r.status_code
        print(stat)
        if stat == 200:
            return {'http': proxy,'https': proxy}
            
    except:
        print('find new one')
        new = proxyfix('g')
        #print(e)
        return new
