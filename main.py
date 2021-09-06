from LinkedList import Linked_List


Farm = Linked_List()

# Adding the first five bunnies

Farm.append()
Farm.append()
Farm.append()
Farm.append()
Farm.append()

# Main loop that will run the simulation
while True:
    Farm.bunny_year()
    if Farm.end_check():
        break
