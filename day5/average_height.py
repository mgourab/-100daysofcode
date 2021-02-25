# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
#print(student_heights)

#Write your code below this row 👇

no_of_students = 0
sum_of_heights = 0

# count the sum of all the items in the list and increase the counter
for height in student_heights:
    sum_of_heights += height
    no_of_students += 1

# print the number of students and sum of the heights
print(sum_of_heights, no_of_students)

# do the average height
avg_height = sum_of_heights / no_of_students
print(avg_height)


