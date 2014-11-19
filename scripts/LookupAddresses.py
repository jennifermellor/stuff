__author__ = 'jen'

## Install simplejson 3.3.2: sudo python setup.py install

import csv
import random
import simplejson, urllib
import time

GEOCODE_BASE_URL = 'http://maps.googleapis.com/maps/api/geocode/json'

def geocode(address,sensor, **geo_args):
    geo_args.update({
        'address': address,
        'sensor': sensor
    })

    url = GEOCODE_BASE_URL + '?' + urllib.urlencode(geo_args)
    result = simplejson.load(urllib.urlopen(url))

    #print ''
    print result

    if (result['status'] != 'OK'):
        return 'FAIL'

    results = result['results']
    geometry = results[0]['geometry']
    #print geometry
    location = geometry['location']
    lat = location['lat']
    lng = location['lng']

    #print lat
    #print lng

    route = ''

    addr_comp = results[0]['address_components']
    for comp in addr_comp:
        type = comp['types'][0]
        #print type
        if type == 'route':
            route = comp['short_name'];

    #print 'route: ' + route

#    'address_components':[
#        {
#            'long_name':'1001',
#            'types':[
#                'street_number'
#            ],
#            'short_name':'1001'
#        },
#        {
#            'long_name':'Camino Del Valle',
#            'types':[
#                'route'
#            ],
#            'short_name':'Cam Del Valle'
#        },

    trio = str(lat) + ',' + str(lng) + ',' + route
    return trio



reader = csv.reader(open('ten_k_people.csv', "rb"), delimiter = ",", skipinitialspace=True)


list = []

output = []

for name in reader:
    list.append(name)

## LOOKUP GEOCODES FOR EACH ADDRESS
i=1 ## not too many at a time.
min=260
max=296
output_filename="ten_k_people_lat_lng_" + str(min) + "_" + str(max) + ".csv"
for row in list:
    if (i >= min and i <= max):
        time.sleep(1) # delays
        ##print row
        address1 = row[3]
        address2 = row[4]
        city = row[5]
        state = row[6]
        zip = row[7]
        addr = address1 + ',' + city + ',' + state + ',USA'
        #print addr
        out = geocode(address=addr,sensor="false")
        print out
        if (out == 'FAIL'):
            print 'FAILED AT i = ' + str(i)
            i = max+1
        #else:
        output.append(out.encode('utf-8'))
    i += 1


print i 

resultFile = open(output_filename, 'wb') 
for row in output:
    resultFile.write(row + '\n')

