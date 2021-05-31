class Employee:
    company = "Casio"
    salary = 10000
    salarybonus = 1100

    @property
    def totalSalary(self):
        return self.salary + self.salarybonus

    @totalSalary.setter
    def totalSalary(self, newsalary):
        self.salarybonus = newsalary - self.salary


e = Employee()
print(e.totalSalary)
e.totalSalary = 11500
print(e.salarybonus)
