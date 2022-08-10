from personType import personType

# Showing the data
def display_data(records):
    counter=0
    for doc in records.doctors_list:
        counter+=1
        print(str(counter)+" "+doc.first_name+" "+doc.last_name)
    index = int(input("Choose the number: "))-1
    doctor = records.doctors_list[index]
    print("Name: " + doctor.first_name + " " + doctor.last_name)
    print("specialities: " + str(doctor.specialities))
    print("hourly_fees: " + str(doctor.hourly_charge))

# Removing the data
def remove_data(records):
    counter = 0
    for doc in records.doctors_list:
        counter+=1
        print(str(counter) + " " + doc.first_name + " " + doc.last_name)
    index = int(input("Choose the number: ")) - 1
    records.doctors_list[index].remove_doctor_from_record(records)

# Editing the fees for the hourly rate
def edit_fees(records):
    counter = 0
    for doc in records.doctors_list:
        counter+=1
        print(str(counter) + " " + doc.first_name + " " + doc.last_name)
    index = int(input("Choose the number: ")) - 1
    records.doctors_list[index].change_hourly_rate()

# Adding a new speciality into the record
def add_new_speciality(records):
    counter = 0
    for doc in records.doctors_list:
        counter+=1
        print(str(counter) + " " + doc.first_name + " " + doc.last_name)
    index = int(input("Choose the number: ")) - 1
    records.doctors_list[index].add_speciality()

# Editing a speciality into the record
def edit_speciality(records):
    counter = 0
    for doc in records.doctors_list:
        counter+=1
        print(str(counter) + " " + doc.first_name + " " + doc.last_name)
    index = int(input("Choose the number: ")) - 1
    records.doctors_list[index].change_speciality()

# Enter the information regarding about doctor's speciality
class doctorType(personType):

    def __init__(self):
        super().__init__()
        self.specialities = list()
        self.hourly_charge = float(input("Enter the doctor's hourly charge rate: "))
        self.duration = 0
        self.fees = 0
        specialities = input("Enter the doctor's speciality/specialities separated by a comma: ")
        if specialities.__contains__(","):
            specialities=specialities.split(",")
            for speciality in specialities:
                self.specialities.append(speciality)
        else:
            self.specialities.append(specialities)

    def remove_doctor_from_record(self,records):
        records.doctors_list.remove(self)

    def register_doctor(self,records):
        records.doctors_list.append(self)

    def change_hourly_rate(self):
        self.hourly_charge = float(input("Enter the doctor's new hourly charge rate: "))

    def calculate_fees(self):
        duration = input("Enter the duration in the hh:mm:ss format: ")
        duration = duration.split(":")
        hours = int(duration[0])
        minutes = int(duration[1])
        seconds = int(duration[2])
        minutes = round(float(minutes+(seconds/60)), 2)
        hours = round(float(hours+(minutes/60)), 2)
        self.duration = hours
        self.fees = self.hourly_charge * self.duration
        self.print_fees()

    def print_fees(self):
        print("\nduration: "+str(self.duration)+" hrs")
        print("fees: "+str(self.fees))

    def finished(self):
        self.duration = 0
        self.fees = 0

    def add_speciality(self):
        new_data = input("Enter the doctor's new speciality: ")
        if new_data.__contains__(","):
            new_data = new_data.split(",")
            for data in new_data:
                self.specialities.append(data)
        else:
            self.specialities.append(new_data)

    def change_speciality(self):
        print("Name: "+self.first_name+" "+self.last_name+"\nspeciality: ")
        counter=0
        for speciality in self.specialities:
            counter+=1
            print(str(counter)+" "+ speciality)

        index = int(input("Choose the number of the speciality that is to be changed: "))-1

        self.specialities.pop(index)
        self.specialities.insert(index, input("Enter the new speciality: "))