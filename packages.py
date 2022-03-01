
from ReadPackageCsv import get_first_truck_list
from ReadPackageCsv import get_second_truck_list
from ReadPackageCsv import get_third_truck_list
from distance import get_total_distance
from distance import get_first_package_times
from distance import get_second_package_times
from distance import get_third_package_times
from distance import get_current_distance
from distance import get_path
from distance import first_sorted_index_get
from distance import first_sorted_truck_get
from distance import second_sorted_index_get
from distance import second_sorted_truck_get
from distance import third_sorted_index_get
from distance import third_sorted_truck_get
from distance import  get_addy
from ReadPackageCsv import get_hash_instance


#stores leave times for packages
first_package_delivery = []
second_package_delivery = []
third_package_delivery = []
#stores addresses
first_delivery_distance = []
second_delivery_distance = []
third_delivery_distance = []

#these are the times each truck leaves the hub
#first time given as a constraint, for the earliest time the truck can leave the hub
first_leave = '8:00:00'
#second time determined due to packages delayed to 9:05am constraint
second_time = '9:05:00'
#third time chosen to give first driver enough time to deliver the first round of packages
third_time = '11:00:00'


#space time complexity of O(n) due to one for loop
#sets departure time for the packages to when the first truck leaves (8)
index = 0 #counter to make the loop work for each package
for value in get_first_truck_list():
    get_first_truck_list()[index][9] = first_leave
    first_package_delivery.append(get_first_truck_list()[index])
    index += 1
# o(n^2) due to two nested loops
#compares addresses from CSV file and hashmap, and appends to a list of addresses
try:
    count = 0
    for x in first_package_delivery:
        for y in get_addy():
            if x[2] == y[2]:
                first_delivery_distance.append(y[0])
                first_package_delivery[count][1] = y[0]
        count += 1
except IndexError:
    pass

#constant time
#sorts the packages in the first truck by shortest distance from the hub to first package to next etc
#uses greedy algorithm defined in distance
get_path(first_package_delivery, 1, 0)
first_trip_total = 0

#o(n) due to one loop
#calculates total distance for the first truck and current distance (of each package)
ind = 0
for index in range(len(first_sorted_index_get())):
    try:
        first_trip_total = get_total_distance(int(first_sorted_index_get()[index]), int(first_sorted_index_get()[index + 1]), first_trip_total)
        pack = get_first_package_times(get_current_distance(int(first_sorted_index_get()[index]), int(first_sorted_index_get()[index + 1])))
        first_sorted_truck_get()[ind][10] = (str(pack))
        get_hash_instance().update(int(first_sorted_truck_get()[ind][0]), first_package_delivery)
        ind += 1
    except IndexError:
        pass

#same function to set departure time for truck 2
#O(n) due to one loop
index = 0
for value in get_second_truck_list():
    get_second_truck_list()[index][9] = second_time
    second_package_delivery.append(get_second_truck_list()[index])
    index += 1
#same function to compare and append addresses
#O(n^2) due to nested loops
try:
    index = 0
    for k in second_package_delivery:
        for j in get_addy():
            if k[2] == j[2]:
                second_delivery_distance.append(j[0])
                second_package_delivery[index][1] = j[0]
        index += 1
except IndexError:
    pass
#same function as truck 1
#O(1) constant time
get_path(second_package_delivery, 2, 0)
second_total = 0
# same function as truck 1
#O(n) one for loop
i = 0
for index in range(len(second_sorted_index_get())):
    try:
        second_total = get_total_distance(int(second_sorted_index_get()[index]), int(second_sorted_index_get()[index + 1]), second_total)
        pack = get_second_package_times(get_current_distance(int(second_sorted_index_get()[index]), int(second_sorted_index_get()[index + 1])))
        second_sorted_truck_get()[i][10] = (str(pack))
        get_hash_instance().update(int(second_sorted_truck_get()[i][0]), second_package_delivery)
        i += 1
    except IndexError:
        pass

 #same function as truck 1
#O(n) one for loop
index = 0
for value in get_third_truck_list():
    get_third_truck_list()[index][9] = third_time
    third_package_delivery.append(get_third_truck_list()[index])
    index += 1
#same function as truck 1
#O(n^2) nested loops
try:
    index = 0
    for k in third_package_delivery:
        for j in get_addy():
            if k[2] == j[2]:
                third_delivery_distance.append(j[0])
                third_package_delivery[index][1] = j[0]
        index += 1
except IndexError:
    pass
#same function as truck 1
#O(1)
get_path(third_package_delivery, 3, 0)
third_tot = 0
i = 0
#same function as truck 1
#O(n) one for loop
for index in range(len(third_sorted_index_get())):
    try:
        # calculate the total distance of the truck
        third_tot = get_total_distance(int(third_sorted_index_get()[index]), int(third_sorted_index_get()[index + 1]), third_tot)
        # calculate the distance of each package along the route
        pack = get_third_package_times(get_current_distance(int(third_sorted_index_get()[index]), int(third_sorted_index_get()[index + 1])))
        third_sorted_truck_get()[i][10] = (str(pack))
        get_hash_instance().update(int(third_sorted_truck_get()[i][0]), third_package_delivery)
        i += 1
    except IndexError:
        pass
#O(1)
#calculates total distance traveled by adding up all the individual distances for each truck calculated earlier
def total_distance():
    total_distance = first_trip_total + second_total + third_tot
    return total_distance
