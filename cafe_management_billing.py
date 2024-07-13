menu = {
    'Papad' : 40,
    'Butter Chicken' : 180,
    'chas' : 20,
    'Tadka Dal' : 100,
    'Chapati' : 10,
    'Tandoori Roti' : 40,
    'Rice' : 80
}

print()
print("Welcome To Cafe Hotel")

print()
print()

for key, value in menu.items():
    print(key," - " , value)

print()
print()

def main():
    total_order = 0

    while True:
        print(" 1 - Add Order ")
        print(" 2 - Remove Order ")
        print(" 3 - Check In ")

        print()

        choice = int(input("Enter Task 1-2-3 :- "))

        print()

        if(choice == 1):
            menu_item = input("Enter Order Item :- ")

            if menu_item in menu:
                print("Your Order Has Added :- ", menu_item)
                total_order += menu[menu_item]

            else:
                print("Dish are Not Available in Cafe Hotel")

        print()
        
        if(choice == 2):
            menu_item = input("Enter Order Item :- ")

            if menu_item in menu:
                print("Your Order Has Removed :- ", menu_item)
                total_order -= menu[menu_item]

            else:
                print("You are not order this item")

        print()

        if(choice == 3):
            print(" Your Bill Price is :- ", total_order)
            break

if __name__ == "__main__":
    main()