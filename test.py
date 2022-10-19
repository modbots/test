import urllib.request
#importing the module
file = urllib.request.urlopen("https://cdm1-h7.allnporn.com/vids/277894195.mp4")
#just a dummy file
siz = file.length

def sizeof_fmt(num, suffix="B"):
    for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Yi{suffix}"

r = sizeof_fmt(siz)
print(r)