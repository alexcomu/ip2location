import csv, sys
from pymongo import MongoClient

def process(inputfile):
    connection = MongoClient()

    db = connection.get_database('geoip')
    collection = db.get_collection('geoip')
    with open(inputfile, 'rb') as csvfile:
        ipreader = csv.reader(csvfile, delimiter=',')
        for row in ipreader:
            data = collection.insert_one(
                {
                    "range1":int(row[0]),
                    "range2":int(row[1]),
                    "country_code":row[2],
                    "country":row[3],
                    "region":row[4],
                    "city" = row[5],
                    "lat" = row[6],
                    "lng" = row[7],
                    "zipcode" = row[8],
                    "timezone" = row[9]
                })
            print "Insert: ", data


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "ERROR! Correct usage is:\n"
        print "\t$ python SCRIPT_NAME INPUT_FILE\n"
        sys.exit()
    process(sys.argv[1])
