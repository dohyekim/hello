import urllib.request as ur
import timeit
start = timeit.default_timer()
url = "http://api.aoikujira.com/ip/ini"

res = ur.urlopen(url)
data = res.read()

text = data.decode("utf-8")
print(text)


end = timeit.default_timer()
print("Elapsed time is", (end - start), "ms.")
