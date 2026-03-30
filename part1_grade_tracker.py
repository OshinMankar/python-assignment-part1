# TASK 1 - Data Parsing & Profile Cleaning

raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

students = []

for raw in raw_students:
    clean_name = raw["name"].strip().title() # .strip() removes extra spaces --------- # .title() converts the string to Title Case
    clean_roll = int(raw["roll"]) # convert it to an integer
    marks_list_raw = raw["marks_str"].split(", ") #.split(", ") cuts that string at every ", " and gives us a list
    clean_marks = [] #to store the marks as integers

    for mark in marks_list_raw: #to loop through each mark(holds one string) in marks_list one by one
        clean_marks.append(int(mark)) #adds the number to the end of clean_marks


    is_valid = True
    for char in clean_name: #to loop through each character
        if char != " " and not char.isalpha(): #check if character is NOT a space AND NOT a letter
            is_valid = False
            break

    if is_valid:
        validity = "valid name"
    else:
        validity = "invalid name"
    

    student = {"name": clean_name, "roll": clean_roll, "marks": clean_marks}
    students.append(student) #to add cleaned student dictionary to students list

    print("==================================")
    print("student : " + clean_name + "   " + validity)
    print("Roll No : " + str(clean_roll))
    print("Marks   : " + str(clean_marks))
    print("==================================")
    print()

for student in students: #loop through students to find the one with roll number 103
    if student["roll"]==103:
        print(student["name"].upper()) # .upper() converts every letter to uppercase
        print(student["name"].lower()) # .lower() converts every letter to lowercase

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#TASK 2 - Marks Analysis Using Loops & Conditionals

student_name = students[0]["name"] # students[0] is Ayesha - we uase her data as specified in the assignment
subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
marks_list = [88, 72, 95, 60, 78]

print()
print("Results for " + student_name)
print("===========================")

for i in range(len(subjects)): # gives index number - we use i to access the list
    subject = subjects[i]
    mark = marks_list[i]

    if mark >= 90:
        grade = "A+"
    elif mark >= 80:
        grade = "A"
    elif mark >= 70:
        grade = "B"
    elif mark >= 60:
        grade = "C"
    else:
        grade = "F"    
    print(" " + subject + " -- Marks: " + str(mark) + " Grade: " + grade) # mark is integer hence str()

print("==========================================================")
print()

total = 0
for i in range(len(marks_list)):
    total = total + marks_list[i]

average = round(total / len(marks_list), 2)

highest_index = 0
for i in range(len(marks_list)):
    if marks_list[i] > marks_list[highest_index]:
        highest_index = i

lowest_index = 0
for i in range(len(marks_list)):
    if marks_list[i] < marks_list[lowest_index]:
        lowest_index = i

highest_subject = subjects[highest_index]
highest_mark = marks_list[highest_index]
lowest_subject = subjects[lowest_index]
lowest_mark = marks_list[lowest_index]

print("Total Marks : " + str(total))
print("Average Marks : " + str(average))
print("Highest : " + highest_subject + "(" + str(highest_mark) + ")")
print("Lowest : " + lowest_subject + "(" + str(lowest_mark) + ")")

print("----Add New subjects---")
print("Type done as subject name to stop.")
print()

new_subjects_count = 0

while True:
    subject_input = input("enter subject name(or done to stop): ").strip()

    if subject_input.lower() == "done":
        break

    if subject_input == "":
        print("Warning: Subject name cannot be empty. Try again.")
        continue
    marks_input = input("Enter marks for " + subject_input + " (0-100): ").strip()

    if not marks_input.isdigit():
        print("Warning: Marks must be a number. Skipping.")
        continue

    marks_value = int(marks_input)

    if marks_value < 0 or marks_value >100:
        print(" Warning: Marks must be between 0 and 100. Skipping.")
        continue

    subjects.append(subject_input)
    marks_list.append(marks_value)
    new_subjects_count += 1

    print(" Added: " + subject_input + "-" + str(marks_value))
    print()

new_total = 0
for i in range (len(marks_list)):
    new_total =  new_total + marks_list[i]
    
new_average = round(new_total / len(marks_list), 2)

print()
print("==================================")
print("New Subjects added: "+ str(new_subjects_count))
print("Update average :" + str(new_average))
print("===================================")

#TASK 3 : Class Performance Summary

class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]
processed = [] # empty list to store processed student data
for name, marks in class_data:
    total = 0
    for i in range(len(marks)):
        total = total + marks[i]

    average = round(total / len(marks), 2)

    if average >= 60:
        status = "Pass"
    else:
        status = "Fail"
    
    processed.append((name, average, status))

print ("Name             | Average | Status") #header row
print("---------------------------------------")

for i in range(len(processed)): #to print each student row sepeartely
    name = processed[i][0] #unpack the tuple into 3 variables
    average = processed[i][1]
    status = processed[i][2]

    name_column = name + " " * (17 - len(name)) #calculate how many spaces to add after name
    avg_str = format(average,".2f") #.2f means 2 decimal palces, f means fixed point number
    avg_column= " " * (7 - len(avg_str)) + avg_str + " "
    print(name_column + "| " + avg_column + "| " + status)
print()

pass_count = 0 #count how many studensts passed and failed
fail_count = 0

for i in range(len(processed)):
    if processed [i][2] == "Pass":
       pass_count = pass_count + 1
    else:
        fail_count = fail_count + 1

topper_index = 0 #assuming the first student is the topper

for i in range(len(processed)):
    if processed[i][1] > processed[topper_index][1]:
        topper_index = i

topper_name = processed[topper_index][0]
topper_average = processed[topper_index][1]

total_of_averages = 0
for i in range(len(processed)):
    total_of_averages = total_of_averages + processed[i][1]

class_average = round(total_of_averages / len(processed), 2)

print("Students passed   : " + str(pass_count))
print("Students failed   : " + str(fail_count))
print("Class topper      : " + topper_name + " (" + str(topper_average) + ")")
print("Class average     : " + str(class_average))

# TASK 4 - String Manipulation Utility

essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

clean_essay = essay.strip() # removes spaces
print("Step 1 - Stripped essay:")
print(clean_essay)
print()

title_essay = clean_essay.title() #uppercase first letter of every word

print("Step 2 - Title Case:")
print(title_essay)
print()

python_count = clean_essay.count("python") #counts how many times the word "python"

print("Step 3 - Count of 'Python':")
print("python appears " + str(python_count) + " time(s)")
print()

replaced_essay = clean_essay.replace("python", "Python 🐍")

print("Step 4 - After replacing 'python':")
print(replaced_essay)
print()

sentences = clean_essay.split(". ") #cuts the string 

print("Steps 5 - List of sentences:")
print(sentences)
print()

print("Step 6 - numbered sentences:")

for i in range(len(sentences)):
    sentence = sentences[i]

    if not sentence.endswith("."):
        sentence = sentence + "."

    print(str(i+1) + ". " + sentence)
print()
