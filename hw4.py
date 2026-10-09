web_development = ["Priya", "Arjun", "Fatima"]
data_science = ["Rohan", "Ananya", "Vikram"]
ui_ux = ["Meera", "Sanjay", "Leena"]

all_participants = [web_development, data_science, ui_ux]

web_development.append("John")

data_science.insert(1, "Amina")

ui_ux.pop()

ds_new = data_science.copy()
del data_science

print(web_development[0:1])

name_lengths = [len(name) for name in ds_new]
print(name_lengths)

workshops = {
    "Web Development": web_development,
    "Data Science": ds_new,
    "UI/UX Design": ui_ux,
}
found_in = [name for name, members in workshops.items() if "Asha" in members]
print('Is "Asha" in any workshop list?', any("Asha" in members for members in workshops.values()))
print('"Asha" found in:', found_in)

first_participants = (web_development[:1][0], ds_new[:1][0], ui_ux[:1][0])
print("First participants tuple:", first_participants)



