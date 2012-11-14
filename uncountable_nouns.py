import json
import urllib2


def get_json_data(cmcontinue):
    json_data=urllib2.urlopen("http://en.wiktionary.org/w/api.php?action=query&list=categorymembers&format=json&&cmtitle=Category%3AEnglish_uncountable_nouns&cmlimit=500" + cmcontinue).read()
    return json.loads(json_data)


def get_uncountable_nouns():
    all_data = []
    data = get_json_data('')
    
    for page in data.get('query').get('categorymembers'):
        all_data.append(page.get('title'))
 
    while data.has_key('query-continue'):
        cmcontinue = data.get('query-continue').get('categorymembers').get('cmcontinue')
        data = get_json_data('&cmcontinue=' + cmcontinue)
        for page in data.get('query').get('categorymembers'):
            all_data.append(page.get('title'))
            
    return all_data


for item in get_uncountable_nouns():
    print item.encode('utf-8')

