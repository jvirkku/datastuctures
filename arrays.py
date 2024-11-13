# In this scenario you have math grades for each student which are stored in an array.
# User can calculate average grade, how many instances there are a specific grade, check how many failed the course
# and check how many passed the course

math_grades = [4, 3, 5, 3, 4, 2, 1, 5, 0, 0, 5, 4, 3, 3, 3]  # grades for each student

class CourseGrades: #class takes an array as argument
    def __init__(self, mathlist):
        self.mathlist = mathlist

    def calculate_average(self): 
        """calculate the average grade"""
        return sum(self.mathlist)/len(self.mathlist) #return the average

    def number_of_grade(self, grade:int): #function takes the number under inspection as argument
        """calculates how many instances there are a specific grade"""
        howmany = 0
        for number in self.mathlist: #travel through the array and check for matching results
            if number == grade:
                howmany += 1 #update the counter as matches are found
        return howmany

    def failed(self): 
        """check how many students failed the course"""
        failed = 0
        for number in self.mathlist:
            if number == 0: #check for matching results and update the counter accordingly
                failed += 1
        return failed

    def passed(self):
        """check how many students passed the course"""
        passed = 0
        for number in self.mathlist:
            if number != 0: #check any grade that is not zero=failed
                passed += 1 #update counter accordingly
        return passed
    
    
grades = CourseGrades(math_grades)
print(grades.calculate_average())
print(grades.number_of_grade(5))
print(grades.failed())
print(grades.passed())
