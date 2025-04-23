import pickle
class Employee:
    def __init__(self, empcode, empname, date_of_joining, salary):
        self.empcode = empcode
        self.empname = empname
        self.date_of_joining = date_of_joining
        self.salary = salary

    def display(self):
        print(f"Employee Code: {self.empcode}")
        print(f"Employee Name: {self.empname}")
        print(f"Date of Joining: {self.date_of_joining}")
        print(f"Salary: {self.salary}")

emp = Employee("E101", "Alice", "2022-05-10", 75000)

with open("employee_data.pkl", "wb") as file:
    pickle.dump(emp, file)
    print("Employee data serialized successfully.")

with open("employee_data.pkl", "rb") as file:
    loaded_emp = pickle.load(file)
    print("\nDeserialized Employee data:")
    loaded_emp.display()