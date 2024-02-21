#### Stock Management System

This project is a stock management system developed in Python using SQLAlchemy and Alembic for database management and migrations.

It is designed to help businesses keep track of their product inventory. It allows users to add products, list available products, and update product quantities. The project uses SQLAlchemy for object-relational mapping and Alembic for database migrations.

#### Features

- Add new products with details such as name, quantity, price, categories, and supplier.
- List all available products.
- Update the quantity of existing products.
- Manage categories and suppliers.
- Support for many-to-many relationships between products and categories.
- Database migrations using Alembic.

#### Getting Started

### Prerequisites

- Python3
- SQLite (or another supported database)

### Installation

1. Clone the repository:
   git clone https://github.com/Dorisk830/Stock_management.git
   cd stock-management


2. Install dependencies then run the application
    pipenv install
    pip install sqlalchemy

3. Database Migrations
    alembic revision -m "Description of migration"
    alembic upgrade head

#### Functionality

1. View Products, Categories, and Suppliers
View a list of all products, categories, and suppliers.
2. Create Product, Category, and Supplier
Add new products, categories, and suppliers to the system.
3. Update Product, Category, and Supplier
Modify existing products, categories, and suppliers.
4. Delete Product, Category, and Supplier
Remove products, categories, and suppliers from the system.
5. Exit
Exit the Product Management System.

### Usage

1.	Run python main.py to start the system.

2.	Choose options from the menu to perform various actions.

3.	Follow the prompts to input details for creating, updating, or deleting entities.

4.	Exit the system when done.

### Examples
•	View Products:

•	Create Product:

•	Update Product:

•	Delete Product
:

### Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.
