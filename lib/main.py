# main.py
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from faker import Faker

Base = declarative_base()

# Association table for many-to-many relationship between Product and Category
product_category_association = Table(
    'product_category_association', Base.metadata,
    Column('product_id', Integer, ForeignKey('product.id')),
    Column('category_id', Integer, ForeignKey('category.id'))
)

class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    products = relationship("Product", secondary=product_category_association, back_populates="categories", overlaps="categories")

class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    quantity = Column(Integer)
    price = Column(Integer)
    categories = relationship("Category", secondary=product_category_association, back_populates="products", overlaps="products")
    supplier_id = Column(Integer, ForeignKey('supplier.id'))
    supplier = relationship("Supplier", back_populates="products")

class Supplier(Base):
    __tablename__ = 'supplier'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    products = relationship("Product", back_populates="supplier")

# Database URL format: dialect+driver://username:password@host:port/database
DATABASE_URL = "sqlite:///./stock_management.db"
engine = create_engine(DATABASE_URL)

# Create tables
Base.metadata.create_all(bind=engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Faker instance for data generation
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

# Function to update product quantity
def update_product_quantity(product_id, new_quantity):
    product = session.query(Product).get(product_id)
    if product:
        product.quantity = new_quantity
        session.commit()
        print(f"Product with ID {product_id} quantity updated successfully.")
    else:
        print(f"Product with ID {product_id} not found.")

# Example usage of functions
if __name__ == "__main__":
    # Example usage of functions
    create_category("Electronics")
    add_product("Laptop", 10, 800, ["Electronics"], "TechSupplier")
    list_products()

    # Add more products
    add_product("Smartphone", 15, 600, ["Electronics"], "TechSupplier")
    add_product("Headphones", 20, 100, ["Electronics"], "AudioSupplier")
    add_product("T-Shirt", 30, 25, ["Clothing"], "FashionSupplier")
    add_product("Jeans", 25, 50, ["Clothing"], "FashionSupplier")
    add_product("Watch", 10, 150, ["Accessories"], "TimeSupplier")
    add_product("Sunglasses", 15, 75, ["Accessories"], "FashionSupplier")
    add_product("Desk Chair", 5, 200, ["Furniture"], "OfficeSupplier")
    add_product("Coffee Table", 8, 120, ["Furniture"], "HomeSupplier")
    add_product("Gaming Laptop", 12, 1200, ["Electronics", "Gaming"], "TechSupplier")
    add_product("Gaming Mouse", 18, 80, ["Electronics", "Gaming"], "TechSupplier")

    # List all products, categories, and suppliers
    list_products()
    list_categories()
    list_suppliers()

    # Example of updating product quantity
    update_product_quantity(1, 15)

    # Close the session
    session.close()
