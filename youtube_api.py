from apiclient.discovery import build
from pprint import pprint
from pymongo import MongoClient, DESCENDING

API_KEY = 'AIzaSyAbaVo3R-1EjRp1p6W2HzncCVtuIk02WDA'

def main():
    saveMongo(search())

def search():
    # 통로 뚫기
    youtube = build('youtube', 'v3', developerKey = API_KEY)

    # request

    req =  youtube.search().list(
        part='snippet',
        q='Python',
        type='video',
        maxResults = 1
    )
    i = 0
    while req and i < 3:
        search_res = req.execute()

        results = search_res['items']

        ids =[r['id']['videoId'] for r in results]

        statRes = youtube.videos().list(
            part = 'snippet, statistics',
            id=','.join(ids)
        ).execute()

        items = statRes['items']
        # # yield items
        # for k, v in resultItems.items():
        #     resultItems[k] = int(v)
        yield items
        # 기존 req와 기존 search_res값의 다음 것을 주세요
        req = youtube.search().list_next(req, search_res)
        i += 1



def saveMongo(items):
    mongo_client = MongoClient('localhost', 27017)
    collection = mongo_client.dooodb.pythons
    collection.delete_many({})
    for item in items:
        # pprint(item)
        for k, v in item[0]['statistics'].items():
            item[0]['statistics'][k] = int(v)
            print(k, v)
        # item['statistics']['viewCount'] = int(item['statistics']['viewCount'])    
    dbresult = collection.insert_many(items)
    print('Affected docs is {}'.format(len(dbresult.inserted_ids)))
    lst = collection.find().sort('statistics.viewCount', DESCENDING).limit(10)
    for l in lst:
        stts = item['statistics']
        snp = item['snippet']
        print(stts['ViewCount'], snp['title'])


if __name__ == '__main__':
    main()