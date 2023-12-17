-- Creating Departments Table
CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY,
    DepartmentName VARCHAR(100)
);

-- Creating Courses Table
CREATE TABLE Courses (
    CourseID INT PRIMARY KEY,
    CourseName VARCHAR(100),
    DepartmentID INT,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);

-- Creating Students Table
CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    Name VARCHAR(100),
    Age INT,
    DepartmentID INT,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);

-- Creating Enrollments Table
CREATE TABLE Enrollments (
    EnrollmentID INT PRIMARY KEY,
    StudentID INT,
    CourseID INT,
    Grade VARCHAR(2),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);


--insert values
-- Inserting data into Departments
INSERT INTO Departments (DepartmentID, DepartmentName)
VALUES
    (1, 'Computer Science'),
    (2, 'Mathematics'),
    (3, 'Physics');

-- Inserting data into Courses
INSERT INTO Courses (CourseID, CourseName, DepartmentID)
VALUES
    (101, 'Introduction to Programming', 1),
    (102, 'Calculus I', 2),
    (103, 'Mechanics', 3);

-- Inserting data into Students
INSERT INTO Students (StudentID, Name, Age, DepartmentID)
VALUES
    (1001, 'Alice', 20, 1),
    (1002, 'Bob', 22, 2),
    (1003, 'Charlie', 21, 3);

-- Inserting data into Enrollments
INSERT INTO Enrollments (EnrollmentID, StudentID, CourseID, Grade)
VALUES
    (5001, 1001, 101, 'A'),
    (5002, 1002, 102, 'B'),
    (5003, 1003, 103, 'A-');
-- Inserting more data into Departments
INSERT INTO Departments (DepartmentID, DepartmentName)
VALUES
    (4, 'Biology'),
    (5, 'History'),
    (6, 'Engineering');

-- Inserting more data into Courses
INSERT INTO Courses (CourseID, CourseName, DepartmentID)
VALUES
    (104, 'Genetics', 4),
    (105, 'World History', 5),
    (106, 'Mechanical Engineering', 6);

-- Inserting more data into Students
INSERT INTO Students (StudentID, Name, Age, DepartmentID)
VALUES
    (1004, 'David', 23, 4),
    (1005, 'Emma', 19, 5),
    (1006, 'Frank', 20, 6);

-- Inserting more data into Enrollments
INSERT INTO Enrollments (EnrollmentID, StudentID, CourseID, Grade)
VALUES
    (5004, 1004, 104, 'B+'),
    (5005, 1005, 105, 'A'),
    (5006, 1006, 106, 'B-');




--questions and  answersss

--Find the department(s) with the highest average grade obtained by students in their courses.

select d.departmentname, AVG(CAST(e.Grade AS DECIMAL)) AS Grade
from departments as d
inner join courses as c on d.departmentid = c.departmentid
inner join enrollments as e on c.courseid = e.courseid
group by departmentname
order by grade desc


--List the names of students who have not enrolled in any course in the 'Computer Science' department.
SELECT Name 
FROM Students AS s
WHERE NOT EXISTS (
    SELECT * 
    FROM Enrollments AS e 
    JOIN Courses AS c ON e.CourseID = c.CourseID 
    WHERE e.StudentID = s.StudentID AND c.DepartmentID = 1
);


--Simulate a scenario where a student's age is updated. However, ensure that if the student is enrolled in a course, their age cannot be reduced below 18. Implement this update operation as part of a transaction.
--Identify the courses in the 'Engineering' department where the average grade is higher than the overall average grade across all departments.
--Find the students who have enrolled in courses from both the 'Mathematics' and 'Physics' departments.
--Create a view that lists the total number of enrollments per course and use it to identify the courses with the highest number of enrollments.