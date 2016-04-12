# We need to create a variable for each class...
math = float(input("What is your grade in Math?"))
english = float(input("What is your grade in English?"))
cs = float(input("What is your grade in Computer Science?"))
science = float(input("What is your grade in Science?"))
socialStudies = float(input("What is your grade in Social Studies?"))
average = (math + english + cs + science + socialStudies)/5

print "Your average is " +  str(average)