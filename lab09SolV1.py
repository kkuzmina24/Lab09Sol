import csv
from datetime import datetime

#asks the user to enter a filename. If the given name does not exist as a file, the user should be asked again until a valid filename is given.
def input_filename(init_list):
    fileName = input("Enter the movies data file name: ") + ".csv"

    try:
        with open(fileName, "r") as init_file:
            pass
    except:
        print(fileName, " is not valid!")
        input_filename(init_list)
    else:
        load_movie_data(fileName, init_list)

#given the name of a file respecting the csv format outlined above, loads the data into a list of lists.
# **Declare column index constants** at the top of your program for each of the movie fields (release date, title, etc.)
# Cast each field to the appropriate type. **Use try/except** so that your program skips lines in the input file that contain a numerical value that fails to cast.
def load_movie_data(fileName, init_list):
    with open(fileName, "r") as myFile:
        myReader = csv.reader(myFile)

        for line in myReader:
            try:
                for item in line:

                    date_obj = datetime.strptime(str(line[0]), '%m/%d/%Y')
                    title = str(line[1])
                    budget = float(line[2])
                    gross = float(line[3])
            except:
                pass
            else:
                record = [date_obj.date(), title, budget, gross]
                init_list.append(record)



#given a movie dataset as a list of lists, adds a profit column to the data computed as the difference between each movie's gross and its budget.
# This function should not return anything, but rather modify the list in place. (**Hint:** you cannot add a column directly. You need to append a value to each row.)
def add_profit_column(init_list):
    for line in range(len(init_list)):
        profit = init_list[line][3] - init_list[line][2]
        init_list[line].append(profit)




#given a movie dataset as a list of lists, searches the dataset and returns the row index of the movie with the highest profit.
def index_max_profit(init_list):
    max = init_list[0][4]
    index = 0

    for line in range(len(init_list)):
        if max <= init_list[line][4]:
            max = init_list[line][4]
            index = line

    return index

#given a list representing a row of data, prints the information to the console showing column labels followed by the value.
def pretty_print_movie_info(init_list):
    print("Date\t\t Name")

    for line in range(len(init_list)):
        print(str(init_list[line][0]),"\t", init_list[line][1], "\t||Cost = $", round(init_list[line][2], 2), "\tGross = $", round(init_list[line][3], 2),
              "\tProfit = $", round(init_list[line][4], 2))

#given a movie dataset as a list of lists and a filename, saves the dataset to a comma-separated values file of the given name.
def save_movie_data(init_list):
    pass

def main():
    init_list = list()
    input_filename(init_list)

    add_profit_column(init_list)

    index_highest = index_max_profit(init_list)
    print("Index of highest profit", index_highest, "Info", init_list[index_highest])

    pretty_print_movie_info(init_list)

    save_movie_data(init_list)

main()