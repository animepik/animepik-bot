from app.core.db import db
from sqlalchemy import Column, BigInteger, sql


class User(db.Model):
    __tablename__ = 'user'
    query: sql

    id = Column(BigInteger, unique=True, primary_key=True)
