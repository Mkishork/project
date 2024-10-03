# Human Resource Management System (HRMS)

This HRMS provides functionality to manage employee data, track attendance, and retrieve employee records through various API endpoints and web pages.

## Endpoints

### index(request)
- **Description**: Renders the index page for the HRMS.
- **Template**: Employee_management/index.html
- **Usage**: Displays the main interface for the system.

---

### add(request)
- **Description**: Adds a new employee using the provided name, destination, and date from the GET request.
- **Templates**:
  - On success: Renders index.html
  - On failure: Renders success.html
- **Usage**: Add an employee by sending a GET request with necessary fields.

---

### get_data(request)
- **Description**: Retrieves all employee data as a JSON response.
- **Response**: A list of employees in JSON format.
- **Usage**: To fetch all employee records.

---

### get_specific_employee(request, id)
- **Description**: Retrieves the data of a specific employee by their ID.
- **Response**: Employee details in JSON format.
- **Usage**: To fetch information about a specific employee by passing their id.

---

### mark_attendance(request, id, status)
- **Description**: Marks attendance for a specific employee, with status either as 'Present' or 'Absent'.
- **Template**: Renders success.html after successfully marking attendance.
- **Usage**: Mark the attendance of an employee by sending their id and attendance status.

---

### get_attendance(request)
- **Description**: Retrieves the attendance records of all employees.
- **Response**: A list of attendance records in JSON format.
- **Usage**: To fetch attendance data for all employees.

---

### get_specificdep_attendance(request, dep_name)
- **Description**: Retrieves attendance records for employees in a specific department.
- **Response**: Department-specific attendance records in JSON format.
- **Usage**: Fetch attendance records filtered by the department name (dep_name).

---

## Templates Used
- **index.html**: Displays the main HRMS interface.
- **success.html**: Shows success/failure messages for certain actions like adding employees or marking attendance.

---

## Dependencies
- Django framework (version 3.x or higher)
- Python 3.x
- JSON for API responses

---

## Setup and Installation

1. Create a folder.
2. Create a virtual environment (venv).
3. Copy the code into the folder.
4. Activate the virtual environment.
5. Install Django.
6. Create a table in the database named `empol`.
7. Go to the project directory and run the following commands:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
