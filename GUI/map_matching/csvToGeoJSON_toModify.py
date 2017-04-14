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
#######################################################################
# NEED MODIFICATIONS
#######################################################################
# Required template for LINESTRING type of features
#       { "type": "Feature", 
#       "properties": { "fid": "check_gml.0", "id": 4231222, "highway": "primary", "oneway": "yes", "name": "广场西侧路", "lanes": null, "layer": null, "bridge": null, "public_transport": null },
#       "geometry": { "type": "LineString", "coordinates": [ [ 116.3894568, 39.9061898 ], [ 116.38946060000001, 39.9059947 ], [ 116.3896381, 39.9017362 ], [ 116.38964, 39.9016023 ], [ 116.3896382, 39.9014946 ], [ 116.3896784, 39.9009988 ], [ 116.38971650000001, 39.9005031 ], [ 116.3898158, 39.8987502 ] ] } 
#       },

#######################################################################
# NEED MODIFICATIONS
#######################################################################
# Required template for Point type of features
# PLEASE DEFINE ....


# the head of the geojson file
output = \
    ''' \
{ "type" : "Feature Collection",
    {"features" : [
    '''
#######################################################################
# NEED MODIFICATIONS
#######################################################################
# Required template for geoJson file headers
#       {"type": "FeatureCollection",
#       "crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } },
#       "features": [


# loop through the csv by row skipping the first
iter = 1

#######################################################################
# NEED MODIFICATIONS
#######################################################################
# here we have to modify the assignment of the variable to the template accordingly
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
