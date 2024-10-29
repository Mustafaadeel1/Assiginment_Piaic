# Student Performance Tracker :
# This program will track student performance in a class.
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def calculate_average(self):
        average =  sum(self.score) / len(self.score)
        return average
    def is_passing(self):
        self.score >= 40

class Performancetracker_class(Student):
    def __init__(self):
        self.dict_student = []  

    def add_student(self, student):
        self.dict_student.append(student)  

    
    def calculate_class_average(self):
        try:
            total = 0
            for student in self.dict_student:
                total += student.score
            average = total / len(self.dict_student)
            print("\n----- Class Performance Summary -----")
            print(f"Total class average score: {average:.2f}\n")
        except AttributeError:
            print("Error: A student's score attribute is missing or incorrect.")
        except TypeError:
            print("Error: This peersone is less than Passing criteria This Student is Fail Try Again and work hard .")
        except ZeroDivisionError:
            print("Error: No students in the list to calculate an average.")
    
    def display_student_performance(self):
        for student in self.dict_student:
            print(f"Student name is {student.name}")
            print(f"Student score is {student.score}")
            print("----------Class Avareage----------")
            print(f"Avareage Score :{student.calculate_average():.2f}")

performance = Performancetracker_class()
performance.add_student(Student("Mustafa", [40]))
performance.add_student(Student("Abbas", [90]))
performance.add_student(Student("Moeez", [99]))  
performance.add_student(Student("Malang", [39]))  

performance.display_student_performance()
performance.calculate_class_average()