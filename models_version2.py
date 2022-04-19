# coding: utf-8
from sqlalchemy import Column, DECIMAL, ForeignKey, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, LONGTEXT, TINYINT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Brand(Base):
    __tablename__ = 'brands'

    id = Column(BIGINT(20), primary_key=True)
    name = Column(String(255, 'utf8mb4_unicode_ci'), nullable=False)
    description = Column(Text(collation='utf8mb4_unicode_ci'))
    specialite = Column(String(255, 'utf8mb4_unicode_ci'))
    logo = Column(String(255, 'utf8mb4_unicode_ci'))
    click_counts = Column(BIGINT(20), nullable=False, server_default=text("0"))
    view_counts = Column(BIGINT(20), nullable=False, server_default=text("0"))
    search_counts = Column(BIGINT(20), nullable=False, server_default=text("0"))
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)


class Category(Base):
    __tablename__ = 'categories'

    id = Column(BIGINT(20), primary_key=True)
    name = Column(String(255, 'utf8mb4_unicode_ci'), nullable=False)
    description = Column(LONGTEXT, nullable=False)
    id_parent = Column(BIGINT(20))
    title_options = Column(String(255, 'utf8mb4_unicode_ci'), nullable=False, server_default=text("'[]'"))
    Specific_options = Column(String(255, 'utf8mb4_unicode_ci'), nullable=False, server_default=text("'[]'"))
    click_counts = Column('click-counts', BIGINT(20), nullable=False, server_default=text("0"))
    view_counts = Column('view-counts', BIGINT(20), nullable=False, server_default=text("0"))
    search_counts = Column('search-counts', BIGINT(20), nullable=False, server_default=text("0"))
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)


class FailedJob(Base):
    __tablename__ = 'failed_jobs'

    id = Column(BIGINT(20), primary_key=True)
    uuid = Column(String(255, 'utf8mb4_unicode_ci'), nullable=False, unique=True)
    connection = Column(Text(collation='utf8mb4_unicode_ci'), nullable=False)
    queue = Column(Text(collation='utf8mb4_unicode_ci'), nullable=False)
    payload = Column(LONGTEXT, nullable=False)
    exception = Column(LONGTEXT, nullable=False)
    failed_at = Column(TIMESTAMP, nullable=False, server_default=text("current_timestamp()"))


class Job(Base):
    __tablename__ = 'jobs'

    id = Column(BIGINT(20), primary_key=True)
    queue = Column(String(255, 'utf8mb4_unicode_ci'), nullable=False, index=True)
    payload = Column(LONGTEXT, nullable=False)
    attempts = Column(TINYINT(3), nullable=False)
    reserved_at = Column(INTEGER(10))
    available_at = Column(INTEGER(10), nullable=False)
    created_at = Column(INTEGER(10), nullable=False)


class Migration(Base):
    __tablename__ = 'migrations'

    id = Column(INTEGER(10), primary_key=True)
    migration = Column(String(255, 'utf8mb4_unicode_ci'), nullable=False)
    batch = Column(INTEGER(11), nullable=False)


class Option(Base):
    __tablename__ = 'options'

    id = Column(BIGINT(20), primary_key=True)
    name = Column(String(255, 'utf8mb4_unicode_ci'), nullable=False)
    value = Column(String(255, 'utf8mb4_unicode_ci'))
    unit = Column(String(255, 'utf8mb4_unicode_ci'))
    id_parent = Column(ForeignKey('options.id', ondelete='CASCADE'), index=True)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

    parent = relationship('Option', remote_side=[id])


t_password_resets = Table(
    'password_resets', metadata,
    Column('email', String(255, 'utf8mb4_unicode_ci'), nullable=False, index=True),
    Column('token', String(255, 'utf8mb4_unicode_ci'), nullable=False),
    Column('created_at', TIMESTAMP)
)


