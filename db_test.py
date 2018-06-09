import sqlite3
from employee import employee

conn=sqlite3.connect(":memory:")

c = conn.cursor()
####
c.execute("""CREATE TABLE employees (
       first text,
       last test,
       pay integer
       )""")

emp_1 = employee('John','Doe', 80000)
emp_2 = employee('Jane','Doe', 82000)
print(emp_1.fullname)

c.execute("INSERT INTO employees values (?,?,?)", (emp_1.first, emp_1.last, emp_1.pay))
conn.commit()

c.execute("INSERT INTO employees values (:first,:last,:pay)", {'first':emp_2.first,'last':emp_2.last,'pay':emp_2.pay })
conn.commit()

#c.execute("SELECT * FROM employees")
c.execute("SELECT * FROM employees WHERE last=:last and pay>:pay",{'last':"Doe",'pay':80000})
print(c.fetchall())

conn.commit()
conn.close()
