cities=["Mumbai", "Delhi", "Chennai", "Kolkata", "Bengaluru", "Hyderabad", "Jaipur", "Thiruvananthapuram","Dispur","Ranchi","Lucknow","Dehradun"]
c=0
while True:
    print("\nWelcome to City Selector!")
    print("1. Add a city")
    print("2. Remove a city")
    print("3. Display all cities")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '4':
        print("Exiting the city selector. Goodbye!")
        break
    if choice in ['1','2','3']:
        if choice =='1':
            city = input("Enter your city: ")
            for i in cities:
                if (i == city):
                    c+=1
            if(c>0):        
                    print(f"{city} already exists in the list!")
                    break
            else:
             cities.append(city)
             print(f"{city} added successfully!")
        
        if choice == '2':
            city= input("Enter your city: ")
            cities.remove(city)
            print(f"{city} removed successfully!")
            
        if choice == '3':
            print(cities)