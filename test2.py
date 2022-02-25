# coding: utf-8
from sqlalchemy import CHAR, Column, DECIMAL, DateTime, Enum, Float, ForeignKey, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import BIGINT, ENUM, INTEGER, LONGTEXT, TINYINT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class ActionType(Base):
    __tablename__ = 'action_types'

    id_action = Column(BIGINT(20), primary_key=True)
    action = Column(Enum('click', 'view', 'search'), nullable=False)
    id_product = Column(INTEGER(11), nullable=False)
    id_product_store = Column(INTEGER(11))
    Date = Column(DateTime, nullable=False)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)


class Brand(Base):
    __tablename__ = 'brands'

    id = Column(BIGINT(20), primary_key=True)
    name = Column(String(255, 'utf8mb4_unicode_ci'), nullable=False)
    description = Column(LONGTEXT, nullable=False)
    Specialite = Column(String(255, 'utf8mb4_unicode_ci'), server_default=text("'[]'"))
    logo = Column(String(255, 'utf8mb4_unicode_ci'), nullable=False)
    click_counts = Column(BIGINT(20))
    view_counts = Column(BIGINT(20))
    search_counts = Column(BIGINT(20))
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)


class Category(Base):
    __tablename__ = 'categories'

    id = Column(BIGINT(20), primary_key=True)
    name = Column(String(255, 'utf8mb4_unicode_ci'), nullable=False)
    description = Column(LONGTEXT, nullable=False)
    id_parent = Column(BIGINT(20))
    title_options = Column(String(255, 'utf8mb4_unicode_ci'), server_default=text("'[]'"))
    Specific_options = Column(String(255, 'utf8mb4_unicode_ci'), server_default=text("'[]'"))
    click_counts = Column(BIGINT(20))
    view_counts = Column(BIGINT(20))
    search_counts = Column(BIGINT(20))
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
    id_parent = Column(BIGINT(20), index=True)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)


t_password_resets = Table(
    'password_resets', metadata,
    Column('email', String(255, 'utf8mb4_unicode_ci'), nullable=False, index=True),
    Column('token', String(255, 'utf8mb4_unicode_ci'), nullable=False),
    Column('created_at', TIMESTAMP)
)


t_price_histories = Table(
    'price_histories', metadata,
    Column('id_product', INTEGER(11), nullable=False),
    Column('Date', DateTime, nullable=False),
    Column('Average', Float, nullable=False),
    Column('Best_price', Float, nullable=False)
)


class ProductDetail(Base):
    __tablename__ = 'product_details'

    id = Column(BIGINT(20), primary_key=True)
    rating_value = Column(DECIMAL(2, 1), nullable=False, server_default=text("0.0"))
    rating_count = Column(INTEGER(11), nullable=False, server_default=text("0"))
    short_description = Column(LONGTEXT, nullable=False)
    description = Column(LONGTEXT)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)


class Store(Base):
    __tablename__ = 'stores'

    id = Column(BIGINT(20), primary_key=True)
    name = Column(String(255, 'utf8mb4_unicode_ci'), nullable=False)
    description = Column(LONGTEXT, nullable=False)
    Specialite = Column(String(255, 'utf8mb4_unicode_ci'), nullable=False, server_default=text("'[]'"))
    phone = Column(BIGINT(20), nullable=False)
    email = Column(String(255, 'utf8mb4_unicode_ci'), nullable=False, unique=True)
    address = Column(String(255, 'utf8mb4_unicode_ci'), nullable=False)
    site_officiel = Column(String(255, 'utf8mb4_unicode_ci'), nullable=False)
    logo = Column(String(255, 'utf8mb4_unicode_ci'), nullable=False)
    click_counts = Column(BIGINT(20))
    view_counts = Column(BIGINT(20))
    search_counts = Column(BIGINT(20))
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)


