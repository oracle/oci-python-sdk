CREATE TABLE Departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(100)
);

CREATE TABLE Jobs (
    job_id INT PRIMARY KEY,
    job_title VARCHAR(100),
    min_salary DECIMAL(10, 2),
    max_salary DECIMAL(10, 2),
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES Departments(department_id)
);

CREATE TABLE Employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    job_id INT,
    hire_date DATE,
    salary DECIMAL(10, 2),
    manager_id INT,
    FOREIGN KEY (job_id) REFERENCES Jobs(job_id),
    FOREIGN KEY (manager_id) REFERENCES Employees(employee_id)
);

CREATE TABLE Job_Postings (
    posting_id INT PRIMARY KEY,
    job_id INT,
    posted_date DATE,
    closing_date DATE,
    status VARCHAR(20),
    FOREIGN KEY (job_id) REFERENCES Jobs(job_id)
);

CREATE TABLE Applications (
    application_id INT PRIMARY KEY,
    posting_id INT,
    applicant_name VARCHAR(100),
    application_date DATE,
    status VARCHAR(20),
    FOREIGN KEY (posting_id) REFERENCES Job_Postings(posting_id)
);

CREATE TABLE Hiring_Processes (
    process_id INT PRIMARY KEY,
    application_id INT,
    interview_date DATE,
    decision VARCHAR(20),
    FOREIGN KEY (application_id) REFERENCES Applications(application_id)
);
