#In this scenario the school organizes a lottery.
#Each participant pull out a number, reads it out to the organizer, which then notes it down along with the participant's name.
#After a couple days the organizer selects the winning number the number the participants pulled out will determine the winner.
#Due to the large number of participants, the organizers will anounce the results publicly to ensure everyone can hear them.
#After choosing pulling the winning number, they need to find who has the winning number.

#A dictionary with the names of the participants and the number they pulled.
lottery_winners = {
    'Jukka': 12345,
    'Riku': 54321,
    'Miko': 11111,
    'Helmi': 22222,
    'Meri': 33333,
    'Hilla': 44444,
    'Eetu': 55555,
    'Jarno': 66666
}

#infinite loop for the input. Loop reads the input as integer(x).
#If it succeesd (meaning, if the inputed value is an intiger) the loop ends, and the value is saved.
#if the input isn't an intiger, it raises value error.
#if value error is raised, prints the message "Please enter a valid number" and the loop repeats
#ands a gap is left between the printout and the input window for clarity
#the loop ends when an integer is inputed

while True:
    try:
        x = int(input("Enter the winning number: "))
        break
    except ValueError:
        print("\nPlease enter a valid number. The lottery numbers are 5 digits long")
        print()


#Changes the "lottery_winners" dictionary to a list of tuples, for searching purposes.
winners_list = list(lottery_winners.items())

#N as the length of the list of tuples
n = len(winners_list)

#Search function.
#The function will go through each pulled out number element ([1]) in a list of tuples.
#If an element matches the inputed winning number it returns it's position.
#If the function runs out on pulled out number elements in the list of tuples and doesn't find a match, it returns -1 to ensure it doesnt return
#any value already existing in a tuple.

def LinearSearch(winners_list, n, x):
    for i in range(0, n):
        if winners_list[i][1] == x:
            return i
    return -1

#winner as the result of the LinearSearch function.
winner = LinearSearch(winners_list, n, x)


#If the result of the search function (aka winner) was 1, returns the message "Number did not enter the lotery pool"
#as it isn't located anywhere in the list of tuples
#if it returns anything else than 1, it prints the message "Winner:" and prints name ([0]) the element with the position of the returned value.
if winner == -1:
    print("Number did not enter the lotery pool")
else:
    print("Winner: ", winners_list[winner][0])