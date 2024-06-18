# API application programming interface
#itunes API https://itunes.apple.com/search?entity=song&limit=1&term=weezer
# limit=1 shows the song for the artist defined as weezer in term, this downlaod a file
# JSON, Javascript object notation, language agonstic format for exchanging data.

import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
#print(json.dumps(response.json(), indent=2))
o = response.json()

for result in o["results"]:
    print(result["trackName"])
    # print(result)