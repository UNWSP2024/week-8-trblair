# Program #5: Course Info
# Write a program that has the user input a bunch of course ID and course name pairs.  
# For example a course ID could be "COS 2005" and the course name could be "Python Programming."   
# Then ask the user for a subject (like "COS"). 
# Finally, the program will display the ID and name of all the courses having that subject.
def courseslection():
    x=1
    classlist=[]
    while x>0:
        print("Please input a course ID")
        classlist.append(input())
        again=input("Would you like to enter another course id? y/n\n")
        if again=="n":
            x=0
    subject=input("What subject would you like to search for?\n")
    l1 = [i for i in classlist if subject in i]
    print(l1)
courseslection()
