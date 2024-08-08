from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from typing import List, Optional
from pydantic import BaseModel


class Chapter(BaseModel):
    name: str
    text: str
    rating: Optional[int] = None


class Course(BaseModel):
    name: str
    date: int
    description: str
    domain: List[str]
    chapters: List[Chapter]
