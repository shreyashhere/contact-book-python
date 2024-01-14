print("\n\t\t\t\t\tWelcome\tContact Book") # title

def addcontact(name : str,number : str,contact_type : str): # function to add contacts to contacts.csv
   
    file = open("contacts.csv","r") # creating file object to read existing contact details

    all_contacts_data = file.readlines() # read all contacts details 

    file.close() # close file object to release memory

    for i in all_contacts_data: # iterate through each contact ( each person contact )
        contact_detail = i.split(",") # split the name and contact number and other details to list to access individual

        if contact_detail[0] == name: # check if the name is already exists or not
            print("\nName Already Exists , Choose Different Name") # message 
            print("\nExisting Contact Details :-") 
            print("Name : " + contact_detail[0] + "    Number : " + contact_detail[1]) # printing the contact details of the same name matched
            return # return , function call ended ( no further execution of function )
        
        elif contact_detail[1] == number: # check if the number is already exists or not

            print("\nNumber Already Exists , Check The Number And Try Again")
            print("Name : " + contact_detail[0] + "    Number : " + contact_detail[1]) # printing the contact details of the same number matched
            return # return , function call ended ( no further execution of function )
     
    # if number and names are not already exists then after for loop add new contact
    file = open("contacts.csv","a") # create a file object to append data to file contacts.csv
   
    new_contact_detail = name + "," + number + "," + contact_type + "\n" # create a complete string for csv file 

    file.write(new_contact_detail) # append data to file
    
    file.close() # close the file object to release momory

    print("\nContact Details Added Successfully") # after successfully adding new contact details to file displays message
    return # return to called

def remove_contact(name_or_number : str): # function to remove contact based on either number or name

    file = open("contacts.csv","+r") # file object to read and write on contacts.csv

    existing_contact_details = file.readlines() # store all rows in the form of list , readed from file using above file object
    file.close()
    if(len(existing_contact_details) == 0): # if the list is empty , meaning file is empty
        print("\nContact Not Found , You Can Add New Contact Using Option 1") # display message that contact not found
        return # return to where function is called
    
    else: # if list is not empty , meaning file is not empty

        modified_contact_details = [] # new list to store the contact details where the matched contact is removed

        is_contact_match_found = False

        for contact in existing_contact_details: # iterate through each contact to find the match give in arguement of function to remove it
            contact_detail_list = contact.split(",") # split the csv data into list , to access individual column

            if name_or_number == contact_detail_list[0]: # if the name matched from file 

                is_contact_match_found = True # set this boolean variable to true if the number matched from file data

                print("\nContact Found , Name : " + contact_detail_list[0] + "  Number : " + contact_detail_list[1]) # display founded contact to user
                confirm = input("Do You Wanna Delete This Contact Then Enter 'yes' OR Enter Any Other Value : ") # ask user if he/she wanna delete this contact or not

                if(confirm.lower() == "yes"): # if user inputs yes , means he/she wanna delete this contact
                    continue # skips the next codes for this iteration , to avoid the current contact details to append on modified list
                else: # if user inputs other than yes , means he/she dont wanna delete this contact 
                    print("\nContact Remove Operation Cancled") # just displays message that remove operation canceled
                
            elif name_or_number == contact_detail_list[1]: # if the number matched from file data

                is_contact_match_found = True # set this boolean variable to true if the number matched from file data
                
                print("\nContact Found , Name : " + contact_detail_list[0] + "  Number : " + contact_detail_list[1]) # display founded contact to user
                confirm = input("Do You Wanna Delete This Contact Then Enter 'yes' OR Enter Any Other Value : ") # ask user if he/she wanna delete this contact or not

                if(confirm.lower() == "yes"):  # if user inputs yes , means he/she wanna delete this contact
                    continue # skips the next codes for this iteration , to avoid the current contact details to append on modified list

                else: # if user inputs other than yes , means he/she dont wanna delete this contact 
                    print("\nContact Remove Operation Cancled") # just displays message that remove operation canceled

            modified_contact_details.append(contact) # append the current contact details , every iteration
        
        file = open("contacts.csv","w") # create a file object with write mode
    
        file.writelines(modified_contact_details) # write all modified contact ( removed the request contact if found ) to contacts.csv
        file.close() # close the file object to release memory

        if(is_contact_match_found): # check if contact found or not
            print("\nContact Removed Successfully") # display message if contact found , and removed successfully
        else:
            print("\nContact Not Found , You Can Add New Contact Using Option 1") # display message that contact not found

