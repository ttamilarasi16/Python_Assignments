
class MultipleFunctionsSingleClass():
    
    def subfields():
        print ("Sub-fields in AI are:")
        givenlist = ['Machine Learning', 'Neural Networks', 'Vision', 'Robotics', 'Speech Processing', 'Natural Language Processing']
        for aisubfields in givenlist:
            print( " ", aisubfields)
    
    def OddEven():
        Inputnumber = int(input("Enter the number to find whether it's odd or even"))
        if (Inputnumber % 2 == 1):
            print(Inputnumber, "is Odd number")
        else:
            print(Inputnumber, "is Even number")
    
    
    def MarriageEligibility():
        InputGender = input("Enter your Gender")
        Inputage = int(input("Enter your Age"))
        if ((InputGender == "Male" and Inputage >= 21) or (InputGender == "Female" and Inputage >= 18)):
            print ("You are eligible for marriage")
        else:
            print ("You are not Eligible for marriage")
    
    
    def percentage():
        sub1 = int(input("Enter your Sub1 Mark: "))
        sub2 = int(input("Enter your Sub2 Mark: "))
        sub3 = int(input("Enter your Sub3 Mark: "))
        sub4 = int(input("Enter your Sub4 Mark: "))
        sub5 = int(input("Enter your Sub5 Mark: "))
    
        Subjects = ["subject1", "subject2", "subject3", "subject4", "subject5"]
        Marklist = [sub1, sub2, sub3, sub4, sub5]
    
        for subject, sub in zip(Subjects, Marklist):
            print(f"{subject} = {sub}")
    
        Totalmarks = sub1 + sub2 + sub3 + sub4 + sub5
        Percent = Totalmarks / 5

        print(f"Total: {Totalmarks}")
        print(f"Percentage: {Percent}")


    
    def TriangleAreaPerimeter():
        Height = int(input("Enter the Height of the Triangle:"))
        breadth = int(input("Enter the Breadth of the Triangle:"))
        print("Formula to find Area of the Triangle: (Height * Breadth) / 2")
        print("Area of the Triangle: ",(Height * breadth) / 2)
        Length1 = int(input("Enter the Length1 of the Triangle:"))
        Length2 = int(input("Enter the Length2 of the Triangle:"))
        Length3 = int(input("Enter the Length3 of the Triangle:"))
        print("Formula to find Perimeter of the Triangle: Length1 + Length2 + Length3")
        print("Perimeter of Triangle: ",Length1 + Length2 + Length3)