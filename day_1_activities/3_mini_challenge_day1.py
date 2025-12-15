# Project Prompt:

# You are hired to build a Student Lookup Tool for a school front office. The secretary must be able to:

    # Enter a student’s full name

    # Instantly see:

            # CPS ID

            # Homeroom

            # Grade Level

            # Primary Email

            # Students must:

            # Describe the search process

## be able to add new data
# Your program must allow the secretary to ADD a brand new student
# into the system while the program is running.

# Your job is to let the secretary type in a new student just like filling out a registration form.
# Once the form is complete, your program must turn that information into a dictionary and add it to the main list of students.
# If the student already exists (same CPS ID), your program must block the entry to prevent duplicates.

# The program should:
    # 1. Ask the user for the following information:
    #    - CPS ID
    #    - First Name
    #    - Last Name
    #    - Middle Name
    #    - Homeroom
    #    - Grade Level
    #    - Primary Email
    #    - Secondary Email

id= input(" What is your CPS ID?")
for student in student:
    if id == student['CPS ID']:
        print(student[' CPS ID'])

First_name= input(" What is your first name")
for student in student:
    if First_name == student['First name']:
        print(student[' First name'])

Last_name= input(" What is your last name")
for student in student: 
    if Last_name== student[ 'Last name ']:
        print(student[' Last name'])

Middle_Name= input(" What is your middle name")
for student in student:
    if Middle_Name == student[' Middle name']:
        print(student[ ' Middle name'])

Homeroom= input( " What is your Homeroom")
for student in student:
    if Homeroom in student[' Homeroom']:
        print(student[ ' Homeroom'])

Grade_Level= input( " What is your grade level")
for student in student:
    if Grade_Level == student[' Grade Level']:
        print(student[' Grade level'])

Primary_Email= input(" What is your Primary Email")
for student in student:
    if Primary_Email in student[" Primary Email"]:
        print(student[ 'Primary Email'])

Secondary_Email= input(" What is your secondary email")
for student in student:
    if Secondary_Email in student[' Secondary Email']:
        print(student[ ' Secondary Email'])

# 2. Combine the First and Last name into this format:
    #    "Last, First"  



# 3. Store all of the new information into ONE dictionary
    #    that matches the structure of the existing student data.

# 4. Add (append) that new dictionary into the main students list.

# 5. After adding the student, the program must:
    #    - Print a confirmation message
    #    - Print the total number of students in the system
    #    - Print the newly added student record

# 6. The program must NOT delete or overwrite any existing students.

# 7. If the CPS ID already exists in the system:
        #    - Do NOT add the student
        #    - Display an error message saying the CPS ID is already taken



