work_hours = [('abby', 200),('Billy',400),('Cassie', 800)]
    
def employee_check(work_hours):
    
    current_max =0
    employee_of_month = ''
    for employee, hours in work_hours:
        if hours >current_max:
            current_max = hours
            employee_of_month = employee
    
    #return
    return (employee_of_month,current_max)
result =employee_check(work_hours)
print(result)