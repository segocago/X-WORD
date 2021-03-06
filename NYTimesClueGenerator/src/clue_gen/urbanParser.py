import urllib.request
import json

URL = "http://api.urbandictionary.com/v0/define?term="

'''
    Parsing the given word from Urban Dictionary API
    
    :param word - the given word
'''


def getWordFromUrban(word, trace = False):
    # Trace
    if trace is True:
        print("\t\tChecking Urban dictionary for the word: \"" + word + "\"")

    url = URL + word

    defsMixed = []
    exMixed = []

    try:

        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        content = response.read().decode('utf-8');
        contentJson = json.loads(content)


        list = contentJson["list"]

        for i in list:
            if(i["word"] == word):
                definition = i["definition"]
                defsMixed.append(definition)
                example = i["example"]
                exMixed.append(example)

    except Exception as e:
        pass

    # Trace
    if trace is True and len(defsMixed) == 0 and len(exMixed) == 0:
        print("\t\tNo results from Urban dictionary for the word: \"" + word + "\"\n")

    word = {
        "word": word,
        "syn": [],
        "ant": [],
        "def": defsMixed,
        "examples": exMixed
    }
    return word
