# main.py
import os
import sys
from sqlalchemy.orm import sessionmaker
from tabulate import tabulate
from models import Product, Category, Supplier, Base, engine

sys.path.append(os.getcwd())

# CLI functionality for Product, Category, and Supplier
def view_products(session):
    products = session.query(Product).all()
    product_data = [[product.id, product.name, product.quantity, product.price] for product in products]
    print(tabulate(product_data, headers=["ID", "Name", "Quantity", "Price"], tablefmt="fancy_grid"))

def view_categories(session):
    categories = session.query(Category).all()
    category_data = [[category.id, category.name] for category in categories]
    print(tabulate(category_data, headers=["ID", "Name"], tablefmt="fancy_grid"))

def view_suppliers(session):
    suppliers = session.query(Supplier).all()
    supplier_data = [[supplier.id, supplier.name] for supplier in suppliers]
    print(tabulate(supplier_data, headers=["ID", "Name"], tablefmt="fancy_grid"))

def create_product(session):
    name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    quantity = validate_positive_integer(quantity, "Quantity")
    price = int(input("Enter price: "))
    category_names = input("Enter categories (comma-separated): ").split(',')
    supplier_name = input("Enter supplier name: ")

    supplier = session.query(Supplier).filter_by(name=supplier_name).first()
    if not supplier:
        supplier = Supplier(name=supplier_name)
        session.add(supplier)
        session.commit()

    categories = []
    for category_name in category_names:
        category = session.query(Category).filter_by(name=category_name).first()
        if not category:
            category = Category(name=category_name)
            session.add(category)
            session.commit()
        categories.append(category)

    product = Product(
        name=name,
        quantity=quantity,
        price=price,
        categories=categories,
        supplier=supplier
    )
    session.add(product)
    session.commit()
    print("Product created successfully.")

def update_product(session):
    view_products(session)
    product_id = int(input("Enter the ID of the product to update: "))
    product = session.query(Product).get(product_id)
    if product:
        print(f"Updating product with ID {product_id}")
        name = input("Enter new name (press Enter to keep current): ")
        quantity = input("Enter new quantity (press Enter to keep current): ")
        price = input("Enter new price (press Enter to keep current): ")

        if name:
            product.name = name
        if quantity:
            product.quantity = int(quantity)
        if price:
            product.price = int(price)

        session.commit()
        print(f"Product with ID {product_id} updated successfully.")
    else:
        print(f"Product with ID {product_id} not found.")

def delete_product(session):
    view_products(session)
    product_id = int(input("Enter the ID of the product to delete: "))
    product = session.query(Product).get(product_id)
    if product:
        session.delete(product)
        session.commit()
        print(f"Product with ID {product_id} deleted successfully.")
    else:
        print(f"Product with ID {product_id} not found.")

def create_category(session):
    name = input("Enter category name: ")

    category = Category(name=name)
    session.add(category)
    session.commit()
    print("Category created successfully.")

def update_category(session):
    view_categories(session)
    category_id = int(input("Enter the ID of the category to update: "))
    category = session.query(Category).get(category_id)
    if category:
        print(f"Updating category with ID {category_id}")
        name = input("Enter new name (press Enter to keep current): ")

        if name:
            category.name = name

        session.commit()
        print(f"Category with ID {category_id} updated successfully.")
    else:
        print(f"Category with ID {category_id} not found.")

def delete_category(session):
    view_categories(session)
    category_id = int(input("Enter the ID of the category to delete: "))
    category = session.query(Category).get(category_id)
    if category:
        session.delete(category)
        session.commit()
        print(f"Category with ID {category_id} deleted successfully.")
    else:
        print(f"Category with ID {category_id} not found.")

def create_supplier(session):
    name = input("Enter supplier name: ")

    supplier = Supplier(name=name)
    session.add(supplier)
    session.commit()
    print("Supplier created successfully.")

def update_supplier(session):
    view_suppliers(session)
    supplier_id = int(input("Enter the ID of the supplier to update: "))
    supplier = session.query(Supplier).get(supplier_id)
    if supplier:
        print(f"Updating supplier with ID {supplier_id}")
        name = input("Enter new name (press Enter to keep current): ")

        if name:
            supplier.name = name

        session.commit()
        print(f"Supplier with ID {supplier_id} updated successfully.")
    else:
        print(f"Supplier with ID {supplier_id} not found.")

def delete_supplier(session):
    view_suppliers(session)
    supplier_id = int(input("Enter the ID of the supplier to delete: "))
    supplier = session.query(Supplier).get(supplier_id)
    if supplier:
        session.delete(supplier)
        session.commit()
        print(f"Supplier with ID {supplier_id} deleted successfully.")
    else:
        print(f"Supplier with ID {supplier_id} not found.")


def validate_positive_integer(value, field_name):
    try:
        int_value = int(value)
        if int_value <= 0:
            raise ValueError(f"{field_name} must be a positive integer.")
        return int_value
    except ValueError:
        raise ValueError(f"{field_name} must be a valid positive integer.")


def main():
    Base.metadata.create_all(engine)  # Create tables
    Session = sessionmaker(bind=engine)
    session = Session()

    while True:
        print("\n" + "-" * 50)
        print("Welcome to our Stock Management System")
        print("-" * 50)
        print("1. View Products")
        print("2. View Categories")
        print("3. View Suppliers")
        print("4. Create Product")
        print("5. Update Product")
        print("6. Delete Product")
        print("7. Create Category")
        print("8. Update Category")
        print("9. Delete Category")
        print("10. Create Supplier")
        print("11. Update Supplier")
        print("12. Delete Supplier")
        print("13. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            view_products(session)
        elif choice == '2':
            view_categories(session)
        elif choice == '3':
            view_suppliers(session)
        elif choice == '4':
            create_product(session)
        elif choice == '5':
            update_product(session)
        elif choice == '6':
            delete_product(session)
        elif choice == '7':
            create_category(session)
        elif choice == '8':
            update_category(session)
        elif choice == '9':
            delete_category(session)
        elif choice == '10':
            create_supplier(session)
        elif choice == '11':
            update_supplier(session)
        elif choice == '12':
            delete_supplier(session)
        elif choice == '13':
            print("Goodbye, see you soon!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
