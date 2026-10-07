header = """==============================
      BOOKSTORE RECEIPT
=============================="""


item1_title, item1_price = "Python Basics", 450
item2_title, item2_price = "Data Science Intro", 600

item_template = "Book Title: {}\t- ₹{}\n"
line1 = item_template.format(item1_title, item1_price)
line2 = item_template.format(item2_title, item2_price)

total = item1_price + item2_price
total_line = "\nTOTAL:\t\t\t₹{}\n".format(total)

thank_you = "\nThank you for shopping with us!"

receipt = header + "\n" + line1 + line2 + total_line + thank_you
print(receipt.upper())