import csv

fieldnames = ['Time', 'Wert', 'Kommentar']
with open('history.csv', 'w', newline='') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames, dialect="excel")
    csv_writer.writeheader()


def write_history(x_value, sens1, out1):

    with open('history.csv', 'a', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames, dialect="excel")
        info = {
            'Time': x_value,
            'Wert': sens1,
            'Kommentar': out1
        }
        csv_writer.writerow(info)
