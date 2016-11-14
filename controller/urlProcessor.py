

from pymongo import MongoClient
import datetime
client = MongoClient('localhost', 27017)


class UrlProcessor:

    db = client['url_shortner']
    urlCollection = db.url_shortner

    def __init__(self):
        self.urlCollection = self.db.url_shortner

    def processUrl(self,url):
        url_entry = {"url" : url,
                     "date" : datetime.datetime.utcnow()}
        print url +" reuqsrt"
        url_id = self.urlCollection.insert_one(url_entry).inserted_id
        print url_id
        return url_id



def main():
    db = client['url_shortner']
    collection = db.url_shortner
    print "hello"
    url_entry = {"url":"http://www.facebook.com",
                 "date":datetime.datetime.utcnow()}

    url_id = collection.insert_one(url_entry).inserted_id
    print url_id



if __name__ == "__main__":
    main()