# Student Performance Tracker

This program tracks student performance in a class by calculating individual averages and the overall class average.

## Overview

The **Student Performance Tracker** program allows teachers to manage student performance by recording scores in multiple subjects and calculating averages. Each student's score is assessed to determine if they pass based on an average score.

## Classes

### Student Class

The `Student` class represents an individual student.

#### Attributes

- **`name`**: The name of the student (type: `str`).
- **`score`**: A list containing the scores of the student in different subjects (type: `list`).

#### Methods

- **`calculate_average()`**: Calculates the average score of the student based on their scores.
  
  ```python
  def calculate_average(self):
      average = sum(self.score) / len(self.score)
      return average

**is_passing()**: 

Checks if the student's average score is at least 40.
```python
def is_passing(self):
    return self.calculate_average() >= 40
```
# PerformanceTracker Class

The PerformanceTracker class manages multiple Student `objects`.

### Attributes
`dict_student`: 
    
* A list that stores Student objects.
### Methods
`add_student(student)`:

* Adds a new student to the tracker.
```python
def add_student(self, student):
    self.dict_student.append(student)
```

* `Calculate_class_average():` Calculates and prints the average score for the entire class.
```python
def calculate_class_average(self):
    try:
        total = 0
        for student in self.dict_student:
            total += student.calculate_average()  # Use calculate_average
        average = total / len(self.dict_student)
        print("\n----- Class Performance Summary -----")
        print(f"Total class average score: {average:.2f}\n")
    except AttributeError:
        print("Error: A student's score attribute is missing or incorrect.")
    except TypeError:
        print("Error: Non-numeric score detected.")
    except ZeroDivisionError:
        print("Error: No students in the list to calculate an average.")
```
* `display_student_performance():` Displays each student's name, scores, and average score.

```python
def display_student_performance(self):
    for student in self.dict_student:
        print(f"Student name is {student.name}")
        print(f"Student score is {student.score}")
        print(f"Average Score: {student.calculate_average():.2f}")
```
# Example Usage
* Here’s how you can use the PerformanceTracker class to manage student performance:
```python
# Create an instance of PerformanceTracker
performance = PerformanceTracker()

# Add students
performance.add_student(Student("Mustafa",[40]))
performance.add_student(Student("Abbas", [90]))
performance.add_student(Student("Moeez",[99]))  
performance.add_student(Student("Malang",[39]))  

# Display student performance and calculate class average
performance.display_student_performance()
performance.calculate_class_average()
```
# Output Example
* When you run the example code, you can expect output similar to the following:

```python
Student name is Mustafa
Student score is [40]
Average Score: 40.00
Student name is Abbas
Student score is [90]
Average Score: 90.00
Student name is Moeez
Student score is [99]
Average Score: 99.00
Student name is Malang
Student score is [39]
Average Score: 39.00
