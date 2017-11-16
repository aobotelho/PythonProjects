import googlemaps
from datetime import datetime
import csv

ORIGIN_CITY = 0
ORIGIN_STATE = 1
DESTINATION_CITY = 2
DESTINATION_STATE = 3
DISTANCE = 4
HOURS = 5
MINUTES = 6
DECIMAL_TIME = 7

gmaps = googlemaps.Client(key = open('MapsKey.txt','r',encoding='utf-8').read())

with open('Cities.csv',newline='',encoding='utf-8') as myFile, open('FullCities.csv','w',newline='',encoding='utf-8') as writeFile:
    reader = csv.reader(myFile)
    writer = csv.writer(writeFile,delimiter=',')
    #Skip Header
    firstRow = True
    for row in reader:
        if firstRow == True or row[DECIMAL_TIME] != '':
            writer.writerow(row)
            firstRow = False
        else:
            print('Original row: {}'.format(row))
            found = False
            attempts = 0
            while(found == False and attempts <10):
                directions_result = gmaps.directions('{},{}'.format(row[ORIGIN_CITY],row[ORIGIN_STATE]),'{},{}'.format(row[DESTINATION_CITY],row[DESTINATION_STATE]),mode="driving")
                if directions_result != []:
                    directions_result = directions_result[0]['legs'][0]
                    print('Road distance: {}'.format(directions_result['distance']['text']))
                    print('Road duration: {}'.format(directions_result['duration']['text']))

                    #Store distance
                    row[DISTANCE] = directions_result['distance']['text'].split(' ')[0]

                    #Store Time
                    if len(directions_result['duration']['text'].split(' ')) > 2:
                        #Hour
                        row[HOURS] = directions_result['duration']['text'].split(' ')[0]
                        #Minutes
                        row[MINUTES] = directions_result['duration']['text'].split(' ')[2]
                        #Store Hour + decimal(min). e.g. 1h15min = 1.25h
                        row[DECIMAL_TIME] = str(int(directions_result['duration']['text'].split(' ')[2])/60 + int(row[HOURS]))
                    else:
                        #Just minutes
                        row[MINUTES] = directions_result['duration']['text'].split(' ')[0]
                        row[DECIMAL_TIME] = str(int(row[MINUTES])/60)
                    found = True
                else:
                    attempts = attempts + 1
                    print('Did not find route from {} and {}. Tried {} times'.format(row[ORIGIN_CITY],row[DESTINATION_CITY],attempts))
            print('Final row: {}'.format(row))
            writer.writerow(row)

'''
gmaps = googlemaps.Client(key = open('MapsKey.txt','r').read())

now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit")[0]['legs'][0]

print(directions_result)
'''