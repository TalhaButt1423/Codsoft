contact_List = []
print("\t*CONTACT BOOK*")
print("\t<------------>")
while True:
    print()
    print("1. Add new contact")
    print("2. View contact list")
    print("3. Search a contact")
    print("4. Update a contact")
    print("5. Delete a contact")
    print("6. Delete all contacts")
    print()
    choice=input("Enter your choice from above: ")
    if choice=='1'or choice=='2'or choice=='3'or choice=='4'or choice=='5'or choice=='6' :
        if choice=="1":
            save = []
            i=input("Enter the name of contact: ")
            y=input("Enter the phone number: ")
            j=input("Enter the email address: ")
            save.append(i)
            save.append(y)
            save.append(j)
            z=len(i)
            leny=len(y)
            lenj=len(j)
            u=max(len(i),len(y),len(j))
            k=u+len(i)
            contact_List.append(save)
            print("Contact saved successfully !")
        elif choice=='2':
            if len(contact_List)>0:
                print(' '*k+"---<CONTACT LIST>---")
                print("   Name","Phone number","Email Address")
                for x, contact in enumerate(contact_List, start=1):
                    print(f"{x}.", ' '.join(contact))
            else:
                print("Contact list is EMPTY !")
        elif choice=='3':
            to_find=input("Enter the name or phone number of contact: ")
            found_contacts=[]
            for unknown,contacts in enumerate(contact_List, start=1):
                for unknown2,contacts_ in enumerate(contacts,start=1):
                    if to_find in contacts_ or to_find.upper() in contacts_ or to_find.lower() in contacts_:
                        found_contacts.append(contacts)
            len2=len(found_contacts)
            if len2>0:
                for c, h in enumerate(found_contacts, start=1):
                    print(c,'.',' '.join(h))
            else:
                print("Contact not found !")
        elif choice=='4':
            if len(contact_List)>0:
                print(' '*k+"---<CONTACT LIST>---")
                print("   Name", ' ' * u, "Phone number", ' ' * u, "Email Address")
                for x, contact in enumerate(contact_List, start=1):
                    print(f"{x}.", (' ' * u).join(contact))
                to_update=input("Enter the index number of contact to be updated: ")
                new=[]
                if to_update.isdigit():
                    to_update=int(to_update)
                    to_update -= 1
                    lenh = len(contact_List)
                    if to_update < lenh and to_update >= 0:
                        i_ = input("Enter the updated name: ")
                        y_ = input("Enter the updated phone number: ")
                        j_ = input("Enter the updated email address: ")
                        new.append(i_)
                        new.append(y_)
                        new.append(j_)
                        contact_List[to_update] = new
                        print("Contact successfully updated !")
                    else:
                        print("Enter the correct Index number !")
                else:
                    print("Enter the correct Index number !")
            else:
                print("Contact list is EMPTY !")
        elif choice=='5':
            if len(contact_List)>0:
                print(' '*k+"---<CONTACT LIST>---")
                print("   Name", ' ' * u, "Phone number", ' ' * u, "Email Address")
                for x, contact in enumerate(contact_List, start=1):
                    print(f"{x}.", (' ' * u).join(contact))
                delete = int(input("Enter the index number of contact to be deleted: "))
                delete-=1
                lenh_ = len(contact_List)
                print(lenh_)
                if delete < lenh_ and delete > 0:
                    contact_List.pop(delete)
                    print("Contact deleted successfully !")
                else:
                    print("Enter the correct Index number !")
            else:
                print("Contact list is EMPTY !")
        elif choice=='6':
            confirm= input("Are you sure to delete all the stored tasks!\nEnter '0' to confirm: ")
            if confirm== "0":
                contact_List.clear()
                print("All contact details deleted successfully!")
            else:
                print("All contacts remain undeleted!")
                print()

    else:
        print("Enter correct choice from given options i.e(1,2,3,4,5,6) !")