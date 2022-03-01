import csv
import datetime

with open('DistanceTable.csv') as csvfile:
    readCSV = list(csv.reader(csvfile, delimiter=','))

with open('DistanceName.csv') as csv_name_file:
    readCSV2 = list(csv.reader(csv_name_file, delimiter=','))

    #O(1) constant
    #this calculates the total distance traveled by truck by adding up individual distances in csv file
    def get_total_distance(row, column, total):
        d = readCSV[row][column]
        if d is '':
            d = readCSV[column][row]

        total += float(d)
        return total
    #O(1)
    #returns current distance between packages
    def get_current_distance(row, column):
        d = readCSV[row][column]
        if d is '':
            d = readCSV[column][row]
        return float(d)

    #the times the trucks leave the hub
    first_leave = ['8:00:00']
    second_leave = ['9:05:00']
    third_leave = ['11:00:00']
    #O(n)
    #calculates total distance for a truck, by taking distance and dividing by 18
    # 18 is the miles per hour each truck am travel.
    #converts that to time with divmod function and then to date time dimeddlta object which can be used in the packages file
    #to calculate distance
    def get_first_package_times(dt):
        t = dt / 18
        m = '{0:02.0f}:{1:02.0f}'.format(*divmod(t * 60, 60))
        new = m + ':00'
        first_leave.append(new)
        total = datetime.timedelta()
        for index in first_leave:
            (hours, min, sec) = index.split(':')
            d = datetime.timedelta(hours=int(hours), minutes=int(min), seconds=int(sec))
            total += d
        return total

    #same as first but for second truck leave
    def get_second_package_times(dt):
        t = dt / 18
        m = '{0:02.0f}:{1:02.0f}'.format(*divmod(t * 60, 60))
        new = m + ':00'
        second_leave.append(new)
        total = datetime.timedelta()
        for index in second_leave:
            (hours, min, sec) = index.split(':')
            d = datetime.timedelta(hours=int(hours), minutes=int(min), seconds=int(sec))
            total += d
        return total
    #same as first but for 3rd truck leave
    def get_third_package_times(dt):
        t = dt / 18
        m = '{0:02.0f}:{1:02.0f}'.format(*divmod(t * 60, 60))
        new = m + ':00'
        third_leave.append(new)
        total = datetime.timedelta()
        for index in third_leave:
            (hours, min, sec) = index.split(':')
            d = datetime.timedelta(hours=int(hours), minutes=int(min), seconds=int(sec))
            total += d
        return total
    #O(1) constant
    #returns the address file
    def get_addy():
        return readCSV2
    #first truck sorted package list and index list
    first_sorted_truck = []
    first_sorted_index = []
    #second truck sorted package list and index list
    second_sorted_truck = []
    second_sorted_index = []
    #third truck sorted package list and index list
    third_sorted_truck = []
    third_sorted_index = []

    # O(1) constant
    first_sorted_index.insert(0, '0')
    second_sorted_index.insert(0, '0')
    third_sorted_index.insert(0, '0')


    # O(1) constant for the following
    #returns the list values
    def first_sorted_index_get():
        return first_sorted_index


    def first_sorted_truck_get():
        return first_sorted_truck


    def second_sorted_index_get():
        return second_sorted_index


    def second_sorted_truck_get():
        return second_sorted_truck


    def third_sorted_index_get():
        return third_sorted_index


    def third_sorted_truck_get():
        return third_sorted_truck
#greedy algorithm formula to find the shortest distance to each package, starting at the hub

#o(n^2), 2 nested loops

    def get_path(dist, truck, loc):
        if len(dist) == 0:
            return dist
        else:  #
            try:
                lowest_value = 50.0 #set the lowest value
                new = 0
                for index in dist: # loop through packages to find the lowest value to the hub
                    if get_current_distance(loc, int(index[1])) <= lowest_value:
                        lowest_value = get_current_distance(loc, int(index[1]))  #
                        new = int(index[1])
                #checks to see what truck the package is associated with and appends the values to the
                #truck list and index lists defined earlier
                #removes this lowest value from the list, as well as sets current location to the new location
                #then it loops through again for each remaining package until the list is empty, the base case to end the loop.
                for index in dist:  #
                    if get_current_distance(loc, int(index[1])) == lowest_value:
                        if truck == 1:
                            first_sorted_truck.append(index)
                            first_sorted_index.append(index[1])
                            dist.pop(dist.index(index))
                            loc = new
                            get_path(dist, 1, loc)
                        elif truck == 2:
                            second_sorted_truck.append(index)
                            second_sorted_index.append(index[1])
                            dist.pop(dist.index(index))
                            loc = new
                            get_path(dist, 2, loc)
                        elif truck == 3:
                            third_sorted_truck.append(index)
                            third_sorted_index.append(index[1])
                            dist.pop(dist.index(index))
                            loc = new
                            get_path(dist, 3, loc)
            except IndexError:
                pass
