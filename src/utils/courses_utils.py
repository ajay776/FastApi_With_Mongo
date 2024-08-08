from fastapi import HTTPException


async def get_courses(collection, sort_by, domain):
    query = {}
    if domain:
        query["domain"] = domain
    courses = list(collection.find(query))
    if sort_by == "name":
        courses.sort(key=lambda x: x["name"])
    elif sort_by == "date":
        courses.sort(key=lambda x: x["date"], reverse=True)

    elif sort_by == "rating":
        for course in courses:
            course["total_rating"] = sum(
                chapter.get("rating", 0) for chapter in course.get("chapters", [])
            )
        courses.sort(key=lambda x: x.get("total_rating", 0), reverse=True)
    return courses


async def get_course_overview(course_name, collection):
    course = collection.find_one({"name": course_name})
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course


async def get_chapter_info(course_name, chapter_name, collection):
    course = collection.find_one({"name": course_name})
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    for chapter in course["chapters"]:
        if chapter["name"] == chapter_name:
            return chapter
    raise HTTPException(status_code=404, detail="Chapter not found")


async def rate_chapter(course_name, chapter_name, rating, collection):
    course = collection.find_one({"name": course_name})
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    chapter_found = False
    for chapter in course["chapters"]:
        if chapter["name"] == chapter_name:
            chapter_found = True
            chapter["rating"] = chapter.get("rating", 0) + (1 if rating else -1)
    if not chapter_found:
        raise HTTPException(status_code=404, detail="Chapter not found")
    print(course["chapters"])
    collection.update_one(
        {"name": course_name}, {"$set": {"chapters": course["chapters"]}}
    )
    return {"message": "Rating updated"}
