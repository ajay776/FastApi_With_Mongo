from pymongo import MongoClient
from .settings import DB_URL
import json
import os


async def read_courses():
    file_path = os.path.abspath(os.path.join("src", "courses.json"))
    with open(file_path) as f:
        courses = json.load(f)
    return courses


async def fetch_collections():
    courses = await read_courses()
    return courses


async def load_db():
    client = MongoClient(DB_URL)
    db = client["course_database"]
    collection = db["courses"]
    return collection


async def insert_and_make_indexes():
    collection = await load_db()
    courses = await fetch_collections()
    collection.delete_many({})
    collection.insert_many(courses)
    collection.create_index("name")
    collection.create_index("date")
    return True
