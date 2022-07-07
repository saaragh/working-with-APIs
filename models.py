from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from database import Base


class  emp(Base):
    __tablename__ = "EMP"

    # fields
    emp_id = Column(Integer ,primary_key=True, index=True)
    first_name = Column(String(20))
    last_name = Column(String(20))
    city = Column(String)
    age = Column(Integer)
    experience = Column(Integer)
    ctc = Column(Integer)
    contact = Column(Integer)