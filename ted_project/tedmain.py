import Ted_crawl as T

# for i in range(1, 10):
#     tedcrawl = T.TedCrawl()
#     tedcrawl.engcrawl()
#     tedcrawl.korcrawl()
#     tedcrawl.getDetail()



for i in range(1,10):
    ted = T.Ted()
    ted.sqlEngData()
    ted.sqlKorData()
    ted.sqlDetail()

# updateTalk(123)