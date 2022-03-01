import csv
from hash_map import HashMap

#Creates access to file to be read
with open('PackageData.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    #New hash map object to hold the package values
    hash_instance = HashMap()

    #create lists for each truck to hold the packages
    first_trip = []
    second_trip = []
    third_trip = []

    #reads the CSV file, pairing the values with packageID as the key
    for row in readCSV:
        packageID = row[0]
        address = row[1]
        city = row[2]
        state = row[3]
        zip = row[4]
        deadline = row[5]
        weight = row[6]
        note = row[7]
        departure = ''
        address_comp = ''
        status = 'At hub'
        value = [packageID, address_comp, address, city, state,
                         zip, deadline, weight, note, departure,
                         status]



        #O(1)
        #first truck
        #using given constraints to load packages into the truck lists
        if 'Must' in value[8]:
            first_trip.append(value)
        if '9:00:00' in value[6]:
            first_trip.append(value)
        if '10:30:00' in value[6] and 'None' in value[8]:
            first_trip.append(value)
        if value not in first_trip and '37' in value[7]:
            first_trip.append(value)

       #second truck
        if 'Can' in value[8]:
            second_trip.append(value)
        if 'Delayed' in value[8]:
            second_trip.append(value)
        if '84103' in value [5] and '84104' in value [5] and value not in first_trip:
            second_trip.append(value)
        #third truck, fix wrong address
        if 'Wrong' in value[8]:
            value[2] = '410 S State St'
            value[5] = '84111'
            third_trip.append(value)

        if value not in first_trip and value not in second_trip and value not in second_trip:
            if len(second_trip) > len(third_trip):
                third_trip.append(value)
            else:
                second_trip.append(value)

        #inserting the key, value pair into the hash table from the file
        hash_instance.insert(packageID, value)

    #0(1)
    #returns the instance of the hash_map and list of values
    def get_hash_instance():
        return hash_instance
    #0(1) for each list
    #This function will return the list of packages on each truck

    def get_first_truck_list():
        return first_trip

    def get_second_truck_list():
        return second_trip

    def get_third_truck_list():
        return third_trip
