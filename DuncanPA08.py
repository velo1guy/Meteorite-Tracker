# North Seattle College, CSC 110
# Week 8 PA
# Author: Elliot Duncan
# Email: elliot.duncan@seattleschools.org

#The purpose of this program is to get different attributes from a csv file based on the name, and making new csv files of meteorites above 
# a certain weight. Sorry this is late, didnt read the last part of the assignment, its been a very long week, still havnt been able to get my 
# friend back to the U.S, but have contacted the embasy and have him in a safe location so thats good...

#main function, calls on selection menue as long as selection number isnt 0
def main():
    #makes empty dictionary
    global met_dictionary
    met_dictionary = {}

    #opens csv and turns it into a string IMPORTANT: for some reason I have to use the path in raw text, nothing else works, im on win 11 and 
    # I think it might have to do with that. I also cant see the files being written in module 2. that being said it all works, and if you are
    # to change the path to just Meteorite_Landings.csv hopefully it will work on your computer. Thank you and sorry for all this
    #UPDATE: just decided to change it to Meteorite_Landings.csv for you, scince I have everything working good, might go back to win 10, this 
    # sucks, now I just get an ERRNO 2... if you have any words of wisdom that would be awesome.
    with open(r"\Meteorite_Landings.csv", "r", encoding="utf-8") as csv_file:
        data = csv_file.read()
    #turn string into lists based on each new line
    rows = data.split("\n")
    #splits row into individual values, can debug using the top row, all of which should come up as -1
    for row in rows:
        value = row.split(",")
        #sets values to their name to keep code orderly, and if there isnt a value that works, sets it to -1, also strips all characters that 
        # would cause problems
        meteorite_name = value[0]
        try:
            weight = int(value[1])
        except: weight = -1
        try:
            lattitude = float(value[2].strip('"() '))
        except:
            lattitude = -1
        try:
            longitude = float(value[3].strip('"() '))
        except:
            longitude = -1
        # Adds meteorites to dictionary
        met_dictionary[meteorite_name] = [weight, lattitude, longitude]

    #initial message
    print("Welcome to the Meteorite Landings Database!")
    #main selection
    selection()
    # loops if selection is not 0, bit of redundancy but I think in this case its fine
    while selection_number != 0:
        selection()

#Selection menue
def selection():
    #set to global for main function, could also just define before main
    global selection_number
    print("""
Enter 1 to look up information on a meteorite by name.
Enter 2 to create a new csv file that contains all meteorites greater than a specified mass.
Enter 0 to exit.

""")
   # goes through possible selections, quits program if selection is 0
    selection_number = input("What would you like to do?: ")
    if selection_number == "1":
        get_meteorite_info(met_dictionary)
    elif selection_number == "2":
        create_mass_file(met_dictionary)
    elif selection_number == "0":
        quit()
    else: 
        error(selection_number)

# Pause function for the end of functions
def pause():
    input("Press enter to continue: ")

#error message function to remove redundancy
def error(input):
    print("")
    print("ERROR:", input, "is not a valid input, please try again")

#Looks up a specified meteorite based on name then prints out info on it
def get_meteorite_info(met_dictionary):
    meteorite_name = input("Please enter the name of the meteorite you'd like to look up: ")
    # checks for metiorite name and when it gets a mach adds it to a list to be used in printout, or returns an error message
    if meteorite_name in met_dictionary:
        met_data = met_dictionary[meteorite_name]
    #printout:
        print("The meteorite named", (meteorite_name), "weighed", met_data[0], "grams and was found at latitude", met_data[1], "and longitude", met_data[2])
        pause()
    else:
        error(meteorite_name)

#Creates new CSV with all asteroids over a specified weight in grams
def create_mass_file(met_dictionary):
    #initial input
    meteorite_weight = input("Please enter a mass in grams: ")
    # creates a new csv in the current directory that is named the specified weight.CSV, then finds any meteorites above the weight and writes 
    # them. For some reason I can only see the file if I do the direct path like I did above, however I changed it back so it should work for 
    # you. I used a printout to debug when I went to just the filename to make sure it was still getting the correct number of Meteorites and
    # it was.
    with open("C:\\Users\\ellio\\OneDrive\Desktop\\Homework\\CSC 110\\PA 8\\"+ meteorite_weight + ".csv", "w", encoding="utf-8") as new_csv:
        for meteorite in met_dictionary:
            list_of_values = met_dictionary[meteorite]
            if list_of_values[0] > int(meteorite_weight):
                new_csv.write(meteorite + "\n")
        print("New file " + meteorite_weight + ".csv created")
    pause()

#Call to main
main()