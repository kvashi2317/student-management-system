class Student:
    def __init__(self,name,roll,maths,science,english,computer):
        self.name=name
        self.roll=roll
        self.maths=maths
        self.science=science
        self.english=english
        self.computer=computer

                 



    def total_marks(self):
     return self.maths+self.science+self.english+self.computer

    def percentage(self):
     return self.total_marks()/4

    def result(self):
      if self.maths<40 or self.science<40 or self.english<40 or self.computer<40:
        return "Fail"
      return "pass"



    def grade(self):
     per=self.percentage()

     if per>=90:
       return "A"
     elif per>=75:
        return"B"
     elif per>=60:
        return "C"
     elif per>=40:
        return "D"
     else:
        return"F"



    

