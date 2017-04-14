import csv

# Read in raw data from csv

rawData = csv.reader(open(r'C:\xampp\htdocs\macTrackz\map_matching\sample.csv', 'r'), dialect='excel')

# the template. where data from the csv will be formatted to geojson
template = \
    ''' \
    { "type" : "Feature",
        "id" : %s,
            "geometry" : {
                "type" : "Point",
                "coordinates" : ["%s","%s"]},
        },
    '''

# the head of the geojson file
output = \
    ''' \
{ "type" : "Feature Collection",
    {"features" : [
    '''

# loop through the csv by row skipping the first
iter = 1
for row in rawData:
    id = iter
    lat = row[0]
    lon = row[1]
    output += template % (iter, row[0], row[1])
    iter += 1
        
# the tail of the geojson file
output += \
    ''' \
    ]
}
    '''
    
# opens an geoJSON file to write the output to
outFileHandle = open(r'C:\xampp\htdocs\macTrackz\map_matching\output.geojson', 'w')
outFileHandle.write(output)
outFileHandle.close()    
