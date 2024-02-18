'''a program that calculate the grade of student based on  their percentage score.
the program should print out the '''

grade = int(input('enter ur grade :'))
print(grade)
if grade >= 90 and grade <= 100:
    print(grade, ' A is ur grade')
elif grade <= 80 and grade > 90:
    print(grade, ' B is ur grade')
elif grade <= 70 and grade > 80:
    print(grade, ' C is ur grade')
elif grade <= 60 and grade > 70:
    print(grade, ' D is ur grade')
else:
    print(grade, ' F is ur grade')

#end
