computer_science = {"Alice", "Bob", "Elizabeth", "James", "Fatima"}
medicine = {"Bob", "Chioma", "James", "Yusuf", "Grace"}
engineering = {"Elizabeth", "Chioma", "David", "Alice", "Yusuf"}
#Task 1
print(computer_science & medicine & engineering)
#Task 2
print(computer_science ^ medicine)
#Task 3
print(computer_science - engineering)
# Task 4
print(computer_science | medicine | engineering)
#Task 5
exclusives = set()
comp = computer_science.difference(medicine, engineering)
med = medicine - computer_science - engineering
engine = engineering - computer_science - medicine
exclusives.update(comp, med, engine)
print(exclusives)
#Task 6
seen = medicine & engineering
print("True" if seen else "False")
#Task 7
computer_science.add("Blessing")
print(computer_science)
medicine.remove("Bob")
print(medicine)
#Task 8
present = computer_science | medicine | engineering
print(present - computer_science)










