
from itemadapter import ItemAdapter
import json
import pymysql

class PoemscrapyPipeline:
    def __init__(self):
        self.connect = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='mengshuo',  # 设置成用户自己的数据库密码
            db='poem',
            charset='utf8'
        )
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        self.cursor.execute('INSERT INTO beautifulsentence(source,sentence,content,url)VALUES("{}", "{}", "{}", "{}")'.format(item['source'], item['sentence'], item['content'], item['url']))
        self.connect.commit()
        return item

    def close_spider(self, spider):
        # 关闭数据库连接
        self.cursor.close()
        self.connect.close()

