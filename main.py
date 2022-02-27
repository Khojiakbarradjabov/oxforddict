import requests

from pprint import pprint as print

app_id = "351b87de"
app_key = "171124dfebe5e4486a99dc2f2f9c978e"
language = "en-gb"

word_id = "earth"
url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()


r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
print(r.status_code)
res = r.json()
print(res)
#print(res['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0])
#print(len(res['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]))
#print(type(res['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]))