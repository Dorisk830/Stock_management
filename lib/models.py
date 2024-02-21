from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Boolean

DATABASE_URL = "sqlite:///./stock_management.db"
engine = create_engine(DATABASE_URL)

Base = declarative_base()

# Create tables
Base.metadata.create_all(bind=engine)

# Association table for many-to-many relationship between Product and Category
product_category_association = Table(
    'product_category_association', Base.metadata,
    Column('product_id', Integer, ForeignKey('product.id')),
    Column('category_id', Integer, ForeignKey('category.id'))
)
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    email_verified = Column(Boolean, default=False)
    auth_time = Column(Integer)
    user_id = Column(String, unique=True)
    sign_in_provider = Column(String)
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
