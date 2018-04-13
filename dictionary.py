import re
import urllib.request

try:
    word = input("Enter the word to be searched:")
    url = "http://dictionary.reference.com/browse/"

    url = url + word

    data = urllib.request.urlopen(url).read()
    data1 = data.decode('utf-8')

    #print(data1)

    m = re.search('<meta name="description" content="',data1)
    start = m.end()
    end = start+300

    newString = data1[start:end]
    #print(newString)

    m = re.search("See more.",newString)

    e = m.start()
    definition = newString[0:e]
    print(definition)

except:
    print('Word not found')
