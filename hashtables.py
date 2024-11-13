from sortingalgorithm import sorted_grade_book

'''
Current iteration of HashTable
index Pos.  ->    1             2               3
key + value ->[[1]["Casper"]][[2]["Billy"]][[3]["Bob", "Joe"]]
    - if a person has a similar grade it will be listed into the same value

This hashtables can output people with similar grade levels and remove
'''

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key): #creates the hash called "index"
        #generates the index of the element by the modolus of the key by the amount of data given
        return key % self.size

    def add(self, key, value):
        #gets the index of each element
        index = self._hash_function(key)
        
        #pairing the value to the key, to be placed in the hash table
        #pair = [key][value as list]

        #if a value has the same key it will be apneded to the same index position
        #if not it will be still be placed as a list alone

        for pair in self.table[index]:
            
            if pair[0] == key: 
                pair[1].append(value) #names get appended to a list of similar grade values
                return
        
        #each element in the table contains the key and the value
        #position is based on the "index" made by the modulus
        self.table[index].append([key, [value]]) #made values a list


    #search function has a complexity of 0(1), linearly searches
    def search(self, key):                       
        index = self._hash_function(key)
        #place read head in the index value of the key
        for pair in self.table[index]:
            #we search though the table to match the key
            if pair[0] == key:
            #place [0] has the key, check if it mathces
                return pair[1]
                #we return the value
        return None

    #uses same concepts above 
    def remove(self, key):
        index = self._hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return

# Example usage:
hash_table = HashTable(5)

N = len(sorted_grade_book)


#value = grade, key = name
#Add all sorted grade book items into the hash table
for key, value in sorted_grade_book.items(): #items gives both key and value
    hash_table.add(value, f"{key}")
'''print("Index output of people with grave level 1")'''
'''print(hash_table.search(1))'''
'''print("Remove people with grade level 1")'''
hash_table.remove(1)
'''print("output of people with grade level 1")'''
'''print(hash_table.search(1))'''