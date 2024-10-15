import StudentClass as s


student1 = s.student('892733264', 'Sanskar Tomar', '11/18/2003', 'Jr')

student1.calc_age()
student1.get_registration()



print(f"Because the student is a {student1.get_class()}")


print(f"the age of the student is {student1.get_age()}")