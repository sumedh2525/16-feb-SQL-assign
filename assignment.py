#Q1. What is a database? Differentiate between SQL and NoSQL databases.
# Ans:
#SQL databases use a structured query language (SQL) to store and retrieve data. 
# SQL is a powerful language that allows users to create, update, delete, and query data in a database. SQL databases are typically used for applications that require complex queries and transaction management.

#NoSQL databases do not use SQL. Instead, they store data in a variety of formats, including key-value pairs, documents, and graphs. 
# NoSQL databases are typically used for applications that require high performance and scalability, such as web applications and mobile apps.






#Q2. What is DDL? Explain why CREATE, DROP, ALTER, and TRUNCATE 
# are used with an example.
# CREATE:
CREATE TABLE  workers(ID INT , Name VARCHAR(70) , Age INT , Salary DECIMAL(10,2));

# DROP:
DROP TABLE Customers;

ALTER TABLE workers
ADD COLUMNS Department VARCHAR(70);

TRUNCATE TABLE Orders;

#Q3. What is DML? Explain INSERT, UPDATE, and DELETE with an example.
INSERT TO Customers (CustomerID , CustomerName,Email)
VALUES (1, 'Sudh','sudhpwskills@gmail.com');
UPDATE workers
SET Salary = Salary*1.1
WHERE Department = 'sales';
DELETE FROM Orders
WHERE OrderDate < '2022-01-01';



#Q4. What is DQL? Explain SELECT with an example.
SELECT column_list
FROM table_name;
SELECT Name, Age
FROM Customers;
WHERE Age > 18;


#Q5. Explain Primary Key and Foreign Key.

#A primary key is a column or combination of columns that uniquely identifies each row in a table.
#  A foreign key is a column or combination of columns that references the primary key of another table


#Q6. Write a python code to connect MySQL to python. Explain the cursor() and execute() method.

import mysql.connector
# create a connection object
connection = mysql.connector.connect(
    host = "localhost"
    user = "root"
    password = "password"
    database = "mydatabase"
)

cursor = connection.cursor()
cursor.execute("SELECT * FROM customers")
results = cursors.fetchall()
for row in results:
    print(row)
connection.close()


#Q7. Give the order of execution of SQL clauses in an SQL query.
#FROM:
#The FROM clause specifies the table or tables from which the data is retrieved. It identifies the source tables for the query.

#WHERE:
#The WHERE clause is used to filter rows based on specified conditions. It allows you to define criteria to restrict the result set based on column values.

#GROUP BY:
#The GROUP BY clause is used to group rows that have the same values in specified columns. It is often used in combination with aggregate functions like SUM, COUNT, AVG, etc.

#HAVING:
#The HAVING clause is used to filter the grouped rows based on specified conditions. It allows you to define criteria to restrict the result set after the GROUP BY clause has been applied.

#SELECT:
#The SELECT clause specifies the columns to be retrieved from the table(s). It defines the projection of the data to be returned in the result set.

#ORDER BY:
#The ORDER BY clause is used to sort the result set based on specified columns. It allows you to sort the data in ascending or descending order.

#LIMIT/OFFSET:
#The LIMIT/OFFSET clause is used to restrict the number of rows returned in the result set. It is often used for pagination or to limit the number of results




