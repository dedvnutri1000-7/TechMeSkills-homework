CREATE TABLE Employees (
    EmployeeID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT,
    Position TEXT,
    Department TEXT,
    Salary REAL
);

INSERT INTO Employees (Name, Position, Department, Salary) VALUES
('John Smith',    'Developer', 'IT',     4500),
('Anna Brown',    'Manager',   'Sales',  6000),
('Michael Green', 'Analyst',   'Finance',5200),
('Laura White',   'Developer', 'IT',     4800),
('David Black',   'Manager',   'HR',     6500);

UPDATE Employees
SET Position = 'Senior Developer', Salary = 5500
WHERE Name = 'John Smith';

ALTER TABLE Employees
ADD HireDate DATE;

UPDATE Employees SET HireDate = '2020-03-15' WHERE Name = 'John Smith';
UPDATE Employees SET HireDate = '2019-07-01' WHERE Name = 'Anna Brown';
UPDATE Employees SET HireDate = '2021-01-10' WHERE Name = 'Michael Green';
UPDATE Employees SET HireDate = '2020-09-05' WHERE Name = 'Laura White';
UPDATE Employees SET HireDate = '2018-12-20' WHERE Name = 'David Black';

SELECT * FROM Employees WHERE Position = 'Manager';

SELECT * FROM Employees WHERE Salary > 5000;

SELECT * FROM Employees WHERE Department = 'Sales';

SELECT AVG(Salary) AS AverageSalary FROM Employees;