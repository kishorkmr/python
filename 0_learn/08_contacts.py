contacts = {
    "number":4,
    "students":
    [
        {"name":"name1", "email":"email1@mail.com"},
        {"name":"name2", "email":"email2@mail.com"},
        {"name":"name3", "email":"email3@mail.com"},
        {"name":"name4", "email":"email4@mail.com"}
    ]
}

for student in contacts:
    print(student)
    #output
    #number
    #students

for student in contacts["students"]:
    print(student['email'])
    #output
    #email1@mail.com
    #email2@mail.com
    #email3@mail.com
    #email4@mail.com
    #email5@mail.com