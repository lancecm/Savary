# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from sqlalchemy.orm import sessionmaker
from savary.models import ShoeTable, db_connect, create_table
from savary.middlewares import driver


class SavaryPipeline(object):
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def close_spider(self, spider):
        driver.close()

    def process_item(self, item, spider):
        session = self.Session()
        shoe = ShoeTable()
        try:
            is_exist = session.query(ShoeTable).filter_by(title=item["title"], sub_title=item["sub_title"]).first()
            print(is_exist)
            if is_exist is None:
                shoe.title = item["title"]
                shoe.sub_title = item["sub_title"]
                shoe.price = item["price"]
                shoe.link = item["link"]
                shoe.image_url = item["image_url"]
                shoe.source = item["source"]

                session.add(shoe)
            else:
                session.query(ShoeTable). \
                    filter_by(title=item["title"], sub_title=item["sub_title"]). \
                    update({ShoeTable.price: item["price"], ShoeTable.image_url: item["image_url"]},
                           synchronize_session=False)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item
