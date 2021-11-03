# Trevon McKenzie
# 1880601

import csv
import datetime


def by_name(e):
    return e['manufacturer_name']    # a function that sorts the dictionary by manufacturer name


def by_id(e):                         # a function that sorts the dictionary by item ID
    return e['item_ID']


def by_service_date(e):                # a function that sorts the dictionary by service date
    return e['service_date']


def by_price(e):                      # a function that sorts the dictionary by price
    return e['price']


def make_date_object(str_date):       # a function that makes a date object from a string date in the form x/xx/xxxx
    separated_date = str_date.split('/')
    date_object = datetime.datetime(int(separated_date[2]), int(separated_date[0]), int(separated_date[1]))
    return date_object


def make_str_date(date_object):       # a function that makes a string date in the form x/xx/xxxx from a date object
    str_date = date_object.strftime('%m') + '/' + date_object.strftime('%d') + '/' + date_object.strftime('%Y')
    return str_date


i = 0
devices = []
my_list = ['item_ID', 'manufacturer_name', 'item_type', 'damaged']
set_of_types = set()                    # a set that holds the types of devices
current_date = datetime.datetime.now()  # holds current date info.

my_file = open('ManufacturerList.csv', 'r')
reader = csv.reader(my_file, delimiter=',')      # open manufacturer list and cycle through each line
for line in reader:
    j = 0
    devices.append({})                           # create dictionary as element in list
    for item in line:
        if my_list[j] == 'item_ID':
            devices[i][my_list[j]] = int(item)   # convert item id number into integer value and add key-value pair
        else:                                    # to the dictionary
            devices[i][my_list[j]] = item      # add key-value pair to the dictionary
        if my_list[j] == 'item_type':
            set_of_types.add(item)             # add item type to set of types
        j += 1
    i += 1

i = 0

my_file = open('PriceList.csv', 'r')                   # open price list and iterate over each line
reader = csv.reader(my_file, delimiter=',')
for line in reader:
    for ID in line:
        while int(ID) not in devices[i].values():      # match item IDs
            i += 1
        else:
            devices[i]['price'] = int(line[1])         # add the price of the matching item to the dictionary
            i = 0
            break

my_file = open('ServiceDatesList.csv', 'r')            # open service dates list and iterate over each line
reader = csv.reader(my_file, delimiter=',')
for line in reader:
    for ID in line:
        while int(ID) not in devices[i].values():      # match item IDs
            i += 1
        else:
            devices[i]['service_date'] = line[1]       # add the service date of the matching item to the dictionary
            i = 0
            break

sorted_dictionaries = devices.copy()       # create copy of the dictionary
sorted_dictionaries.sort(key=by_name)      # call function to sort dictionary alphabetically

my_file = open('FullInventory.csv', 'w')          # open full inventory file for writing
for device in sorted_dictionaries:
    my_file.write(str(device['item_ID']))         # write device information to the file
    my_file.write(',')
    my_file.write(device['manufacturer_name'])
    my_file.write(',')
    my_file.write(device['item_type'])
    my_file.write(',')
    my_file.write(str(device['price']))
    my_file.write(',')
    my_file.write(device['service_date'])
    my_file.write(',')
    my_file.write(device['damaged'])
    my_file.write('\n')
my_file.close()                                   # close file

sorted_dictionaries.sort(key=by_id)                       # call function to sort by ID

for item_type in set_of_types:                            # iterate over the different item types
    my_file = open(item_type + 'Inventory.csv', 'w')      # open item_type inventory file for writing
    for device in sorted_dictionaries:
        if device['item_type'] == item_type:              # check if the item type of the device matches current item
            my_file.write(str(device['item_ID']))         # type and write device info to file
            my_file.write(',')
            my_file.write(device['manufacturer_name'])
            my_file.write(',')
            my_file.write(str(device['price']))
            my_file.write(',')
            my_file.write(device['service_date'])
            my_file.write(',')
            my_file.write((device['damaged']))
            my_file.write('\n')
    my_file.close()                                      # close file

for device in sorted_dictionaries:                                        # iterate over each device and convert the
    device['service_date'] = make_date_object(device['service_date'])     # service date into a date object. Sort the
sorted_dictionaries.sort(key=by_service_date)                             # dictionary by date

my_file = open('PastServiceDateInventory.csv', 'w')                       # open past service date inventory file
for device in sorted_dictionaries:
    if device['service_date'] < current_date:     # compare each device's service date to the present
        device['service_date'] = make_str_date(device['service_date'])  # convert date objects into str values and write
        my_file.write(str(device['item_ID']))                           # to file
        my_file.write(',')
        my_file.write(device['manufacturer_name'])
        my_file.write(',')
        my_file.write(device['item_type'])
        my_file.write(',')
        my_file.write(str(device['price']))
        my_file.write(',')
        my_file.write(device['service_date'])
        my_file.write(',')
        my_file.write(device['damaged'])
        my_file.write('\n')
    else:
        device['service_date'] = make_str_date(device['service_date'])  # convert date objects into str values
my_file.close()   # close file




sorted_dictionaries.sort(reverse=True, key=by_price)   # sort dictionary by descending price

my_file = open('DamagedInventory.csv', 'w')            # open damaged inventory file for writing
for device in sorted_dictionaries:
    if device['damaged'] == 'damaged':                 # if device is damaged, write device info to file
        my_file.write(str(device['item_ID']))
        my_file.write(',')
        my_file.write(device['manufacturer_name'])
        my_file.write(',')
        my_file.write(device['item_type'])
        my_file.write(',')
        my_file.write(str(device['price']))
        my_file.write(',')
        my_file.write(device['service_date'])
        my_file.write('\n')
my_file.close()    # close file
