import pymongo
from io import BytesIO
from dotenv import load_dotenv
import os

load_dotenv()

ini = os.getenv('mgo_pass')
client = pymongo.MongoClient(f"mongodb+srv://test:{ini}@cluster0.beyzc.mongodb.net/?retryWrites=true&w=majority")
db = client.test

data_db = client['sample']
first_coll = data_db['abc']
second_coll = data_db['def']
third_coll = data_db['ghi']

d = dict(Name='Atanu', Age=24)

first_coll.insert_one(d)
second_coll.insert_one(d)
third_coll.insert_one(d)