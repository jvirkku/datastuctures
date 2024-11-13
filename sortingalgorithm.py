''' To do: implement test cases and performacne analysis time and heat"'''


#refrence: https://www.geeksforgeeks.org/bubble-sort-algorithm/
#Good explanation on how bubble sort works: https://www.youtube.com/watch?v=xli_FI7CuzA 


Grade_Book = {
    "April" : 3,
    "Imogene" : 4,
    "Jo" : 3,
    "Miguel" : 5,
    "Mary" : 4,
    "Jose" : 2,
    "John" : 3,
    "Michael" : 4,
    "Antonio" : 5,
    "Reynaldo" : 4,
    "Jocelyn" : 3,
    "Josephine" : 3,
    "Marites" : 3,
    "Arnel" : 1,
    "Rey" : 4,
    "Grace" : 5,
    "Vilma" : 4,
    "Catherine" : 3,
    "Melanie" : 4,
    "Rose" : 5,
}

grade_book_as_list = list(Grade_Book.items())
#convert the dicionary into a list of tuples of name attached to grade
#so that we can change the poistion, based on the grade, while their grade is still attached to it

print("before")
print(grade_book_as_list)

#implement bubble sort

def bubblesort(grade_book_as_list): #the input can be any list with a numbered tuple memeber
    n = len(grade_book_as_list)
    
    for i in range(n):#"i" will go throguh all the elements in list
        for j in range(0, n-i-1): #last i position should be the largest pair for the "i" iteration
            #"j" will go through the list again but from 0 -> n-i-1, as said

            #this algorithem works by swaping pairs
            #if the right element is smaller than the left, they swap
            #if not they dont

            #oventually it the largest number will bubble up

            #where the first iteration of i find the largest number, will be placed last, so for j it will be n-i-j
            #then the next i will find the secound biggest and so on.

            if grade_book_as_list[j][1] > grade_book_as_list[j+1][1]: #"[1]" is the value linked to the person's name
                #perform swap
                left_element = grade_book_as_list[j] #since list[j] would have a new value after this line
                grade_book_as_list[j] = grade_book_as_list[j+1]
                grade_book_as_list[j+1] = left_element
            else:
                None
                #if the right pair is greater, do nothing


do_sorting = bubblesort(grade_book_as_list) #orders the list from least grade to gratest

sorted_grade_book = dict(grade_book_as_list) #convert the list to a dict

print("output")
print(sorted_grade_book)

print()

def test_output(sorted_grade_book):
    ordered_list = []
    for i in sorted_grade_book.values():
        ordered_list.append(i)
    compared_list = [3,4,3,5,4,2,3,4,5,4,3,3,3,1,4,5,4,3,4,5]
    compared_list_sorted = sorted(compared_list)
    if ordered_list == compared_list_sorted:
        return True
    else:
        return False

do_testing = test_output(sorted_grade_book)
print(do_testing)