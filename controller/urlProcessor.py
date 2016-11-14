

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
        print inputId
        arr = []
        num = inputId
        while num:
            remainder = num % self.BASE62_BASE
            num = num / self.BASE62_BASE
            arr.append(self.BASE62_CHAR[remainder])
        print arr
        arr =[]
        i=0
        while i>0:
            candidateChar = inputId[i-1]
            val , rem = divmod(ord(candidateChar),self.BASE62_BASE)
            arr.append(self.BASE62_CHAR[rem])
            i = i-1
        print arr.reverse()

# TODO
    def decodeBase62(self,encodedInput):
        arr = []

        res = 0
        limit = len(encodedInput)
        for i in xrange(limit):
            res = self.BASE62_CHAR[encodedInput[i]] * 62 + res

        return res

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
    # vl.encodeBase62(545)
    # print vl.decodeBase62("n8")
    print vl.getNextSequence()



if __name__ == "__main__":
    main()