#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/10/31 18:28
# @Author : Srunkyo
# @File   : dbtest.py

from sqlalchemy.orm import sessionmaker
from savary.models import ShoeTable, db_connect, create_table

engine = db_connect()
create_table(engine)
Session = sessionmaker(bind=engine)

session = Session()
nike_table = ShoeTable()
nike_table.title = "test t"
nike_table.sub_title = "test sub_t"
nike_table.price = "1"

try:
    session.add(nike_table)
    session.commit()

    #query again
    obj = session.query(ShoeTable).first()
    print(obj.title)
    print(obj.sub_title)
except:
    session.rollback()
    raise
finally:
    session.close()