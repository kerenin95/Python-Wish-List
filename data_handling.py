import csv

def read_data():
    """Reads in from a csv and returns the data"""
    try:                
        with open(FILENAME, 'r') as csvfile:
            csv_data = csv.reader(csvfile)
            data = [[item1.strip(), item2.strip()]
                    for item1, item2 in csv_data]
            return data
    except IOError:
        print("No such file or directory")
    except Exception as e:
        print("Error:", e)
    
    return []

def write_data(data):
    """Writes out to a csv"""
    try:
        with open(FILENAME, 'w', newline='') as csvfile:  # if you have a PC
        # with open(FILENAME, 'w') as csvfile:    # if you have a Mac
            csv_writer = csv.writer(csvfile)
            for row in data:
                if row:
                    csv_writer.writerow(row)
    except IOError:
        print("No such file or directory")
    except Exception as e:
        print("Error:", e)

    print("File saved.")

# 22.2 Write valid number error checking
# Takes a value, returns a positive float or zero
def valid_time(num):
    """Makes sure a value is a number and not negative"""

    try:
        num = float(num)

        if num >= 0:
            return num
    except ValueError:
        print("Workout times must be entered as numbers.")
    
    print("Workout times must be positive values.")
    return -1

def table_print(headers, data, widths=10):
    #change here
    """prints a nested list in a double column table format"""
    output = "{:<{}} {:<{}} {:<{}}"

    # print header row
    print(output.format(headers[0], widths, headers[1], widths, headers[2], widths))

    # print dashes to match width (2 cols)
    print("-" * (widths + 1) * 2)

    # print out data (2 cols)
    for item1, item2, item3 in sorted(data):
        print(output.format(item1, widths, item2, widths, item3, widths))
    
    print()

def set_filename(new_name = "test_data.csv"):
    global FILENAME
    FILENAME = new_name

if __name__ == "__main__":
    FILENAME = ""
    set_filename()
    print(FILENAME)

    data = read_data()
    print(data)

    print(valid_time(20))

    table_print(["header1", "header2"], data, 15)

    write_data(data)