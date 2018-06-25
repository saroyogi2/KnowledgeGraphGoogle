import os
import sys
import json
import urllib
import urllib2


class Summarize:
    def __init__(self,text):
        self.text = text
    def summarizetext(self):
        text = self.text
        return text




if __name__ == '__main__':
    text = sys.argv[1] 
    api_key = open('/home/ramakrishnabhat/Ram/KGkey.txt').read()
    api_key = api_key.replace('\n','')
    query = text
    service_url = 'https://kgsearch.googleapis.com/v1/entities:search'
    params = {
        'query' :query,
        'key' : api_key,
        'limit' : 10,
        'indent' : True,
    }
    url = service_url + '?' + urllib.urlencode(params)
    response = json.loads(urllib.urlopen(url).read())
    try:
        for element in response['itemListElement']:
            print element['result']['name'] + ' (' + str(element['resultScore']) + ')'
            # print element['result']['name']
            # print element['resultScore']
            # print element['result']['@type']
            # print element['result']['@id']
            # print element['result']['image']
            # print element['result']['description']
    except:
        pass
    s1 = Summarize(text)
    SumText= s1.summarizetext()
    print SumText
    print query
    print url
    print response

        