class User(Base):
    __tablename__ = 'users'

    id = Column(BIGINT(20), primary_key=True)
    email = Column(String(255, 'utf8mb4_unicode_ci'), nullable=False)
    email_verified_at = Column(TIMESTAMP)
    password = Column(String(255, 'utf8mb4_unicode_ci'), nullable=False)
    role = Column(ENUM('0', '1', '2'), nullable=False, server_default=text("'0'"))
    remember_token = Column(String(100, 'utf8mb4_unicode_ci'))
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(BIGINT(20), primary_key=True)
    id_user = Column(ForeignKey('users.id'), nullable=False, index=True)
    name = Column(String(255, 'utf8mb4_unicode_ci'), nullable=False)
    gender = Column(ENUM('male', 'Female'), server_default=text("'male'"))
    address = Column(String(255, 'utf8mb4_unicode_ci'))
    About_me = Column(Text(collation='utf8mb4_unicode_ci'))
    image = Column(String(255, 'utf8mb4_unicode_ci'), server_default=text("'user_image.png'"))
    cover = Column(String(255, 'utf8mb4_unicode_ci'), server_default=text("'user_image.png'"))
    City_id = Column(CHAR(50, 'utf8mb4_unicode_ci'), server_default=text("'Tanger'"))
    phone = Column(BIGINT(20))
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

    user = relationship('User')


class Product(Base):
    __tablename__ = 'products'

    id = Column(BIGINT(20), primary_key=True)
    name = Column(String(255, 'utf8mb4_unicode_ci'), nullable=False, server_default=text("''"))
    title = Column(Text(collation='utf8mb4_unicode_ci'))
    slug = Column(Text(collation='utf8mb4_unicode_ci'))
    best_price = Column(DECIMAL(10, 0), server_default=text("0"))
    brand = Column(ForeignKey('brands.id'), nullable=False, index=True)
    category = Column(ForeignKey('categories.id'), nullable=False, index=True)
    product_details = Column(ForeignKey('product_details.id'), nullable=False, index=True)
    images = Column(Text(collation='utf8mb4_unicode_ci'))
    id_parent = Column(BIGINT(20))
    click_counts = Column(BIGINT(20), server_default=text("0"))
    view_counts = Column(BIGINT(20), server_default=text("0"))
    search_counts = Column(BIGINT(20), server_default=text("0"))
    options = Column(String(255, 'utf8mb4_unicode_ci'), nullable=False, server_default=text("'[]'"))
    choix_equipe = Column(TINYINT(1), nullable=False, server_default=text("1"))
    status = Column(TINYINT(1), nullable=False, server_default=text("1"))
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

    brand1 = relationship('Brand')
    category1 = relationship('Category')
    product_detail = relationship('ProductDetail')


class CustomerFavorite(Base):
    __tablename__ = 'customer_favorites'

    id = Column(BIGINT(20), primary_key=True)
    id_customer = Column(ForeignKey('customers.id'), nullable=False, index=True)
    id_product = Column(ForeignKey('products.id'), nullable=False, index=True)
    Date = Column(DateTime, nullable=False)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

    customer = relationship('Customer')
    product = relationship('Product')


class CustomerHistory(Base):
    __tablename__ = 'customer_histories'

    id = Column(BIGINT(20), primary_key=True)
    id_customer = Column(ForeignKey('customers.id'), nullable=False, index=True)
    id_product = Column(ForeignKey('products.id'), nullable=False, index=True)
    Date = Column(DateTime, nullable=False)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

    customer = relationship('Customer')
    product = relationship('Product')


class CustomerReview(Base):
    __tablename__ = 'customer_reviews'

    id = Column(BIGINT(20), primary_key=True)
    id_customer = Column(ForeignKey('customers.id'), nullable=False, index=True)
    id_product = Column(ForeignKey('products.id'), nullable=False, index=True)
    review_title = Column(String(255, 'utf8mb4_unicode_ci'), nullable=False)
    review_contenu = Column(LONGTEXT, nullable=False)
    rating_value = Column(DECIMAL(1, 1), nullable=False)
    review_statut = Column(String(255, 'utf8mb4_unicode_ci'), nullable=False)
    review_date = Column(DateTime, nullable=False)

    customer = relationship('Customer')
    product = relationship('Product')


class ProductStore(Base):
    __tablename__ = 'product__stores'

    id = Column(BIGINT(20), primary_key=True)
    id_product = Column(ForeignKey('products.id'), nullable=False, index=True)
    store = Column(ForeignKey('stores.id'), nullable=False, index=True)
    title = Column(Text(collation='utf8mb4_unicode_ci'))
    price = Column(DECIMAL(8, 2), nullable=False)
    link = Column(LONGTEXT, nullable=False)
    click_counts = Column(BIGINT(20))
    view_counts = Column(BIGINT(20))
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

    product = relationship('Product')
    store1 = relationship('Store')
