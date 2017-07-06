import requests
import json

params={'client_id': 'YOUR CLIENT ID HERE',
        'client_secret': 'CLIENT SECRET ',
        'q':'addClass+in:file+language:js+repo:jquery/jquery'}

#NOT WORKING: For some reason github is saying that I need to include at least one user, organization, or repository
def getFilesforLanguage(lang):
    req = requests.get("https://api.github.com/search/code",params)
    data = json.loads(req.text)
    print (data)

getFilesforLanguage('js')


