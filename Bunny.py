from random import randrange
# Bunny objects act as nodes for the Linked List
# So each Bunny has data as well as a reference to the next bunny on the list


class Bunny:
    id_list = []

    def __init__(self, fur=None):
        self.next = None
        self.sex = Bunny.gender()
        self.age = 0
        self.name = self.names()
        self.radioactive = Bunny.radioactive_status()
        self.death = False
        self.cull = False
        self.id_number = Bunny.id_num()
        self.x_coordinate = None
        self.y_coordinate = None
        self.grid_symbol = self.symbol()
        if fur is None:
            self.fur = Bunny.fur_color()
        else:
            self.fur = fur

    def names(self):
        name_list_m = ["Mike", "Orson", "Steve", "Kyle", "Eric"]
        name_list_f = ["Emma", "Ava", "Sophia", "Amelia", "Isabella"]
        num = randrange(0, 5)
        if self.sex == "Female":
            return name_list_f[num]
        return name_list_m[num]

    def aging(self):
        self.age += 1
        if self.age > 10 and self.radioactive is False:
            self.death = True
        elif self.age > 20 and self.radioactive is True:
            self.death = True

    def print(self):
        file = open("Bunny Year Activity.txt", "a")
        bunny_print = "ID: " + str(self.id_number) + " | Name: " + self.name + " | Age: " + str(self.age) + " | Gender: "\
                    + self.sex + " | Fur Color: " + self.fur + " | Radioactive : " + str(self.radioactive) \
                    + " | cull status: " + str(self.cull)
        print(bunny_print)
        file.write(bunny_print + "\n")

    def symbol(self):
        if self.radioactive:
            return "X"
        else:
            if self.sex == "Male":
                return "m"
            else:
                return "f"

    def update_symbol(self):
        if self.age >= 2 and not self.radioactive:
            if self.sex == "Female":
                self.grid_symbol = "F"
            else:
                self.grid_symbol = "M"
        if self.radioactive:
            self.grid_symbol = "X"

# ID numbers are used just for easier differentiation when comparing bunnies. 100 is chosen
# because the population cannot reach that number. IDs given are all unique to the bunny. However
# once a bunny dies, the id number it used may by used by another bunny.
    @staticmethod
    def id_num():
        while True:
            num = randrange(100)
            if num not in Bunny.id_list:
                Bunny.id_list.append(num)
                break
        return num

    @staticmethod
    def gender():
        num = randrange(0, 2)
        if num == 0:
            return "Female"
        return "Male"

    @staticmethod
    def fur_color():
        fur = ["white", "brown", "black", "spotted"]
        num = randrange(0, 4)
        return fur[num]

    @staticmethod
    def radioactive_status():
        num = randrange(0, 100)
        if num < 2:
            return True
        return False







