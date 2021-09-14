# Trevon McKenzie
# 1880601

print("Davy's auto shop services")   #Output menu of automotive services
print("Oil change -- $35")           #and the corresponding cost
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12\n")

services_cost = {"Oil change": 35, "Tire rotation": 19,  #Create dictionary associating service names
                 "Car wash": 7, "Car wax": 12, '-': 0}   #with cost

first_service = input("Select first service:\n")         #user inputs first and second services
second_service = input("Select second service:\n\n")

print("Davy's auto shop invoice\n")
if first_service == '-':              #two if-else statements check if user entered a dash
  print("Service 1: No service")      #which indicates no service
else:
  print("Service 1: {}, ${}".format(first_service, services_cost[first_service]))    #Output requested services
if second_service == '-':                                                            #along with prices
  print("Service 2: No service\n")
else:
  print("Service 2: {}, ${}\n".format(second_service, services_cost[second_service]))
print("Total: $", services_cost[first_service] + services_cost[second_service], sep='')  #output total price of
                                                                                         #requested services
