import keyboard

from Bunny import Bunny
from random import randrange
import time


class Linked_List:
    total_bunnies = 0
    year = 0
    bunny_locations = []

    grid = [[".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."]]

# When Linked List is created, it creates one bunny object that will act as the head of the list.
# This head bunny will be ignored and will only be used as a tool for traversing the list
    def __init__(self):
        self.head = Bunny()

# New bunnies are added at the end of the Linked List. To do so we must traverse through the list using a while loop.
# The while loop condition is to loop as long as the "next" member of the bunny that is being referenced is not none.
# This is done so that the reference variable is referencing the last bunny on the Linked List by the end.
    def append(self, fur=None, location=None):
        file = open("Bunny Year Activity.txt", "a")
        new_bunny = Bunny(fur)
        temp_ptr = self.head
        while temp_ptr.next:
            temp_ptr = temp_ptr.next
        temp_ptr.next = new_bunny
        if location is None:
            new_bunny.x_coordinate, new_bunny.y_coordinate = self.return_coordinates()
        else:
            new_bunny.x_coordinate = location[0]
            new_bunny.y_coordinate = location[1]
        Linked_List.grid[new_bunny.y_coordinate][new_bunny.x_coordinate] = new_bunny.grid_symbol
        Linked_List.total_bunnies += 1
        if Linked_List.year != 0:
            print("ID: " + str(new_bunny.id_number) + " | " + new_bunny.name + " is born!")
            file.write("ID: " + str(new_bunny.id_number) + " | " + new_bunny.name + " is born!\n")
        file.close()

# If we do not need access to the last bunny in the Linked List and just need to access them all one at a time,
# to traverse we use a while loop with the condition to loop as long as the variable is referencing something.
#  By the time the while loop is over, the reference variable will be referencing nothing and it will not be usable
# until the variable is made to reference something else.

    def print_bunnies(self):
        temp_ptr = self.head.next
        while temp_ptr:
            temp_ptr.print()
            temp_ptr = temp_ptr.next

# When removing a bunny from the list, we just make sure it is not referenced to by the previous bunny in their
# "next" member. This is fine since an object not referenced is automatically erased.
    def year_aging(self):
        file = open("Bunny Year Activity.txt", "a")
        back_ptr = self.head
        temp_ptr = self.head.next
        while temp_ptr:
            temp_ptr.aging()
            if temp_ptr.death:
                Linked_List.total_bunnies -= 1
                Linked_List.grid[temp_ptr.y_coordinate][temp_ptr.x_coordinate] = "."
                Bunny.id_list.remove(temp_ptr.id_number)
                print("Bunny " + temp_ptr.name + " has died due to old age")
                file.write("Bunny " + temp_ptr.name + " has died due to old age\n")
                back_ptr.next = temp_ptr.next
                temp_ptr = temp_ptr.next
                continue
            back_ptr = temp_ptr
            temp_ptr = temp_ptr.next
        file.close()

    def manual_cull_check(self):
        limit = 5
        start = time.time()
        print("Press k to cull")
        while time.time() - start < limit:
            if keyboard.is_pressed('k'):
                self.cull_check(True)
                break

    def reproduction(self):
        temp_ptr = self.head.next
        fur = []
        mother_locations = []
        adult_males = 0
        adult_females = 0
        while temp_ptr:
            if temp_ptr.sex == "Female" and temp_ptr.age >= 2 and temp_ptr.radioactive is False:
                adult_females += 1
                fur.append(temp_ptr.fur)
                mother_locations.append([temp_ptr.x_coordinate, temp_ptr.y_coordinate])
            elif temp_ptr.sex == "Male" and temp_ptr.age >= 2 and temp_ptr.radioactive is False:
                adult_males += 1
            temp_ptr = temp_ptr.next
        for female in range(adult_females):
            if adult_males > 0:
                location, availability = Linked_List.area_available(mother_locations[female])
                if availability is True:
                    self.append(fur[female], location)

