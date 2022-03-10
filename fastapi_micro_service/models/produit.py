from sqlalchemy import Column, String, TIMESTAMP, Text, text, DECIMAL
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Product(Base):
    __tablename__ = 'products'

    id = Column(BIGINT(20), primary_key=True)
    name = Column(String(255, 'utf8mb4_unicode_ci'), nullable=False, server_default=text("''"))
    title = Column(Text(collation='utf8mb4_unicode_ci'))
    slug = Column(Text(collation='utf8mb4_unicode_ci'))
    best_price = Column(DECIMAL(10, 0), server_default=text("0"))
    brand = Column(BIGINT(20), nullable=False)
    category = Column(BIGINT(20), nullable=False)
    product_details = Column(BIGINT(20), nullable=False)
    images = Column(Text(collation='utf8mb4_unicode_ci'))
    id_parent = Column(BIGINT(20))
    options = Column(String(255, 'utf8mb4_unicode_ci'), nullable=False, server_default=text("'[]'"))
    created_at = Column(TIMESTAMP)

    def __init__(self, name, title, slug, brand, category, product_details, images, id_parent, options, created_at):
        self.name = name
        self.title = title
        self.slug = slug
        self.brand = brand
        self.category = category
        self.product_details = product_details
        self.images = images
        self.id_parent = id_parent
        self.options = options
        self.created_at = created_at

    def __toString__(self):
        print(f"-->id = {self.id} ,slug = {self.slug} <--")

    def __str__(self):
        return f'ID = {self.id} name = {self.name},title = {self.title},brand = {self.brand},category = {self.category},id_parent = {self.id_parent}'

