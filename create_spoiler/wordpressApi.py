import requests
import json
from slugify import slugify
from base64 import b64encode

domain = "mangafast.net"
userAndPass = b64encode(b"wikuwiku:scomptek").decode("ascii")
headers = { 'Authorization' : 'Basic %s' %  userAndPass, "Content-Type": "application/json" }

def wordpressApiInsert( data = False, typePost = False, slugString = False):
    baseUrl = "http://" + domain + "/wp-json/wp/v2/" + typePost
    dataPost = {
            "title" : data['title'],
            "slug" :slugString,
            "type" : typePost,
            "tags" : data['tags'],
            "categories" : [2623, 9343],
            "author" : 1,
            "status" : "publish",
            "fields": {
                "tag5" : data['chapter']
                }
            }

    try:
        newId = requests.post(url=baseUrl, data=json.dumps(dataPost), headers=headers)
        newId = newId.json()
        newId = newId['id']
        if typePost == 'read':
            print(newId)
        return newId
    except:
        return False

def wordpressApi( idPost = False, slugString = False ,typePost = False):
    baseUrl = "http://" + domain + "/wp-json/wp/v2/" + typePost + "?slug=" + str(slugString)

    response = requests.get(baseUrl)
    json_response = response.json()
    if len(json_response) != 0:
        if json_response[0].get("id") != None:
            return json_response[0].get("id")
        else:
            return "error"
    else :
        if typePost == 'novelauthor':
            print(baseUrl)
        return "notfound"

def checkAndPost ( slugString = False, stringTypePost= False, data = False):
    idWP = wordpressApi(slugString = slugString, typePost = stringTypePost)
    if idWP == "notfound":
        idWP = wordpressApiInsert(data = data ,slugString = slugString, typePost=stringTypePost)
    print("Id ", stringTypePost ," : ", idWP)
    return idWP