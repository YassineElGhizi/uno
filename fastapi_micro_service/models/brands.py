from sqlalchemy import Column, String, TIMESTAMP, text
from sqlalchemy.dialects.mysql import BIGINT, LONGTEXT
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata

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