# When a cull is activated, we first traverse through the list marking which bunnies need to be culled (which
# is half the population) and then we traverse again to remove the marked bunnies. This is done because the
# cull needs to randomly select bunnies, and the easiest way to do that is to generate random numbers that represent
# the bunnies that need to be removed. The alternative is going one at a time and flipping a coin which is not as
# random as it could be.
    def cull_check(self, manual=False):
        file = open("Bunny Year Activity.txt", "a")
        if Linked_List.total_bunnies > 20 or manual is True:
            cull_number = Linked_List.total_bunnies // 2
            print("---Cull starting -- " + str(cull_number) + " to be culled---")
            file.write("---Cull starting -- " + str(cull_number) + " to be culled---\n")
            time.sleep(2)
            total_bunnies = Linked_List.total_bunnies
            index_list = []
            while len(index_list) < cull_number:
                num = randrange(0, total_bunnies)
                if num not in index_list:
                    index_list.append(num)
            index = 0
            temp_ptr = self.head.next

            while temp_ptr:
                if index in index_list:
                    temp_ptr.cull = True
                index += 1
                temp_ptr = temp_ptr.next

            back_ptr = self.head
            temp_ptr = self.head.next
            while temp_ptr:

                if temp_ptr.cull is True:
                    back_ptr.next = temp_ptr.next
                    Linked_List.total_bunnies -= 1
                    Linked_List.grid[temp_ptr.y_coordinate][temp_ptr.x_coordinate] = "."
                    Bunny.id_list.remove(temp_ptr.id_number)
                    print("ID: " + str(temp_ptr.id_number) + " | cull status: " + str(temp_ptr.cull) +
                          " | " + temp_ptr.name + " has been culled")
                    file.write("ID: " + str(temp_ptr.id_number) + " | cull status: " + str(temp_ptr.cull) + " | " +
                               temp_ptr.name + " has been culled\n")
                    temp_ptr = temp_ptr.next
                    continue
                back_ptr = temp_ptr
                temp_ptr = temp_ptr.next

            print("---Cull has ended---")
            file.write("---Cull has ended---\n")
        file.close()

    def print_grid(self):
        file = open("Bunny Year Activity.txt", "a")
        for row in self.grid:
            print("\n")
            file.write("\n")
            for column in row:
                print(column, end=" ")
                file.write(column)
        print("\n")
        file.write("\n")
        file.close()

    def return_coordinates(self):
        while True:
            num_x = randrange(len(Linked_List.grid[0]))
            num_y = randrange(len(Linked_List.grid))
            if (num_x, num_y) not in self.bunny_locations:
                self.bunny_locations.append((num_x, num_y))
                break
        return num_x, num_y

    def update_bunnies(self):
        self.year_aging()
        self.infection_check()
        self.update_symbols()
        self.movement()

    def update_symbols(self):
        temp_ptr = self.head.next
        while temp_ptr:
            temp_ptr.update_symbol()
            Linked_List.grid[temp_ptr.y_coordinate][temp_ptr.x_coordinate] = temp_ptr.grid_symbol
            temp_ptr = temp_ptr.next

# Bunnies can move one spot in a random direction depending on if the spot is available and if it is inside the
# grid. The method first randomly chooses a direction and if that direction is not possible, then removes
# that direction from the pool of choices and chooses another. If no movement options are available the bunny
# does not move.
    def movement(self):
        direction = {0: -1, 1: 1, 2: -1, 3: 1}
        temp_ptr = self.head.next
        while temp_ptr:
            dir_choices = [0, 1, 2, 3]
            while len(dir_choices) > 0:
                choice = randrange(len(dir_choices))
                if dir_choices[choice] == 0 or dir_choices[choice] == 1:
                    if temp_ptr.x_coordinate + direction[dir_choices[choice]] in range(len(Linked_List.grid[0])) and \
                            Linked_List.grid[temp_ptr.y_coordinate][
                                temp_ptr.x_coordinate + direction[dir_choices[choice]]] == ".":
                        Linked_List.grid[temp_ptr.y_coordinate][temp_ptr.x_coordinate] = "."
                        temp_ptr.x_coordinate += direction[dir_choices[choice]]
                        Linked_List.grid[temp_ptr.y_coordinate][temp_ptr.x_coordinate] = temp_ptr.grid_symbol
                        break
                    else:
                        dir_choices.remove(dir_choices[choice])
                elif dir_choices[choice] == 2 or dir_choices[choice] == 3:
                    if temp_ptr.y_coordinate + direction[dir_choices[choice]] in range(len(Linked_List.grid)) and \
                            Linked_List.grid[temp_ptr.y_coordinate + direction[dir_choices[choice]]][
                                temp_ptr.x_coordinate] == ".":
                        Linked_List.grid[temp_ptr.y_coordinate][temp_ptr.x_coordinate] = "."
                        temp_ptr.y_coordinate += direction[dir_choices[choice]]
                        Linked_List.grid[temp_ptr.y_coordinate][temp_ptr.x_coordinate] = temp_ptr.grid_symbol
                        break
                    else:
                        dir_choices.remove(dir_choices[choice])

            if len(dir_choices) == 0:
                print(str(temp_ptr.name) + " had no where to move")
            temp_ptr = temp_ptr.next

