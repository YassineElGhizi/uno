from sqlalchemy import Column, String, TIMESTAMP, Text, text, DECIMAL
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Option(Base):
    __tablename__ = 'options'

    id = Column(BIGINT(20), primary_key=True)
    name = Column(String(255, 'utf8mb4_unicode_ci'), nullable=False)
    value = Column(String(255, 'utf8mb4_unicode_ci'))
    unit = Column(String(255, 'utf8mb4_unicode_ci'))
    id_parent = Column(BIGINT(20))
