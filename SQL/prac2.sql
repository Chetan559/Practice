-- Create the UniversityDB database
CREATE DATABASE UniversityDB;
GO

-- Use the UniversityDB database
USE UniversityDB;
GO

-- Create the Students table
CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    DateOfBirth DATE
);

-- Create Enrollments table
CREATE TABLE Enrollments (
    enrollmentid INT PRIMARY KEY,
    studentid INT,
    courseid INT,
    grade FLOAT,
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);
-- Create the Courses table
CREATE TABLE Courses (
    CourseID INT PRIMARY KEY,
    CourseName VARCHAR(50),
    Credits INT,
    TeacherID INT,
    FOREIGN KEY (TeacherID) REFERENCES Teachers(TeacherID)
);

-- Create the Teachers table
CREATE TABLE Teachers (
    TeacherID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50)
);

-- Insert 10 tuples into the Students table
INSERT INTO Students (StudentID, FirstName, LastName, DateOfBirth)
VALUES
    (1, 'John', 'Doe', '2000-05-15'),
    (2, 'Jane', 'Smith', '1999-08-22'),
    (3, 'Bob', 'Johnson', '2001-03-10'),
    (4, 'Alice', 'Williams', '2002-11-05'),
    (5, 'Charlie', 'Brown', '2003-07-18'),
    (6, 'Eva', 'Davis', '2000-12-30'),
    (7, 'Mike', 'Miller', '2002-06-25'),
    (8, 'Sophia', 'Clark', '2001-09-12'),
    (9, 'Daniel', 'Taylor', '1999-04-05'),
    (10, 'Olivia', 'Moore', '2003-02-18');

-- Insert 5 tuples into the Teachers table
INSERT INTO Teachers (TeacherID, FirstName, LastName)
VALUES
    (101, 'Professor', 'Johnson'),
    (102, 'Dr.', 'Smith'),
    (103, 'Mrs.', 'Williams'),
    (104, 'Mr.', 'Brown'),
    (105, 'Ms.', 'Clark');

-- Insert 5 tuples into the Courses table
INSERT INTO Courses (CourseID, CourseName, Credits, TeacherID)
VALUES
    (1001, 'Mathematics', 4, 101),
    (1002, 'English', 3, 102),
    (1003, 'Computer Science', 4, 103),
    (1004, 'Physics', 3, 104),
    (1005, 'History', 3, 105);

-- Insert 10 tuples into the Enrollments table

INSERT INTO Enrollments VALUES (1, 1, 101, 90);
INSERT INTO Enrollments VALUES (2, 1, 102, 85);
INSERT INTO Enrollments VALUES (3, 2, 101, 88);
INSERT INTO Enrollments VALUES (4, 2, 103, 92);
INSERT INTO Enrollments VALUES (5, 3, 102, 78);


-- questios 
-- Retrieve the names of students who have enrolled in more than two courses.
-- Find the course with the highest average grade.
-- List the students who have not enrolled in any course.
-- Find the total number of courses with at least one student enrolled.
-- Retrieve the names of students who have the same age as 'Alice'.
-- Find the course with the lowest average grade among courses with more than three students enrolled.
-- List the students who have the highest grade in the 'English' course.
-- Find the courses with the same number of credits as the 'Mathematics' course.
-- Retrieve the names of students who have enrolled in all available courses.
-- Find the average age of students who have enrolled in the 'Computer Science' course.


-- 1
select s.firstname 
from students as s
left join enrollments as e on s.studentid = e.studentid
left join courses as c on e.courseid = c.courseid
group by c.coursename
having count(c.coursename) >2

--2
