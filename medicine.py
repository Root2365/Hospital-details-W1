# Displaying the data for the medicine
def display_data(records):
    counter = 0
    for med in records.medicine_list:
        counter += 1
        print(str(counter) + " " + med.name)
    index = int(input("Choose the number: ")) - 1
    chosen_medicine = records.medicine_list[index]
    print("Medicine Name: "+chosen_medicine.name)
    print("Price: "+str(chosen_medicine.price))
    print("Available Quantity: "+str(chosen_medicine.quantity))

# Removing the data for the medicine
def remove_data(records):
    counter = 0
    for med in records.medicine_list:
        counter += 1
        print(str(counter) + " " + med.name)
    index = int(input("Choose the number: ")) - 1
    chosen_medicine = records.medicine_list[index]
    chosen_medicine.remove_medicine_from_record()

# Editing the price in the medicine list
def edit_price(records):
    counter = 0
    for med in records.medicine_list:
        counter += 1
        print(str(counter) + " " + med.name)
    index = int(input("Choose the number: ")) - 1
    records.medicine_list[index].change_price()

# Adding the quantity of that particular medicine
def add_quantity(records):
    counter = 0
    for med in records.medicine_list:
        counter += 1
        print(str(counter) + " " + med.name)
    index = int(input("Choose the number: ")) - 1
    records.medicine_list[index].add_quantity()


# Calculating the price of the medicine
class medicine:
    def __init__(self):
        self.name = input("Enter the medicine name: ")
        self.price = float(input("Enter the price of the medicine: "))
        self.quantity = int(input("Enter the total amount of the medicine: "))
        self.bought_quantity = 0
        self.cost = 0
        if self.quantity>0:
            self.available = True
        else:
            self.available = False

    def register_medicine(self,records):
        records.medicine_list.append(self)

    def remove_medicine_from_record(self,records):
        records.medicine_list.remove(self)

    def change_price(self):
        self.price = float(input("Enter the new price of the medicine: "))

    def add_quantity(self):
        self.quantity += int(input("Enter the total amount of the medicine added: "))

    def calculate_charge(self):
        if self.available:
            self.check_left_quantity()
            self.bought_quantity = int(input("Enter the amount of "+self.name+" bought: "))
            if self.quantity >= self.bought_quantity:
                self.cost = self.price*self.bought_quantity
                self.quantity = self.quantity - self.bought_quantity
                self.print_purchase()
        else:
            print("This medicine is not currently available.")

    def print_purchase(self):
        print("\nMedicine Name: "+self.name)
        print("Total purchased amount: "+str(self.bought_quantity))
        print("Total cost: "+str(self.cost))

    def check_left_quantity(self):
        print("There are currently "+str(self.quantity)+" of "+self.name+" left.")

    def purchase_finished(self):
        self.cost = 0
        self.bought_quantity = 0
        if self.quantity>0:
            self.available=True
        else:
            self.available=False