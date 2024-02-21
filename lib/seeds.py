# seeds.py
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Category, Product, Supplier, Base
from faker import Faker

DATABASE_URL = "sqlite:///./stock_management.db"

engine = create_engine(DATABASE_URL)

Base.metadata.create_all(bind=engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Faker data generation
fake = Faker()

# Function to create a new category
def create_category(name):
    category = Category(name=name)
    session.add(category)
    session.commit()
    print(f"Category '{name}' created successfully.")

# Function to add a new product
def add_product(name, quantity, price, category_names, supplier_name):
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
    print(f"Product '{name}' added successfully.")

# Function to generate random data and add products
def seed_data(num_products=10):
    for _ in range(num_products):
        product_name = fake.word()
        product_quantity = fake.random_int(min=1, max=100)
        product_price = fake.random_int(min=10, max=500)
        category_names = [fake.word() for _ in range(fake.random_int(min=1, max=3))]
        supplier_name = fake.company()

        add_product(product_name, product_quantity, product_price, category_names, supplier_name)

# Function to list all products
def list_products():
    products = session.query(Product).all()
    if not products:
        print("No products found.")
        return
    for product in products:
        print(f"ID: {product.id}, Name: {product.name}, Quantity: {product.quantity}, Price: {product.price}, Supplier: {product.supplier.name}")

# Function to list all categories
def list_categories():
    categories = session.query(Category).all()
    if not categories:
        print("No categories found.")
        return
    for category in categories:
        print(f"ID: {category.id}, Name: {category.name}")

# Function to list all suppliers
def list_suppliers():
    suppliers = session.query(Supplier).all()
    if not suppliers:
        print("No suppliers found.")
        return
    for supplier in suppliers:
        print(f"ID: {supplier.id}, Name: {supplier.name}")

print("Tables present in the database:")
print(Base.metadata.tables.keys())

seed_data(num_products=10)

# All products after seeding
print("\nList of Products after Seeding:")
list_products()

session.close()
