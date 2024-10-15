import EmployeeClass as e
import PayrollDeductionClass as p

emp1 = e.Employee('Jimmy Smith', 58475, 'Information Systems', 'Developer', 6800.000)
deduction1 = p.Payroll('food court', '8/14/2022', 22.50, 39119)
deduction2 = p.Payroll('gift contribution', '8/12/2022', 25.00, 58475)
deduction3 = p.Payroll('food court', '8/17/2022', 15.25, 21547)
deduction4 = p.Payroll('vending machine', '8/22/2022', 3.00, 58475)
deduction5 = p.Payroll('vending machine', '8/05/2022', 2.75, 58475)
deduction_list = [deduction1, deduction2, deduction3, deduction4, deduction5]


print(f"**Employee Pay**")
print(f"Name: {emp1.get_name()}")
print(f"ID Number: {emp1.get_id()}")
print(f"Department: {emp1.get_department()}")
print(f"Gross Pay: ${emp1.get_salary():.2f}")

charges = 0

for deduction in deduction_list:
    if deduction.get_id() == int(emp1.get_id()):
        charge = deduction.get_charge()
        charges += charge

net_pay = emp1.get_salary() - charges

print(f"Net Pay: ${net_pay:.2f}")


