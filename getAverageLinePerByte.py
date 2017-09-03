import requests
import json
import re
params={'client_id': 'YOUR CLIENT ID HERE',
        'client_secret': 'CLIENT SECRET ',
        'q':'addClass+in:file+language:js+user:jquery'}

#NOT WORKING: For some reason github is saying that I need to include at least one user, organization, or repository
def getLink(lang,user):
    url = "https://api.github.com/search/code?q=all+in:file+language:"+lang+"+user:" + user
    req = requests.get(url)
    data = json.loads(req.text)
    filesList = data['items']
    urls = []
    for file in filesList:
        urls.append(file['html_url'])

    return (urls)
def getBytesPerLine(url="https://github.com/google/mysql-protobuf/blob/467cda676afaa49e762c5c9164a43f6ad31a1fbf/storage/ndb/mcc/frontend/dojo/dojox/highlight/languages/_all.js"):
    bytesPerLine= 0
    req = requests.get(url)
    html = req.text
    print (html)
    #p = re.compile(html)
    #print(p.search(' lines (',' sloc) <span class=\"file-info-divider"></span>').span())

    return bytesPerLine
#getLink('js','google')
getBytesPerLine()