# Checks the spaces around each bunny to see if it is next to a radioactive bunny ("X") and if it is,
# makes that bunny radioactive
    def infection_check(self):
        file = open("Bunny Year Activity.txt", "a")
        temp_ptr = self.head.next
        direction = [-1, 1, -1, 1]
        while temp_ptr:
            for i in range(len(direction)):
                if i < 2:
                    if temp_ptr.x_coordinate + direction[i] in range(len(Linked_List.grid[0])) and\
                            Linked_List.grid[temp_ptr.y_coordinate][temp_ptr.x_coordinate + direction[i]]\
                            == "X" and temp_ptr.radioactive is False:
                        temp_ptr.radioactive = True
                        print(str(temp_ptr.name) + " is now radioactive!")
                        file.write(str(temp_ptr.name) + " is now radioactive!\n")
                else:
                    if temp_ptr.y_coordinate + direction[i] in range(len(Linked_List.grid)) and\
                            Linked_List.grid[temp_ptr.y_coordinate + direction[i]][temp_ptr.x_coordinate]\
                            == "X" and temp_ptr.radioactive is False:
                        temp_ptr.radioactive = True
                        print(str(temp_ptr.name) + " is now radioactive!")
                        file.write(str(temp_ptr.name) + " is now radioactive!\n")
            temp_ptr = temp_ptr.next
        file.close()

    def bunny_year(self):
        file = open("Bunny Year Activity.txt", "a")
        if Linked_List.year == 0:
            title = "---Starting Bunnies--- Total Population: " + str(Linked_List.total_bunnies) + "---"
            print(title)
            file.write(title + "\n")
        else:
            title1 = "---Year " + str(Linked_List.year) + "--- Total Population: " + str(Linked_List.total_bunnies)\
                     + "---"
            print(title1)
            file.write(title1 + "\n")
        file.close()

        time.sleep(2)
        self.print_grid()
        self.print_bunnies()
        self.reproduction()
        self.cull_check()

        self.update_bunnies()
        Linked_List.year_past()

        if Linked_List.total_bunnies != 0:
            self.manual_cull_check()

# Same concept as the movement method to see if there is space around mother to place their babies in. If there is no
# space the baby bunny is not born.
    @staticmethod
    def area_available(location):
        direction = {0: -1, 1: 1, 2: -1, 3: 1}
        dir_choices = [0, 1, 2, 3]
        while len(dir_choices) > 0:

            choice = randrange(len(dir_choices))

            if dir_choices[choice] == 0 or dir_choices[choice] == 1:
                if location[0] + direction[dir_choices[choice]] in range(len(Linked_List.grid[0])) and \
                        Linked_List.grid[location[1]][location[0] + direction[dir_choices[choice]]] == ".":
                    return [location[0] + direction[dir_choices[choice]], location[1]], True
                else:
                    dir_choices.remove(dir_choices[choice])
            elif dir_choices[choice] == 2 or dir_choices[choice] == 3:
                if location[1] + direction[dir_choices[choice]] in range(len(Linked_List.grid)) and \
                        Linked_List.grid[location[1] + direction[dir_choices[choice]]][location[0]] == ".":
                    return [location[0], location[1] + direction[dir_choices[choice]]], True
                else:
                    dir_choices.remove(dir_choices[choice])
        if len(dir_choices) == 0:
            return [0, 0], False

    @classmethod
    def end_check(cls):
        if cls.total_bunnies == 0:
            file = open("Bunny Year Activity.txt", "a")
            print("-----No more bunnies. Simulation ending-----")
            file.write("-----No more bunnies. Simulation ending-----")
            file.close()
            return True

    @classmethod
    def year_past(cls):
        cls.year += 1

