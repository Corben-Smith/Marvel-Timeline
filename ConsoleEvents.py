from Events2 import Get_Event, Display_Events, Display_Timeline

print("============================================")
print("Hello Hero!")
print("Welcome to the Marvel Event Directory (MED)")
print("============================================\n")

while True:
    print("Choose one of the options Below:")
    print("1) See all major events timeline")
    print("2) Look up an event")
    print("3) Exit\n")
    
    choice = input("Enter your choice (1 or 2 or 3):")
    
    if choice == '1':
        Display_Events()
        while True:
            choiceTimeline = input("Do you want to see the timeline graphic? (Y/N)")
            if choiceTimeline == "Y" or choiceTimeline == "y":
                Display_Timeline()
            elif choiceTimeline == "N" or choiceTimeline == "n":
                break
            else:
                print("Follow the rules!")

    elif choice == '2':
        event_name = input("Enter the name of the event: ")
        Get_Event(event_name)
    elif choice == '3':
        print("\nBye")
        print("Better stop that vehicle!!!\n")
        break
    else:
        print("\nInvalid choice. Please enter 1, 2, or 3.\n")