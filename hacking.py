import urllib
#
# u = urllib.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
# data = u.read()
# f = open('rt22.xml', 'wb')
# f.write(data)
# print data
# f.close()

import csv
# web = urllib.urlopen('https://data.nashville.gov/api/views/3wb6-xy3j/rows.csv?accessType=DOWNLOAD')
# data = web.read()
f = open('beer.csv', 'r')
# f.write(data)
for row in csv.DictReader(f):
    try:
        bus_name = row['Business Name']
    except:
        bus_name = None
    print bus_name

