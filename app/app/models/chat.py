from app.core.db import db
from sqlalchemy import Column, BigInteger, sql


class Chat(db.Model):
    __tablename__ = 'chat'
    query: sql

    id = Column(BigInteger, unique=True, primary_key=True)
