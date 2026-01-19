import csv
import requests
from io import StringIO

def load_lexicon(url):
    lexicon = {}
    response = requests.get(url)

    if response.status_code == 200:
        reader = csv.reader(StringIO(response.text), delimiter=',')
        for row in reader:
            lexicon[row[0]] = int(row[1])
    else:
        raise Exception("Failed to load lexicon")

    return lexicon
