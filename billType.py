class billType:
    def __init__(self):
        self.doctor_fees = dict()
        self.medicine_charges = dict()
        self.room_charges = dict()
        self.total_doctor_fees = 0
        self.total_medicine_charges = 0
        self.total_room_charges = 0
        self.total_fees = 0

# Enter the fees
    def display_bills(self):
        print("Doctor Fees: ")
        for doctor_fee in self.doctor_fees.items():
            print(doctor_fee)
        print("Total Doctor Fees: "+str(self.total_doctor_fees))
        print("\n\nMedicine Charges: ")
        for medicine_charge in self.medicine_charges.items():
            print(medicine_charge)
        print("Total Medicine Charges: "+str(self.total_medicine_charges))
        print("\n\nRoom Charges: ")
        for room_charge in self.room_charges.items():
            print(room_charge)
        print("Total Room Charges: "+str(self.total_room_charges))
        print("\n\nTotal Bill: "+str(self.total_fees))

# Enter the doctor name and show doctor fee
    def add_doctor_fees(self,records):
        first_name = input("Enter the first name of the doctor: ")
        last_name = input("Enter the last name of the doctor: ")
        chosen_doctor = None
        for doctor in records.doctors_list:
            if first_name == doctor.first_name and last_name == doctor.last_name:
                chosen_doctor = doctor
                break
        if chosen_doctor==None:
            print("Can't find the doctor with the name "+first_name+" "+last_name+"\n\n")
            return
        else:
            chosen_doctor.calculate_fees()
            if self.doctor_fees.keys().__contains__(chosen_doctor.first_name+" "+chosen_doctor.last_name):
                self.doctor_fees[chosen_doctor.first_name+" "+chosen_doctor.last_name] += chosen_doctor.fees
            else:
                self.doctor_fees[chosen_doctor.first_name+" "+chosen_doctor.last_name] = chosen_doctor.fees
            chosen_doctor.finished()

# Enter room name and calculate charges
    def add_room_charges(self,records):
        name = input("Enter the room name: ")
        chosen_room = None
        for room in records.room_list:
            if name == room.name:
                chosen_room = room
                break
        if chosen_room == None:
            print(name+" can't be found.\n\n")
            return
        else:
            chosen_room.calculate_charge()
            if self.room_charges.keys().__contains__(chosen_room.name):
                self.room_charges[chosen_room.name] += chosen_room.cost
            else:
                self.room_charges[chosen_room.name] = chosen_room.cost
            chosen_room.finished()

# Enter medicine name and show medicine charges
    def add_medicine_charges(self,records):
        name = input("Enter the medicine name: ")
        chosen_medicine = None
        for current_medicine in records.medicine_list:
            if name == current_medicine.name:
                chosen_medicine = current_medicine
                break
        if chosen_medicine == None:
            print(name+" can't be found.\n\n")
            return
        else:
            chosen_medicine.calculate_charge()
            if self.medicine_charges.keys().__contains__(chosen_medicine.name):
                self.medicine_charges[chosen_medicine.name] += chosen_medicine.cost
            else:
                self.medicine_charges[chosen_medicine.name] = chosen_medicine.cost
            chosen_medicine.purchase_finished()

# Enter the total fees
    def calculate_total_fees(self):
        for doctor_fees in self.doctor_fees.values():
            self.total_doctor_fees += doctor_fees
        for medicine_charges in self.medicine_charges.values():
            self.total_medicine_charges += medicine_charges
        for room_charges in self.room_charges.values():
            self.total_room_charges += room_charges
        self.total_fees = self.total_doctor_fees + self.total_medicine_charges + self.total_room_charges