from urllib import request #Error
url = "https://google.com"
html = request.urlopen(url).read()         #https: s = secure, client가 보내는 id/pw가 암호화돼서 server에 전달 (중간에 가로채도 알아보지 못하도록)

import ssl        # socket secure layer
ctx = ssl.create_default_context() #ctx = context
ctx.check_hostname = False #server가 유효한지 아닌지 =Flase 확인 안 하겠다.
ctx.verify_mode = ssl.CERT_NONE
html = urllib.request.urlopen(url, context=ctx).read()
