import urllib.request as ur

url = "http://berryservice.net/#/about/account/login"

saveFile = "./data/berrylogin.htm"

data = ur.urlopen(url).read()
with open(saveFile, mode="w") as file:
    file.write(data)

print("OK!")