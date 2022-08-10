# Displaying data for the room option
def display_data(records):
    counter = 0
    for temp in records.room_list:
        counter += 1
        print(str(counter) + " " + temp.name)
    index = int(input("Choose the number: ")) - 1
    chosen_room = records.room_list[index]
    print("Room Name: "+chosen_room.name)
    print("Hourly charge rate: "+str(chosen_room.hourly_charge_rate))

# Removing data for the room option
def remove_data(records):
    counter = 0
    for temp in records.room_list:
        counter += 1
        print(str(counter) + " " + temp.name)
    index = int(input("Choose the number: ")) - 1
    records.room_list[index].remove_room_from_record()

# Editing the room charges
def edit_charge(records):
    counter = 0
    for temp in records.room_list:
        counter += 1
        print(str(counter) + " " + temp.name)
    index = int(input("Choose the number: ")) - 1
    records.room_list[index].update_charge()

# Editing the name of the room
def edit_name(records):
    counter = 0
    for temp in records.room_list:
        counter += 1
        print(str(counter) + " " + temp.name)
    index = int(input("Choose the number: ")) - 1
    records.room_list[index].update_name()

# Entering the data information about the room
class room:
    def __init__(self):
        self.name = input("Enter the room name: ")
        self.hourly_charge_rate = float(input("Enter the room's hourly charge rate: "))
        self.used_duration = 0
        self.cost = 0

    def record_room(self,records):
        records.room_list.append(self)

    def remove_room_from_record(self,records):
        records.room_list.remove(self)

    def calculate_charge(self):
        duration = input("Enter the duration in the hh:mm:ss format: ")
        duration = duration.split(":")
        hours = int(duration[0])
        minutes = int(duration[1])
        seconds = int(duration[2])
        minutes = round(float(minutes + (seconds / 60)), 2)
        hours = round(float(hours + (minutes / 60)), 2)
        self.used_duration = hours
        self.cost = self.hourly_charge_rate * self.used_duration
        self.print_charge()

    def print_charge(self):
        print("\nduration: "+str(self.used_duration)+" hrs")
        print("cost: "+str(self.cost))

    def finished(self):
        self.used_duration = 0
        self.cost = 0

    def update_charge(self):
        self.hourly_charge_rate = float(input("Enter the room's new hourly charge rate: "))

    def update_name(self):
        self.name = input("Enter the new room name: ")