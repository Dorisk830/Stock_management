from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship


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
