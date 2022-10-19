import requests
import json
def proxyfix(a):
    b = a
    url = "https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/http.txt"#"https://www.proxyscan.io/download?type=http"
    proxis = requests.get(url).text
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
