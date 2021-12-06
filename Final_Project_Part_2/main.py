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
set_of_names = set()
current_date = datetime.datetime.now()  # holds current date info.
stored_manufacturer_name = 0
stored_item_type = 0
found = False

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
        if my_list[j] == 'manufacturer_name':
            set_of_names.add(item)
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

i = 0
for device in sorted_dictionaries:
    device['service_date'] = make_date_object(device['service_date'])
    if device['service_date'] < current_date or device['damaged'] == 'damaged':   # delete device in dictionary if
        del sorted_dictionaries[i]                                                # it is past its service date or if it
        continue                                                                  # is damaged
    i += 1

sorted_dictionaries.sort(reverse=True, key=by_price)   # sort dictionary by descending price


queried_item = input("What are you looking for? ")

while queried_item != 'q':                       # execute query until user enters q
    queried_item_list = queried_item.split()

    k = 0
    for item_type in set_of_types:            # check that the user entered only one item type
        for item in queried_item_list:
            if item_type == item:
                k += 1
            if k > 1:
                print("No such item in inventory")

    k = 0
    for name in set_of_names:             # check that the user entered only one manufacturer name
        for item in queried_item_list:
            if name == item:
                k += 1
            if k > 1:
                print("No such item in inventory")

    for device in sorted_dictionaries:                #
        if device['manufacturer_name'] in queried_item_list and device['item_type'] in queried_item_list:
            stored_manufacturer_name = device['manufacturer_name']  # store manufacturer name and item type in variables
            stored_item_type = device['item_type']
            print("Your item is: {} {} {} {}".format(device['item_ID'], device['manufacturer_name'], device['item_type'], device['price']))
            found = True
            break

    if found == True:
        for device in sorted_dictionaries:        # check that the manufacturer name is not the same
            if device['manufacturer_name'] != stored_manufacturer_name and device['item_type'] == stored_item_type:
                print("You may also consider: {} {} {} {}\n".format(device['item_ID'], device['manufacturer_name'], device['item_type'], device['price']))
    else:
        print("No such item in inventory")

    queried_item = input("What are you looking for? ")  # prompt user for input




