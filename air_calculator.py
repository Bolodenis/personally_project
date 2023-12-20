print("Welcome to Air Ticket calculator")
print(" ")

weight = float(input("What is the weight of the luggage in kgs: "))
class_choice = input("Choose your class (Business/Economy): ").lower()

destinations = ["London", "Nairobi", "Dubai", "Cairo", "Paris", "Tokyo", "Delhi"]
destination = input("What is your destination? " + ", ".join(destinations) + ": ")


weight_per_kg_economy = weight * 5
weight_per_kg_business = weight * 8

if weight > 200:
    print("Sorry, we cannot fly exceeding the allowed weight.")
else:
    if destination == "London":
        if class_choice == "business":
            total_cost = weight_per_kg_business * 2000
        else:
            total_cost = weight_per_kg_economy * 1000
    elif destination == "Nairobi":
        if class_choice == "business":
            total_cost = weight_per_kg_business * 1400
        else:
            total_cost = weight_per_kg_economy * 700
    else:
        if class_choice == "business":
            total_cost = weight_per_kg_business * 1000
        else:
            total_cost = weight_per_kg_economy * 677

    total_cost = round(total_cost, 2)  
    print(f"The total cost of your ticket is: ${total_cost:.2f}")
