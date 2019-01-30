from apiclient.discovery import build
from pprint import pprint
from pymongo import MongoClient, DESCENDING

API_KEY = '123456'

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
    while req and i < 5:
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
        for item in items:
            item['statistics']['viewCount'] = int(item['statistics']['viewCount'])    
        # 기존 req와 기존 search_res값의 다음 것을 주세요
        req = youtube.search().list_next(req, search_res)
        i += 1



def saveMongo(items):
    mongo_client = MongoClient('localhost', 27017)
    collection = mongo_client.dooodb.pythons
    # collection.delete_many({})
    dbresult = collection.insert_many(items)
    print('Affected docs is {}'.format(len(dbresult.inserted_ids)))
    # lst = collection.find().sort('statistics.viewCount', DESCENDING).limit(10)
    # for l in lst:
    #     print (l)


if __name__ == '__main__':
    main()