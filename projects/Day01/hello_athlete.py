name = "Chris Zovko"
weight_kg = 80
sessions_today = 1

minutes = input("How many minutes did you train today? ")
print(f"{name} | {weight_kg}kg | {sessions_today} sessions today | {minutes} minutes")

training_volume = sessions_today * int(minutes)

if training_volume > 120:
    print("Rest day tomorrow")

    