name = input("Enter your name\n ")
# calculating distance covered from home to campus
dep_time = input("What time did you start the journey?\n ")
arrival_time = input("What time did u arrive?\n ")
time_taken = int(arrival_time) - int(dep_time)

speed = input("At what speed were you moving?\n ")
distance_covered = int(speed) * time_taken

print(f"Hello, {name} you covered {distance_covered} km from home to campus.\n")
print("\t###THANKS 4 USING SPEEDO TEC###")