class multiplefunctions:
    def Subfields():
        print("Subfields in AI are :")
        for i in ['Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Natural Language Processing']:
            print(i)
    def oddeven():
        a = int(input("Enter a number: "))
        if a % 2 == 0:
            print(a," is Even number")
        else:
            print(a," is Odd number")
    def Elegible():
        Gender = input("Your gender:")
        Age = int(input("Your Age:"))
        if Gender == 'Male' and Age > 20:
            print('ELIGIBLE')
        elif Gender == 'Female' and Age > 17:
            print('ELIGIBLE')
        else:
            print('NOT ELIGIBLE')
    def percentage():
        subject1 = int(input("Subject1:"))
        subject2 = int(input("Subject2:"))
        subject3 = int(input("Subject3:"))
        subject4 = int(input("Subject4:"))
        subject5 = int(input("Subject5:"))
        Total = subject1+subject2+subject3+subject4+subject5
        print("Total : ",Total)
        print("Percentage : ",Total/500*100)
    def triangle():
        Height = int(input("Height:"))
        Breadth = int(input("Breadth:"))
        print("Area formula: (Height*Breadth)/2")
        Area = (Height*Breadth)/2
        print("Area formula: ",Area)
        Height1 = int(input("Height1:"))
        Height2 = int(input("Height2:"))
        Breadth = int(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        Perimeter = Height1+Height2+Breadth
        print("Perimeter of Triangle: ",Perimeter)
    