class PriceHistory(Base):
    __tablename__ = 'price_histories'

    id = Column(BIGINT(20), primary_key=True)
    id_product = Column(BIGINT(20), nullable=False)
    average = Column(DECIMAL(8, 2), nullable=False)
    best_price = Column(DECIMAL(8, 2), nullable=False)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)


class ProductDetail(Base):
    __tablename__ = 'product_details'

    id = Column(BIGINT(20), primary_key=True)
    rating_value = Column(DECIMAL(8, 1))
    rating_count = Column(INTEGER(11))
    short_description = Column(LONGTEXT)
    description = Column(LONGTEXT)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)


class Product(Base):
    __tablename__ = 'products'

    id = Column(BIGINT(20), primary_key=True)
    name = Column(String(255, 'utf8mb4_unicode_ci'), nullable=False)
    title = Column(Text(collation='utf8mb4_unicode_ci'), nullable=False)
    slug = Column(Text(collation='utf8mb4_unicode_ci'), nullable=False)
    best_price = Column(DECIMAL(8, 2), nullable=False)
    id_parent = Column(BIGINT(20))
    click_counts = Column(BIGINT(20), nullable=False, server_default=text("0"))
    view_counts = Column(BIGINT(20), nullable=False, server_default=text("0"))
    search_counts = Column(BIGINT(20), nullable=False, server_default=text("0"))
    options = Column(String(255, 'utf8mb4_unicode_ci'), nullable=False, server_default=text("'[]'"))
    choix_equipe = Column(TINYINT(1), nullable=False, server_default=text("0"))
    status = Column(TINYINT(1), nullable=False, server_default=text("0"))
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)
    brand = Column(BIGINT(20))
    category = Column(BIGINT(20))
    product_details = Column(BIGINT(20))
    images = Column(Text(collation='utf8mb4_unicode_ci'))


class Store(Base):
    __tablename__ = 'stores'

    id = Column(BIGINT(20), primary_key=True)
    name = Column(String(255, 'utf8mb4_unicode_ci'), nullable=False)
    description = Column(Text(collation='utf8mb4_unicode_ci'))
    specialite = Column(String(255, 'utf8mb4_unicode_ci'), server_default=text("'[]'"))
    phone = Column(String(255, 'utf8mb4_unicode_ci'))
    email = Column(String(255, 'utf8mb4_unicode_ci'))
    adress = Column(String(255, 'utf8mb4_unicode_ci'))
    site_officiel = Column(String(255, 'utf8mb4_unicode_ci'))
    logo = Column(Text(collation='utf8mb4_unicode_ci'))
    click_counts = Column('click-counts', BIGINT(20), nullable=False, server_default=text("0"))
    view_counts = Column('view-counts', BIGINT(20), nullable=False, server_default=text("0"))
    search_counts = Column('search-counts', BIGINT(20), nullable=False, server_default=text("0"))
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)


class User(Base):
    __tablename__ = 'users'

    id = Column(BIGINT(20), primary_key=True)
    name = Column(String(255, 'utf8mb4_unicode_ci'), nullable=False)
    email = Column(String(255, 'utf8mb4_unicode_ci'), nullable=False, unique=True)
    email_verified_at = Column(TIMESTAMP)
    password = Column(String(255, 'utf8mb4_unicode_ci'), nullable=False)
    remember_token = Column(String(100, 'utf8mb4_unicode_ci'))
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)


class ProductStore(Base):
    __tablename__ = 'product__stores'

    id = Column(BIGINT(20), primary_key=True)
    id_product = Column(ForeignKey('products.id'), nullable=False, index=True)
    store = Column(ForeignKey('stores.id'), nullable=False, index=True)
    title = Column(Text(collation='utf8mb4_unicode_ci'), nullable=False)
    price = Column(DECIMAL(8, 2), nullable=False)
    link = Column(Text(collation='utf8mb4_unicode_ci'), nullable=False)
    click_counts = Column('click-counts', BIGINT(20))
    view_counts = Column('view-counts', BIGINT(20))
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

    product = relationship('Product')
    store1 = relationship('Store')
