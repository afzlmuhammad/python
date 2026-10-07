a = """This comprehensive Python course provides a complete introduction to programming, transforming total beginners into confident coders. 
Designed for students with no prior computer science background, the curriculum builds your skills step-by-step. 
You will start with core fundamentals—learning how to write your first "Hello World" script, work with variables, and manage interactive user inputs. 
From there, you will dive into foundational programming mechanics like control flow conditionals, reusable functions, loops, and powerful data structures like lists and dictionaries. 
Packed with hands-on exercises and practical real-world projects, this course teaches you how to leverage existing packages to automate tasks, analyze data, and build a strong foundation for advanced topics in artificial intelligence and web development."""

print(len(a))

if a:
    first_char = a[0]
    last_char = a[-1]
    
    print("First character:", first_char)
    print("Last character:", last_char)

print(a[0:49])

result = a.replace("Python", "PYTHON")
print(result)

a = a.lower()

a = a.strip()

words = a.split()
print(words)

if "course" in a:
    print('The word "course" was found in the paragraph.')

print("The course description is {} characters long and has {} words.".format(len(a), len(words)))   
        