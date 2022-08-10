from billType import billType
from dateType import dateType
from personType import personType

# Displaying the data for the patient
def display_data(records):
    counter = 0
    for temp in records.patient_list:
        counter += 1
        print(str(counter) + " " + str(temp.ID))
    index = int(input("Choose the number: ")) - 1
    chosen_patient = records.patient_list[index]
    print("Patient ID: "+str(chosen_patient.ID))
    print("name: "+chosen_patient.first_name+" "+chosen_patient.last_name)
    print("age: "+str(chosen_patient.age))
    print("date of birth: "+str(chosen_patient.dob.day+"."+chosen_patient.dob.month+"."+chosen_patient.dob.year))
    print("physician's name: "+chosen_patient.physician_name)
    print("admission date: "+str(chosen_patient.admit_date.day+"."+chosen_patient.admit_date.month+"."+chosen_patient.admit_date.year))
    print("discharge date: "+str(chosen_patient.discharge_date.day+"."+chosen_patient.discharge_date.month+"."+chosen_patient.discharge_date.year))
    print("Bills: ")
    chosen_patient.bill.display_bills()

# Removing the data for the patient
def remove_data(records):
    counter = 0
    for temp in records.patient_list:
        counter += 1
        print(str(counter) + " " + temp.ID)
    index = int(input("Choose the number: ")) - 1
    records.patient_list[index].remove_patient_from_list()
    records.patient_list[index].remove_bill()

# Enter the details for the patient
class patientType(personType):
    def __init__(self):
        super().__init__()
        self.ID = int(input("Enter the patient's ID: "))
        self.age = int(input("Enter the patient's age: "))
        self.dob = dateType(input("Enter the patient's date of birth (dd/mm/yy) : "))
        self.physician_name = input("Enter the physician's name: ")
        self.admit_date = dateType(input("Enter the admission date (dd/mm/yy) : "))
        self.discharge_date = dateType(input("Enter the discharge date (dd/mm/yy) : "))
        self.bill = billType()

    def register_patient(self,records):
        records.patient_list.append(self)

    def remove_patient_from_list(self,records):
        records.patient_list.append(self)

    def add_bill(self,bills,records):
        not_finished = True
        while not_finished:
            print("1. add doctor's fees\n2. add room charges\n3. add medicine charges\n4. finished")
            choice = int(input("Enter the number of your choice: "))
            if choice==4:
                not_finished=False
                continue
            elif choice==1:
                self.bill.add_doctor_fees(records)
            elif choice==2:
                self.bill.add_room_charges(records)
            elif choice==3:
                self.bill.add_medicine_charges(records)
        bills[self.ID] = self.bill

    def remove_bill(self,bills):
        bills.pop(self.ID)