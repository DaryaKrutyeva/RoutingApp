#Darya Krutyeva, ID 001110500
import packages
from ReadPackageCsv import get_hash_instance
import datetime


class Main:
    #this is the interface the user will be working with
    #print functions to show welcome message and choices
    print('Thanks for using the Western Governors University Parcel Service')
    print('Please select from the following menu options: ')
    print('1. Track all packages')
    print('2. Track a specific package')
    print('3. Display total distance traveled')
    print('4. Quit')
    choice = input("Input number choice here: ")
    #O(n)
    while choice != '4':
        if choice == '1':
            try:
                #allows user to enter time to check status of packages
                time_input = input('Enter a time to check, in HH:MM:SS format: ')
                (hours, mins, sec) = time_input.split(':')
                converted_input = datetime.timedelta(hours=int(hours), minutes=int(mins), seconds=int(sec))
                for count in range(1,41): #o(n^2) 2 nested loops
                    try:
                        first = get_hash_instance().search(str(count))[9]
                        second = get_hash_instance().search(str(count))[10]
                        (hours, mins, sec) = first.split(':')
                        convert_first = datetime.timedelta(hours=int(hours), minutes=int(mins), seconds=int(sec))
                        (hours, mins, sec) = second.split(':')
                        convert_second = datetime.timedelta(hours=int(hours), minutes=int(mins), seconds=int(sec))
                    except ValueError:
                        pass
                    # if entered time is less than departure time, shows its at hub and when it will depart
                    if convert_first >= converted_input:
                        get_hash_instance().search(str(count))[10] = 'At the Hub'
                        get_hash_instance().search(str(count))[9] = 'Departs at ' + first
                        print('Package ID:', get_hash_instance().search(str(count))[0], '   Address:',
                              get_hash_instance().search(str(count))[2], get_hash_instance().search(str(count))[3],
                              get_hash_instance().search(str(count))[4], get_hash_instance().search(str(count))[5],'  Truck status:',
                              get_hash_instance().search(str(count))[9], '  Delivery status:',
                              get_hash_instance().search(str(count))[10])
                        #if input time greater than departure time
                    elif convert_first <= converted_input:
                        #if package not delivered yet, shows that
                        if converted_input < convert_second:
                            get_hash_instance().search(str(count))[10] = 'On the way'
                            get_hash_instance().search(str(count))[9] = 'Departed at ' + first
                            print('Package ID:', get_hash_instance().search(str(count))[0], '   Address:',
                                  get_hash_instance().search(str(count))[2], get_hash_instance().search(str(count))[3],
                                  get_hash_instance().search(str(count))[4], get_hash_instance().search(str(count))[5],
                                  '  Truck status:',
                                  get_hash_instance().search(str(count))[9], '  Delivery status:',
                                  get_hash_instance().search(str(count))[10])
                        else:
                            #shows what packages were delivered otherwise
                            get_hash_instance().search(str(count))[10] = 'Delivered at ' + second
                            get_hash_instance().search(str(count))[9] = 'Departed at ' + first
                            print('Package ID:', get_hash_instance().search(str(count))[0], '   Address:',
                                  get_hash_instance().search(str(count))[2], get_hash_instance().search(str(count))[3],
                                  get_hash_instance().search(str(count))[4], get_hash_instance().search(str(count))[5],'  Truck status:',
                                  get_hash_instance().search(str(count))[9],'  Delivery status:',
                                  get_hash_instance().search(str(count))[10])
            except IndexError:
                pass
        elif choice == '2': #o(n)
            try:
                count = input('Enter package ID: ') #prompts user to enter package id
                second = get_hash_instance().search(str(count))[10]
                first = get_hash_instance().search(str(count))[9]
                time = input('Enter a time in HH:MM:SS format: ')
                #conveerts time to time delta objects that can be manipulated
                (hours, mins, sec) = time.split(':')
                convert_time = datetime.timedelta(hours=int(hours), minutes=int(mins), seconds=int(sec))
                (hours, mins, sec) = first.split(':')
                convert_first = datetime.timedelta(hours=int(hours), minutes=int(mins), seconds=int(sec))
                (hours, mins, sec) = second.split(':')
                convert_second = datetime.timedelta(hours=int(hours), minutes=int(mins), seconds=int(sec))
                if convert_first >= convert_time: #if package hasn't departed
                    get_hash_instance().search(str(count))[9] = 'Departs at ' + first
                    get_hash_instance().search(str(count))[10] = 'At the Hub'
                    print('Package ID:', get_hash_instance().search(str(count))[0], '  Address:',
                          get_hash_instance().search(str(count))[2], get_hash_instance().search(str(count))[3],
                          get_hash_instance().search(str(count))[4], get_hash_instance().search(str(count))[5],
                          '  Deadline', get_hash_instance().search(str(count))[6],
                          ' Weight:', get_hash_instance().search(str(count))[7], '  Truck status:',
                          get_hash_instance().search(str(count))[9], '  Delivery status:',
                          get_hash_instance().search(str(count))[10])
                elif convert_first <= convert_time: #if package has departed
                    if convert_time < convert_second:
                        get_hash_instance().search(str(count))[10] = 'On the way'
                        get_hash_instance().search(str(count))[9] = 'Departed at ' + first
                        print('Package ID:', get_hash_instance().search(str(count))[0], '   Address:',
                              get_hash_instance().search(str(count))[2], get_hash_instance().search(str(count))[3],
                              get_hash_instance().search(str(count))[4], get_hash_instance().search(str(count))[5],
                              '  Deadline:', get_hash_instance().search(str(count))[6],
                              ' Weight:', get_hash_instance().search(str(count))[7], '  Truck status:',
                              get_hash_instance().search(str(count))[9], '  Delivery status:',
                              get_hash_instance().search(str(count))[10])
                    else: #departed and delivered
                        get_hash_instance().search(str(count))[10] = 'Delivered at ' + second
                        get_hash_instance().search(str(count))[9] = 'Departed at ' + first
                        print('Package ID:', get_hash_instance().search(str(count))[0], '   Address:',
                              get_hash_instance().search(str(count))[2], get_hash_instance().search(str(count))[3],
                              get_hash_instance().search(str(count))[4], get_hash_instance().search(str(count))[5],
                              '  Deadline:', get_hash_instance().search(str(count))[6],
                              ' Weight:', get_hash_instance().search(str(count))[7], '  Truck status:',
                              get_hash_instance().search(str(count))[9], '  Delivery status:',
                              get_hash_instance().search(str(count))[10])
            except ValueError:
                print(ValueError)
                exit()

        elif choice == '3': #shows total distance traveled, O(1)
            print('Trucks completed deliveries with a total of ' + str(packages.total_distance()) + ' miles')
            break
        elif choice == '4':
            exit()

