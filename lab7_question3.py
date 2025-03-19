employees = [
    {"dept_no": 1, "roll_no": 101, "salary": 50000},
    {"dept_no": 1, "roll_no": 102, "salary": 60000},
    {"dept_no": 2, "roll_no": 103, "salary": 55000},
    {"dept_no": 2, "roll_no": 104, "salary": 70000},
    {"dept_no": 1, "roll_no": 105, "salary": 45000},
    {"dept_no": 3, "roll_no": 106, "salary": 65000},
    {"dept_no": 3, "roll_no": 107, "salary": 62000}
]

dept_salaries = {}
for emp in employees:
    dept = emp["dept_no"]
    salary = emp["salary"]
    if dept not in dept_salaries:
        dept_salaries[dept] = []
    dept_salaries[dept].append(salary)

dept_min_max = {dept: {"min": min(salaries), "max": max(salaries)} for dept, salaries in dept_salaries.items()}

print(dept_min_max)