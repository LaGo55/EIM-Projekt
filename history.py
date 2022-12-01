import csv

fieldnames = ["Time", "Frequency", "Temperature"]
with open('history.csv', 'w', newline='') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames, dialect="excel")
    csv_writer.writeheader()


def write_history(x_value, out1, out2):

    with open('history.csv', 'a', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames, dialect="excel")
        info = {
            "Time": x_value,
            "Frequency": out1,
            "Temperature": out2
        }
        csv_writer.writerow(info)
