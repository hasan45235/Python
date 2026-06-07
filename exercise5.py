
def func():

  marks = {"Math": 10, "Physics": 20, "Chemistry": 0,}
  obtained = 0
  total = 300

  grade = ""
  for subject in marks:
    marks[subject] = int(input(f"Enter your {subject} marks: "))


  for  keys in marks:
    obtained += marks[keys]

  percentage = (obtained / total) * 100

  if percentage >= 90:
    grade = "A"
  elif 90 > percentage >= 80:
    grade = "B"
  elif 80 > percentage >= 70:
    grade = "C"
  elif 70 > percentage >= 60:
    grade = "D"
  elif 60 > percentage >= 40:
    grade = "E"
  else:
    grade = "F"
  print(f"The Marks Obtained: {obtained} and Percentage: {percentage}% while Grade: {grade}")

func()
