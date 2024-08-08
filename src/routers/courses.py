from typing import List, Optional, Annotated, Any
from src.configurations.db_config import load_db
from fastapi import APIRouter, Depends
from src.schemas.courses import Course, Chapter
from src.utils import courses_utils

router = APIRouter(prefix="/api", tags=["Courses"])


@router.get(
    "/courses",
    response_model=List[Course],
)
async def get_courses(
    collection: Annotated[Any, Depends(load_db)],
    sort_by: Optional[str] = "name",
    domain: Optional[str] = None,
):
    return await courses_utils.get_courses(collection, sort_by, domain)


@router.get("/courses/{course_name}", response_model=Course)
async def get_course_overview(
    course_name: str, collection: Annotated[Any, Depends(load_db)]
):

    return await courses_utils.get_course_overview(course_name, collection)


@router.get("/courses/{course_name}/chapters/{chapter_name}", response_model=Chapter)
async def get_chapter_info(
    course_name: str, chapter_name: str, collection: Annotated[Any, Depends(load_db)]
):
    return await courses_utils.get_chapter_info(course_name, chapter_name, collection)


@router.post("/courses/{course_name}/chapters/{chapter_name}/rate")
async def rate_chapter(
    course_name: str,
    chapter_name: str,
    rating: bool,
    collection: Annotated[Any, Depends(load_db)],
):
    return await courses_utils.rate_chapter(
        course_name, chapter_name, rating, collection
    )
