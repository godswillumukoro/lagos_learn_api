from typing import Optional, List
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from api_description import description
from api import users, courses, sections

app = FastAPI(
    title="LagosLearn API",
    description=description,
    summary="Take Courses, Get Skilled Up 🚀",
    version="1.0",
    terms_of_service="https://github.com/godswillumukoro/lagos_learn_api",
    contact={
        "name": "LagosLearn API",
        "url": "https://github.com/godswillumukoro/lagos_learn_api",
        "email": "umukoro6@gmail.com",
    },
    # license_info={
    #     "name": "Apache 2.0",
    #     "url": "https://www.apache.org/licenses/LICENSE-  
    # },
)

app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)





