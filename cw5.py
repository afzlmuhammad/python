python = {"Rohan", "Ananya", "Vikram"}
data_science = {"Meera", "Sanjay", "Leena"}

python.add("Rohit")

data_science.remove("Leena")

print(python & data_science)

print(python - data_science)

print(python | data_science)

course = {
    "python" : 3,
    "data_science" : 3
}

mycourse = course.copy()
print(mycourse)

enrollment = {
    "Python": len(python),
    "Data Science": len(data_science),
}
print("Current enrollment:", enrollment)

expected_growth = {course: count * 2 for course, count in enrollment.items()}
print("Expected enrollment:", expected_growth)