def is_matched(str1 : str , str2: str) -> bool:

    matched = False

    for index,character in enumerate(str1):
        if(character == str2[index]):
            matched = True
        else:
            matched = False
        
    return matched

def search_contact(number_or_name : str):

    file = open("contacts.csv","r")

    all_contacts_data = file.readlines()
    file.close()
    if(len(all_contacts_data) == 0):
        print("\nContact Not Found , You Can Add Contact In 1st Opion Of Main Menu")
    
    else:

        is_contact_found = False
        matched_contact = []

        for single_contact in all_contacts_data:

            contact_details_list = single_contact.split(",")
            
            if(is_matched(number_or_name,contact_details_list[0])):

                matched_contact.append(single_contact)
                is_contact_found = True
            
            elif(is_matched(number_or_name,contact_details_list[1])):

                matched_contact.append(single_contact)
                is_contact_found = True
        
        if(not is_contact_found):

            print("\nContact Not Found , You Can Add Contact In 1st Opion Of Main Menu")

        else:

            print("\nMatched Contacts\n")

            for index,contact in enumerate(matched_contact):
                contact_lst = contact.split(",")
                print(f"{index} )    {contact_lst[0]}    {contact_lst[1]}    {contact_lst[2]}",end="")
            
            print("")

def update_contacts():

    file = open("contacts.csv","r")

    all_contacts_data = file.readlines()

    file.close()

    if(len(all_contacts_data) == 0):
        print("\nNo Contacts Found")
    
    else:
        print("\nAvailable Contacts\n")

        for index,contact in enumerate(all_contacts_data,1):

            contact_detail_list = contact.split(",")

            print(f"{index} ) {contact_detail_list[0]}    {contact_detail_list[1]}    {contact_detail_list[2]}",end="")

        print("")

        update_index = int(input("\nEnter Index Number Of Contact You Want To Update , Or Enter '0' To Cancel : "))

        if(update_index == 0):
            print("\nUpdate Canceled")
        elif update_index-1 > len(all_contacts_data) or (update_index < 0):
            print("\nPlease Enter Valid Index Number From Above")
        else:

            print("\nUpdate Menu\n")

            print("1 ) Update Name ")
            print("2 ) Update Number")
            print("3 ) Update Section ( favourite / normal )")
            print("0 ) None , Exit")

            update_input_choice = int(input("\nEnter Update Input Choice : "))

            message = ""

            if update_input_choice == 1 :

                new_name = input("\nEnter New Name : ")
                old_contact_data = all_contacts_data[update_index-1].split(",")
                updated_contact_str = new_name + "," + old_contact_data[1] + "," + old_contact_data[2]

                all_contacts_data[update_index-1] = updated_contact_str
                
                message = "Name Updated Successfully"

            elif update_input_choice == 2:

                new_number = input("\nEnter New Number : ")

                old_contact_data = all_contacts_data[update_index-1].split(",")
                updated_contact_str = old_contact_data[0] + "," + new_number + "," + old_contact_data[2]

                all_contacts_data[update_index-1] = updated_contact_str
                
                message = "Number Updated Successfully"

            elif update_input_choice == 3:
                old_contact_data = all_contacts_data[update_index-1].split(",")

                if( old_contact_data[2] == "normal\n"):

                    to_favourite = input("\nDo You Wanna Make This Contact Favourite ? (y/n) : ")

                    if(to_favourite.lower() == "y"):
                        updated_contact_str = old_contact_data[0] + "," + old_contact_data[1] + ",favourite\n"
                        all_contacts_data[update_index-1] = updated_contact_str
                        message = "Contact Successfully Added To Favourites"
                    else:
                        message = "Contact Section Remains As It Is"
                    
                else : 

                    remove_from_favourite = input("\nDo You Wanna Remove This Contact From Favourite ? (y/n) : ")

                    if(remove_from_favourite.lower() == "y"):
                        updated_contact_str = old_contact_data[0] + "," + old_contact_data[1] + ",normal\n"
                        all_contacts_data[update_index-1] = updated_contact_str
                        message = "Contact Successfully Removed From Favourites"
                    
                    else:
                        message - "Contact Section Remain As It Is"

            elif update_input_choice == 0:
                print("\nUpdate Canceled")

            file = open("contacts.csv","w")

            file.writelines(all_contacts_data)

            file.close()

            print("\n" + message)


