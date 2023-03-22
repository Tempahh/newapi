from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.sql.expression import null
from ..Appk.database import Base

class media(Base):
    __tablename__ = "media"
id = Column(Integer, primary_key=True, nullable=False)
title = Column(String, nullable=False)
content = Column(String, nullable=False)
published = Column(Boolean, default=True)

