import json
from student import Student
students = []
try:
    with open("students.json","r")as file:
        data = json.load(file)
except:
    data=[]

for item in data:
    s=Student(
        item["name"],
        item["roll"],
        item["maths"],
        item["science"],
        item["english"],
        item["computer"],
    )
    students.append(s)


while True:
    print("\n---student management system---")
    print("1.add student")
    print("2.view students")
    print("3.search student")
    print("4.delete student")
    print("5.show result")
    print("6.update result")
    print("7.exit")

    choice = input("enter choice:")
    if choice =="1":
        name =int(input("enter name:"))

    
        try:
            roll=int(input("enter roll number"))
        except ValueError:
            print("please enter numbers only")

        roll=int(input("enter roll:"))
        duplicate=False
        for st in students:
            if st.roll==roll:
                duplicate=True
                break
        if duplicate:
            print("roll number already exists")



        maths=int(input("enter math marks:"))
        science=int(input("enter science marks:"))
        english=int(input("enter english marks:"))
        computer=int(input("enter computer marks:"))
        
        s = Student(name,roll,maths,science,english ,computer)
        students.append(s)

        data=[]
        for st in students:
         data.append({
            "name":st.name,
            "roll":st.roll,
            "maths":st.maths,
            "scinece":st.science,
            "english":st.english,
            "computer":st.computer
        })

        with open("students.json","w")as file:
            json.dump(data,file,indent=4)
        


            

        

        print("student added!")
    

    elif choice =="2":
       if len(students) ==0:
            print("no students found")

       else:
            for s in students:
             print(s.name,s.roll,s.maths,s.science,s.english,s.computer,)

    elif choice=="3":

     roll=input("enter roll to search:")
     found=False
     for s in students:
        if str(s.roll)==roll:
             print("\nStudentFound:")
             print(s.name,s.roll,s.maths,s.science,s.english,s.computer)
             found=True
             break
     if not found:
              print("Student not found")

    elif choice=="4":

     roll=input("enter roll to delete:")
     found=False
     for s in students:
        if str(s.roll)==roll:
            students.remove(s)
            print("Student delted!")

            found=True
            break
     
     if not found:
             print("student not found")

    elif choice=="5":
     roll=input("enter roll number:")
     found=False
     for s in students:
 
        if str(s.roll)==roll:
                print("\n=====result=====")
                print("name,s.name,roll,s.roll,total,s.total_marks()")
                print("percentage:",s.percentage())
                print("result:",s.result())
                print("grade:",s.grade())
                found=True
                break

     if not found:
                 print("student not found")



    elif choice=="6":
        roll=int(input("enter roll number:"))

        found =False
        for s in students:
            if s.roll==roll:
                s.maths=int(input("enter new maths marks:"))
                s.science=int(input("enter new science marks:"))
                s.english=int(input("enter new english marks:"))
                s.computer=int(input("enter new computer marks:"))

            data=[]

            for st in students:
                data.append({
                    "name":st.namr,
                    "roll":st.roll,
                    "maths":st.maths,
                    "science":st.science,
                    "english":st.english,
                    "computer":st.computer,
                })

            with open("student.json","w")as file:
                json.dump(data,file,indent=4)

                print("student updated")
                found=True
                break
            if not found:
                print("student not found")



            
    elif choice =="7":
          print("exiting...")
          break

    else:
      print("invalid choice")

    