

from pymongo import MongoClient
import datetime
client = MongoClient('localhost', 27017)


class UrlProcessor:

    db = client['url_shortner']
    urlCollection = db.url_shortner
    urlCollection = db.counter
    BASE62_CHAR = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    BASE62_BASE = 62
    COUNTER_CONST = "url_id_seq"
    COUNTER_INDEX = "url_id_index"

    def __init__(self):
        self.urlCollection = self.db.url_shortner
        self.counter = self.db.counter

    def processUrl(self,url):
        url_entry = {"_id": self.getNextSequence(),
                     "url" : url,
                     "date" : datetime.datetime.utcnow()}
        print url +" reuqsrt"
        url_id = self.urlCollection.insert_one(url_entry).inserted_id
        print url_id
        return url_id

    def getNextSequence(self):
        index = self.counter.find_and_modify(
            query={'_id': self.COUNTER_CONST} , update={"$inc" :{self.COUNTER_INDEX:1}}, upsert=True
        )
        return index[self.COUNTER_INDEX]

    # TODO

    def encodeBase62(self,inputId):
        if inputId ==0 :
          return self.BASE62_CHAR[0]
        arr =[]
        while inputId:
            inputId,rem = divmod(inputId,self.BASE62_BASE)
            arr.append(self.BASE62_CHAR[rem])
        arr.reverse()
        return ''.join(arr)



# TODO
    def decodeBase62(self,encodedInput):
        strlen = len(encodedInput)
        num = 0
        idx = 0
        for char in encodedInput:
            power = (strlen - (idx +1))
            num += (self.BASE62_BASE ** power) * self.BASE62_CHAR.index(char)
            idx+=1
        return num

def main():
    db = client['url_shortner']
    collection = db.url_shortner
    print "hello"
    url_entry = {"url":"http://www.facebook.com",
                 "date":datetime.datetime.utcnow()}

    url_id = collection.insert_one(url_entry).inserted_id
    print url_id

    vl =  UrlProcessor()

    # TODO
    print vl.encodeBase62(545)
    print vl.decodeBase62("8n")
    print vl.getNextSequence()



if __name__ == "__main__":
    main()