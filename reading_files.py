
employee_file = open("employees.txt", "r")
# print(employee_file.readlines())

for line in employee_file.readlines():
    print(line)

employee_file.close()
