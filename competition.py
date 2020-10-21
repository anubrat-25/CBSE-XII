#creating a dictionary
n=int(input("Enter no. of students:"))
student={}

for i in range(n):
	name=input("Enter student name:")
	comp=int(input("Enter the no. of competitions won:"))
	student[name]=comp

print(student)