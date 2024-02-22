#100DOC_Day3_OddEven.py
print("Welcome to the rollercoaster")

height = int(input("What is your height in cm? "))

bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")

    #check age if/elif/else
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Please pay $5.")
    elif age <= 18:
        bil = 7
        print("Please pay $7.")
    else:
        bill = 12
        print("Please pay $12.")

    #check photo if/elif/else
    wants_photo = input(" Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is {bill}.")

else :
    print("You are too short to ride. Try the kiddy rides!")
