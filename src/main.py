from fastapi import FastAPI

from src.routers import courses
from src.configurations.db_config import insert_and_make_indexes

app = FastAPI()


app.include_router(courses.router)

app.add_event_handler("startup", insert_and_make_indexes)
