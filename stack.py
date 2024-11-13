# This code represents a stack data structure, and in this scenario it is used to track browser history.
# When user surfs internet, the pages visited are logged in a stack. From the stack user can go back to previous pages.


class Browserhistory:
    def __init__(self):
        self.history = []

    def is_empty(self):
        """Check if the history is empty"""
        if len(self.history)== 0:
            return True

    def visit_page(self, item:str):
        """Visited website saves into browser history"""
        self.history.append(item) #add visited page to browser history
        print(f"Visited {item}")

    def go_back(self):
        """Go back to previous page according to browser history"""
        if not self.is_empty(): #check that there is items in history
            latest = self.history.pop() #as you go back to previous page, current gets removed from history
            current = self.history[-1] #current is now last item on the list
            print(f"Going back to {current}from {latest}") 
        else:
            print("There is no previous pages left")

    def current_page(self):
        """Display current website aka last item on the list"""
        print(f"Currently visiting {self.history[-1]}") #display the last item on the list



browser = Browserhistory()
browser.visit_page("google")
browser.visit_page("twitter")
browser.visit_page("facebook")
browser.go_back()
browser.current_page()
browser.visit_page("yahoo")
browser.visit_page("instagram")
browser.visit_page("iltasanomat")
browser.current_page()

for item in browser.history:
    print(item)