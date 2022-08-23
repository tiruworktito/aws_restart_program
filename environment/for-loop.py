
# myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]
# for item in myMixedTypeList:
#     print("{} is of the data type {}".format(item,type(item)))
#     print(myMixedTypeList)
# print (myMixedTypeList [0])
# print (myMixedTypeList [1])
# print (myMixedTypeList [2])
# print (myMixedTypeList [3])
# print (myMixedTypeList [4])
# print (myMixedTypeList [5])
# print("{}" .format(item))
# import csv
# import copy
# myVehicle = {
#     "vin" : "<empty>",
#     "make" : "<empty>" ,
#     "model" : "<empty>" ,
#     "year" : 0,
#     "range" : 0,
#     "topSpeed" : 0,
#     "zeroSixty" : 0.0,
#     "mileage" : 0
# }
# for key, value in myVehicle.items():
#     print("{} : {}".format(key,value))
#     myInventoryList = []
#     with open('car_fleet.csv') as csvFile:
#     csvReader = csv.reader(csvFile, delimiter=',')  
#     lineCount = 0  
#     for row in csvReader:
#         if lineCount == 0:
#             print(f'Column names are: {", ".join(row)}')  
#             lineCount += 1  
#         else:  
#             print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
#             currentVehicle = copy.deepcopy(myVehicle)  
#             currentVehicle["vin"] = row[0]  
#             currentVehicle["make"] = row[1]  
#             currentVehicle["model"] = row[2]  
#             currentVehicle["year"] = row[3]  
#             currentVehicle["range"] = row[4]  
#             currentVehicle["topSpeed"] = row[5]  
#             currentVehicle["zeroSixty"] = row[6]  
#             currentVehicle["mileage"] = row[7]  
#             myInventoryList.append(currentVehicle)  
#             lineCount += 1  
#     print(f'Processed {lineCount} lines.')
#     for myCarProperties in myInventoryList:
#     for key, value in myCarProperties.items():
#         print("{} : {}".format(key,value))
#         print("-----")
import csv
import copy
myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}
for key, value in myVehicle.items():
    print("{} : {}".format(key,value))
    # myInventoryList = []
    with open('car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')  
    lineCount = 0  
    for row in csvReader:
        if lineCount == 0:
            print(f'Column names are: {", ".join(row)}')  
            lineCount += 1  
        else:  
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
            currentVehicle = copy.deepcopy(myVehicle)  
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]  
            myInventoryList.append(currentVehicle)  
            lineCount += 1  
    print(f'Processed {lineCount} lines.')
    currentVehicle = copy.deepcopy(myVehicle)
    for myCarProperties in myInventoryList:
    for key, value in myCarProperties.items():
        print("{} : {}".format(key,value))
        print("-----")