'''
API from Oxford Dictionaries
https://developer.oxforddictionaries.com/
'''

import requests
import json

# api informations
app_id = "36bf0575"
app_key = "8f5d545ccb6c07328927196a9d43d917"
language = "en-us"

word_id = "none"
quit_count = 0

while quit_count < 2:
    word = input("word: ")
    if word: word_id = word

    url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()

    r = requests.get(url, headers={
        "app_id": app_id,
        "app_key": app_key})

    data = json.loads(r.text)

    if "error" in data:
        print(data["error"])
    else:
        print("\nDefinitions of '{w}'".format(w = word_id))
        senses = data["results"][0]["lexicalEntries"][0]["entries"][0]["senses"]
        for s in senses:
            if "definitions" in s:
                print("- "+s["definitions"][0])

        if word_id == "quit": quit_count += 1
        else: quit_count = 0

    print()


    # write json to a file (optional)
    file = open("rtext.json", "wb")
    file.write(r.text.encode())
    file.close()
