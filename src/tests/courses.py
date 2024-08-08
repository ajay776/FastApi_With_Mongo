import pytest
from httpx import AsyncClient
from src.main import app

BASE_URL = "http://127.0.0.1:8000/api"


@pytest.mark.asyncio
async def test_get_courses():
    async with AsyncClient(app=app, base_url=BASE_URL) as ac:
        response = await ac.get("/courses")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_course_overview():
    async with AsyncClient(app=app, base_url=BASE_URL) as ac:
        response = await ac.get("/courses/Highlights of Calculus")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_chapter_info():
    async with AsyncClient(app=app, base_url=BASE_URL) as ac:
        response = await ac.get(
            "/courses/Highlights of Calculus/chapters/Big Picture of Calculus"
        )
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_rate_chapter():
    async with AsyncClient(app=app, base_url=BASE_URL) as ac:
        response = await ac.post(
            "/courses/Highlights of Calculus/chapters/Big Picture of Calculus/rate",
            params={"rating": True},
        )

    assert response.status_code == 200