def show_all_contact_details():
    file = open("contacts.csv","r")

    all_contacts_data = file.readlines()

    if(len(all_contacts_data) == 0):
        print("\nNo Contact Found")

    else:

        print("\nAll Available Contact Details\n")

        for index,contact in enumerate(all_contacts_data,1):

            contact_detail_list = contact.split(",")

            print(f"{index} )  {contact_detail_list[0]}    {contact_detail_list[1]}    {contact_detail_list[2]}",end="")
        
        print("")

def show_all_favourite_contact_details():

    file = open("contacts.csv","r")

    all_contacts_data = file.readlines()

    if(len(all_contacts_data) == 0):
        print("\nNo Contacts Found")
    
    else:

        counter = 0

        print("\nFavourite Contact Details")

        for contact in all_contacts_data:

            contact_details_list = contact.split(",")

            if(contact_details_list[2] == "favourite\n"):
                counter += 1
                print(f"{counter} )  {contact_details_list[0]}    {contact_details_list[1]}    {contact_details_list[2]}",end="")
        
        print("\n")

        if(counter == 0):
            print("No Favourite Contact Found")
# main code starts

while True: # starting of main menu

    print("\nMain Menu\n") # main menu title

    print("1 ) Add Contacts") # option for add contact
    print("2 ) Remove Contacts") # option for removing contact
    print("3 ) Search Contacts") # option for searching contact
    print("4 ) Update Contact Details") # option for updating contact details
    print("5 ) Show All Contacts Details") # option for showing all contacts details 
    print("6 ) Show All Favourite Contacts Details") # option for showing all favourite contact details
    print("0 ) Quit") # option to quit app / program

    input_choice = int(input("\n_ : "))

    if( input_choice == 1): # if input choice from user is 1 ( to add contact )

        print("\nADD CONTACT") # title for add contact

        new_contact_name = input("\nEnter Name Of Contact : ") # input the name for new contact
        new_contact_number = input("Enter Number ( With Country Code) eg . +91xxx : ") # input the number for new contact

        while True: # loop till the user enter correct input for add contact as favourite or not 

            is_add_to_fav = input("Wanna Add This Contact As Favourite Or Not ? ( Y / n ) : ") # input from user if he/she want to add this contact to favourites or not

            contact_type = "" # empty string variable to store contact type either favourite or normal

            if is_add_to_fav.lower() == "y": # if user enter y , means yes he/she wants to add this contact as favourites
                contact_type = "favourite" # set the variable value to favourite
                break # break the loop 

            elif is_add_to_fav.lower() == "n": # if user enter n , means no he/she dont want to add this contact as favourite
                contact_type = "normal" # as user enters no than the contact type value set to 'normal'
                break # break the loop

            else: # if user enters other than y or n 
                print("Please Enter Either 'y' or 'n'") # displays message for user to warn him for enter the valid input

        addcontact(new_contact_name,new_contact_number,"normal") # calls the function which adds the new contact to file

    elif input_choice == 2: # if input choice from user is 1 ( to remove contact )

        number_or_name = input("\nEnter Either Number Of Contact Or Name : ")

        remove_contact(number_or_name) # function called to remove contact 

    elif input_choice == 3: 

        number_or_name = input("\nEnter Either Number Or Name Of Contact You Want To Search : ")

        search_contact(number_or_name) # function called to search contact

    elif input_choice == 4:

        update_contacts()

    elif input_choice == 5:

        show_all_contact_details()

    elif input_choice == 6:

        show_all_favourite_contact_details()

    elif input_choice == 0: # if input choice from user is 0 ( to exit program )

        print("\nProgram Exited -\n") # display message
        break # break from main while loop to exit main menu