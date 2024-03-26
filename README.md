# SIS_SBSA


# Sainath Bahuuddeshiya Sanstha - Student Information System

## Overview
This project is a Student Information System built using Python's Tkinter library for the GUI and MySQL for database management. It provides functionalities to manage student records including registration, updating, deletion, and searching.

## Technologies Used
- **Python**: The primary programming language used for application logic and GUI development.
- **Tkinter**: A Python library for creating GUI applications. Tkinter is used here to design the user interface.
- **MySQL**: An open-source relational database management system used for storing and managing student data.
- **Pymysql**: A Python library for connecting Python programs to the MySQL database.

## Project Structure
- **main.py**: This file contains the main application logic and entry point for the program. It initializes the Tkinter GUI and handles user interactions.
- **LoginPage**: Represents the login page of the application where users can enter their credentials.
- **Window2**: Represents the main window of the application where students' data can be managed.
- **database.py**: Contains functions for database interactions such as fetching, updating, deleting, and inserting student records.
- **config.py**: Stores configuration variables such as database credentials.
- **requirements.txt**: Lists all Python dependencies required for the project.

## Features
1. **Login Page**: Users can log in using their credentials to access the student information system.
2. **Data Management**: Provides functionalities for adding, updating, deleting, and searching student records.
3. **GUI Interface**: Tkinter-based graphical user interface for easy navigation and interaction.
4. **Database Integration**: Utilizes MySQL database for storing and managing student data securely.
5. **Data Validation**: Ensures data integrity by validating user inputs before interacting with the database.

## Usage
1. Clone the repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Update the `config.py` file with your MySQL database credentials.
4. Run `main.py` to launch the application.
5. Log in using the provided credentials (default: username: Rishabh, password: 1234).
6. Navigate through the application to manage student records.

## Future Enhancements
- Implement user authentication and authorization for secure access to the system.
- Add support for more advanced search functionalities such as filtering and sorting.
- Enhance the GUI design for improved user experience.
- Implement data validation for user inputs to ensure data consistency and integrity.

## Conclusion
This project demonstrates the development of a student information system using Python's Tkinter library for the GUI and MySQL for database management. With features for data management and user-friendly interface, it provides an efficient solution for managing student records.

