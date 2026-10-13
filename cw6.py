attendance = [18, 20, 19, 15, 21]
full_days = 0
total = 0
i = 0

while i < 5:
    if attendance[i] >= 20:
        print(attendance[i], "- Full")
        full_days = full_days + 1
    else:
        print(attendance[i], "- Not Full")
    total = total + attendance[i]
    i = i + 1
    
print("Days the class was full:", full_days)

print("Total attendance:", total)


        

        