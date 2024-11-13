#This code represents an IT service desk ticket system and is queue data structure. 
# Tickets are added to the queue, and the workers always process the ticket on the list which was added first, so its first in-first out logic.
# The workers can check if the queue is empty, how many tickets the are total in the queue,
# and also take sneak peaks to the next ticket in line and the latest ticket that has been added 


class IT_support:
    def __init__(self):
        self.queue = [] #initialize an empty list ready for tickets

    def is_empty(self):
        """ Checks if the queue is empty """
        if len(self.queue) == 0: 
            print("There are no tickets in queue")
    
    def tickets_in_queue(self):
        """Check how many tickets there are in queue"""
        print(len(self.queue))
    
    def new_ticket(self, item:str):
        """Add a new ticket to the end of the queue"""
        self.queue.append(item) #appends to the end of the list

    def process_next(self):
        """Take the first ticket to processing and remove it from the queue"""
        if not self.is_empty():
            self.queue.pop(0) #removes first item
        else:
            print("No more tickets to be solved!")

    def peak_latest(self):
        """Sneak peak to the latest added ticket in the queue"""
        print(self.queue[-1])
    
    def peak_next(self):
        """Sneak peak to the next ticket waiting to be processed"""
        print(self.queue[0])
    

servicedesk = IT_support()

servicedesk.new_ticket("Forgotten password")
servicedesk.new_ticket("Printer is not working")
servicedesk.new_ticket("Internet connection issues")
servicedesk.tickets_in_queue()
servicedesk.process_next()
servicedesk.peak_latest()
servicedesk.peak_next()
servicedesk.process_next()
servicedesk.tickets_in_queue()