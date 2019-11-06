#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/10/31 18:20
# @Author : Srunkyo
# @File   : models.py

from sqlalchemy import create_engine, Column, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Integer, SmallInteger, String, Date, DateTime, Float, Boolean, Text, LargeBinary)

from scrapy.utils.project import get_project_settings

DeclarativeBase = declarative_base()


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(get_project_settings().get("CONNECTION_STRING"))


def create_table(engine):
    DeclarativeBase.metadata.create_all(engine)


class ShoeTable(DeclarativeBase):
    __tablename__ = "shoe"

    id = Column(Integer, primary_key=True)
    title = Column('title', String(200))
    sub_title = Column('subtitle', String(200), nullable=True)
    price = Column('price', Float(), nullable=False)
    link = Column('link', Text(), nullable=True)
    image_url = Column('image_url', Text(), nullable=True)
    source = Column('source', String(20), nullable=False)
    
