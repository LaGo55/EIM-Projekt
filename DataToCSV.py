import csv
import functionConditionMonitoring as fCM
fieldnames = ["Time","Data_1","Data_2"]  #,"Data_3"
with open('data.csv', 'w', newline='') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames, dialect="excel")
    csv_writer.writeheader()

def CreateDataBase(x_value, sensor_data_1, sensor_data_2):


    with open('data.csv', 'a', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file,fieldnames=fieldnames, dialect="excel")
        info = {
            "Time": x_value,
            "Data_1": sensor_data_1,
            "Data_2": sensor_data_2,
           # "Data_3": sensor_data_3
                }
        csv_writer.writerow(info)