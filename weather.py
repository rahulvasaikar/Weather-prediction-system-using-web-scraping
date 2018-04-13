import re
import urllib.request

#http://www.weather-forecast.com/locations/Paris/forecasts/latest

try:
    city = input("Enter you city:")
    url = "http://www.weather-forecast.com/locations/"+city+"/forecasts/latest"

    data = urllib.request.urlopen(url).read()
    data1 = data.decode("utf-8")

    #print(data1)

    m = re.search('</span><p class="b-forecast__table-description-content">',data1)

    start = m.end()
    end = start + 300
    newString = data1[start:end]

    #print(newString)

    m = re.search('</p>',newString)

    end = m.start()
    final = newString[0:end]

    print(final)

except:
    print("city not found")
