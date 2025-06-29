# RESTFUL-API-DEVELOPMENT

**COMPANY**= CODTECH IT SOLUTIONS

**NAME**= VIYOM PATHAK

**INTERN ID**= CT04DF2028

**DOMAIN**= SOFTWARE DEVELOPMENT

**DURATION**= 4 WEEKS

**MENTOR NAME**= NEELA SANTOSH  

# DESCRIPTION 

Inventory API Project
Welcome to the Inventory API project! This GitHub repository hosts a lightweight RESTful API designed for managing an inventory system, built using Python and the Flask web framework. The API implements CRUD (Create, Read, Update, Delete) operations, making it an excellent resource for developers learning API development or building scalable inventory solutions. Whether you're a beginner with Visual Studio Code or an experienced coder, this project offers a solid foundation to explore REST principles and extend functionality.

Project Overview
The Inventory API allows users to manage items in a virtual inventory. It features five core endpoints:

POST /items: Add a new item with a name and quantity.
GET /items: Retrieve a list of all items.
GET /items/<id>: Fetch details of a specific item by ID.
PUT /items/<id>: Update an existing item’s details.
DELETE /items/<id>: Remove an item from the inventory.
Currently, the API uses an in-memory list for storage, simulating a database. This simplifies the initial setup but can be enhanced with a persistent database like SQLite or PostgreSQL for real-world applications. The project includes a basic README.md with API documentation, making it easy to understand and contribute to.

Getting Started
To run the API locally, you need Python and Flask installed. Follow these steps:

Clone the repository: git clone <repository-url>.
Navigate to the project folder: cd inventory_api.
Install Flask: pip install flask.
Run the application: python app.py (or python3 app.py depending on your system).
Verify the server is running at http://127.0.0.1:5000.
Test the endpoints using tools like the VS Code REST Client extension, Postman, or a Chrome browser with a JSON formatter extension. For example, send a POST request with {"name": "Book", "quantity": 10} to add an item, then use GET to view the list.

Features and Benefits
This project is ideal for educational purposes, demonstrating RESTful design, HTTP methods, and JSON handling. The debug mode in Flask provides real-time feedback, aiding troubleshooting. The code is modular, allowing you to add validation, authentication, or a database with minimal effort. It’s also a starting point for building larger applications, such as e-commerce backends or warehouse management systems.

Potential Enhancements
Database Integration: Replace the in-memory list with SQLite or MongoDB for persistence.
Input Validation: Add checks for required fields and data types.
Authentication: Implement API keys or JWT for secure access.
Deployment: Host on platforms like Heroku or AWS for public use.

![Image](https://github.com/user-attachments/assets/fa7107e1-e00b-41c5-81f1-b00168a5658a)
