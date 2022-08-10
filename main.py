from records import records
from doctorType import doctorType
from doctorType import display_data as doc_display
from doctorType import remove_data as doc_remove
from doctorType import edit_fees as doc_edit_fees
from doctorType import add_new_speciality as doc_add_sp
from doctorType import edit_speciality as doc_edit_sp
from medicine import medicine as medicineType
from medicine import display_data as med_display
from medicine import remove_data as med_remove
from medicine import add_quantity as med_add_qt
from medicine import edit_price as med_edit_price
from room import room as roomType
from room import display_data as room_display
from room import remove_data as room_remove
from room import edit_charge as room_edit_charge
from room import edit_name as room_edit_name
from patientType import patientType
from patientType import display_data as patient_display
from patientType import remove_data as patient_remove

main_records = records() # keeps the record of all the doctors, rooms and medicine

bills_list = dict() # keeps track of the bill for each patient

main_loop=True

while main_loop:
    register_loop = True
    view_loop = True
    remove_loop = True
    edit_loop = True
    try:
        print("\n\n1.register new data\n2.view existing data\n3.remove existing data\n4.edit information\n5.stop")
        data_choice = int(input("Enter the number of choice: "))
    except ValueError:
        print("Pls enter numbers only")
        continue
    if data_choice==5:
        main_loop=False
        continue
    elif data_choice==1:
        while register_loop:
            try:
                print("\n\n1.register a new doctor\n2.register a new medicine\n3.register a new room\n4.register a new patient\n5.return")
                register_choice = int(input("Enter the number of choice: "))
            except:
                print("Enter numbers only!")
                continue
            if register_choice==5:
                register_loop=False
                continue
            elif register_choice==1:
                temp=True
                while temp:
                    try:
                        doctor = doctorType()
                        temp=False
                    except ValueError:
                        print("The doctor's hourly charge rate should be entered in numbers only")
                        continue

                doctor.register_doctor(main_records)
            elif register_choice==2:
                temp = True
                while temp:
                    try:
                        med = medicineType()
                        temp=False
                    except ValueError:
                        print("Medicine price and quantity should only be numbers only")
                        continue

                med.register_medicine(main_records)
            elif register_choice==3:
                temp = True
                while temp:
                    try:
                        room = roomType()
                        temp=False
                    except ValueError:
                        print("The hourly room charge rate should be numbers only")
                        continue
                room.record_room(main_records)
            elif register_choice==4:
                temp=True
                while temp:
                    try:
                        patient = patientType()
                        temp=False
                    except:
                        print("Invalid value")
                        continue
                temp = True
                while temp:
                    try:
                        patient.add_bill(bills_list,main_records)
                        temp=False
                    except:
                        print("Invalid value")
                        continue
                patient.register_patient(main_records)

    elif data_choice==2:
        if len(main_records.doctors_list)==0 and len(main_records.room_list)==0 and len(main_records.medicine_list)==0 and len(main_records.patient_list)==0:
            print("No data to display yet")
            continue
        while view_loop:
            print("\n\n1.view data about a doctor\n2.view data about a medicine\n3.view data about a room\n4.view data about a patient"
                  "\n5.return")
            try:
                view_choice = int(input("Enter the number of choice: "))
            except ValueError:
                print("Enter numbers only!")
                continue
            if view_choice == 5:
                view_loop = False
                continue
            elif view_choice == 1:
                if len(main_records.doctors_list)==0:
                    print("No doctors yet")
                    continue
                temp=True
                while temp:
                    try:
                        doc_display(main_records)
                        temp=False
                    except:
                        print("Invalid value entered!")
                        continue
            elif view_choice == 2:
                if len(main_records.medicine_list)==0:
                    print("No medicines yet")
                    continue
                temp = True
                while temp:
                    try:
                        med_display(main_records)
                        temp=False
                    except:
                        print("Invalid value entered!")
                        continue
            elif view_choice == 3:
                if len(main_records.room_list)==0:
                    print("No rooms yet")
                    continue
                temp = True
                while temp:
                    try:
                        room_display(main_records)
                        temp=False
                    except:
                        print("Invalid value entered!")
                        continue
            elif view_choice == 4:
                if len(main_records.patient_list)==0:
                    print("No patients yet")
                    continue
                temp = True
                while temp:
                    try:
                        patient_display(main_records)
                        temp=False
                    except:
                        print("Invalid value entered!")
            else:
                print("Invalid selection option!")

    elif data_choice==3:
        if len(main_records.doctors_list)==0 and len(main_records.room_list)==0 and len(main_records.medicine_list)==0 and len(main_records.patient_list)==0:
            print("No data to remove yet")
            continue
        while remove_loop:
            print("\n\n1.remove a doctor\n2.remove a medicine\n3.remove a room\n4.remove a patient\n5.return")
            try:
                remove_choice = int(input("Enter the number of choice: "))
            except ValueError:
                print("Please enter numbers only!")
                continue
            if remove_choice == 5:
                remove_loop = False
                continue
            elif remove_choice == 1:
                if len(main_records.doctors_list)==0:
                    print("No doctors yet")
                    continue
                temp = True
                while temp:
                    try:
                        doc_remove(main_records)
                        temp=False
                    except:
                        print("Invalid value entered!")
                        continue
            elif remove_choice == 2:
                if len(main_records.medicine_list) == 0:
                    print("No medicines yet")
                    continue
                temp = True
                while temp:
                    try:
                        med_remove(main_records)
                        temp=False
                    except:
                        print("Invalid value entered")
                        continue
            elif remove_choice == 3:
                if len(main_records.medicine_list) == 0:
                    print("No rooms yet")
                    continue
                temp = True
                while temp:
                    try:
                        room_remove(main_records)
                        temp=False
                    except:
                        print("Invalid value entered")
                        continue
            elif remove_choice == 4:
                if len(main_records.medicine_list) == 0:
                    print("No patients yet")
                    continue
                temp = True
                while temp:
                    try:
                        patient_remove(main_records)
                        temp=False
                    except:
                        print("Invalid value entered!")
                        continue
            else:
                print("Invalid option number")

    elif data_choice==4:
        if len(main_records.doctors_list)==0 and len(main_records.room_list)==0 and len(main_records.medicine_list)==0 and len(main_records.patient_list)==0:
            print("No data to edit yet")
            continue
        while edit_loop:
            print("\n\n1.edit a doctor's hourly fees\n2.edit a medicine price\n3.edit an hourly charge of a room"
                  "\n4.add a new speciality to a doctor\n5.change the speciality of a doctor\n6.add new medicine quantity"
                  "\n7.change room name\n8.return")
            try:
                edit_choice = int(input("Enter the number of choice: "))
            except ValueError:
                print("Enter numbers only!")
                continue
            if edit_choice == 8:
                edit_loop = False
                continue
            elif edit_choice == 1:
                if len(main_records.doctors_list)==0:
                    print("No doctors yet")
                    continue
                temp = True
                while temp:
                    try:
                        doc_edit_fees(main_records)
                        temp=False
                    except:
                        print("Invalid value")
                        continue

            elif edit_choice == 2:
                if len(main_records.medicine_list) == 0:
                    print("No medicines yet")
                    continue
                temp = True
                while temp:
                    try:
                        med_edit_price(main_records)
                        temp=False
                    except:
                        print("Invalid value")
                        continue
            elif edit_choice == 3:
                if len(main_records.medicine_list) == 0:
                    print("No rooms yet")
                    continue
                temp = True
                while temp:
                    try:
                        room_edit_charge(main_records)
                        temp=False
                    except:
                        print("Invalid value")
                        continue
            elif edit_choice == 4:
                if len(main_records.doctors_list)==0:
                    print("No doctors yet")
                    continue
                temp = True
                while temp:
                    try:
                        doc_add_sp(main_records)
                        temp=False
                    except:
                        print("Invalid value")
                        continue
            elif edit_choice == 5:
                if len(main_records.doctors_list)==0:
                    print("No doctors yet")
                    continue
                temp = True
                while temp:
                    try:
                        doc_edit_sp(main_records)
                        temp=False
                    except:
                        print("Invalid value")
                        continue
            elif edit_choice == 6:
                if len(main_records.medicine_list) == 0:
                    print("No medicines yet")
                    continue
                temp = True
                while temp:
                    try:
                        med_add_qt(main_records)
                        temp=False
                    except:
                        print("Invalid value")
                        continue
            elif edit_choice == 7:
                if len(main_records.medicine_list) == 0:
                    print("No rooms yet")
                    continue
                temp = True
                while temp:
                    try:
                        room_edit_name(main_records)
                        temp=False
                    except:
                        print("Invalid value")
                        continue
            else:
                print("Option number does not exist")
    else:
        print("The option number "+str(data_choice)+" does not exist")