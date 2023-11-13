name = "Alexander Banks"
start_time = input("Enter start time ")
end_time = input("Enter end time ")
tod = input("AM or PM ")
arrest_choice = input("Arrests? ")
citations_choice = input("Citations? ")

print(name)
if tod == "AM":
    print(start_time + " AM","-", end_time + " AM")
elif tod == "PM":
    print(start_time + " PM","-", end_time + " PM")
print("Arrests: " + arrest_choice)
print("Citations: " + citations_choice)