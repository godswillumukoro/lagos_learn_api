from typing import Optional, List
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

description = """
LagosLearn API is engineered to streamline the management of educational resources, enabling easy integration of diverse learning materials, such as courses, modules, assessments, and multimedia content. It empowers educators to create engaging and personalized learning experiences, fostering dynamic interactions and knowledge dissemination among students.

The API offers a range of features tailored to meet the specific needs of educators, students, and institutions within the bustling educational landscape of Lagos, Nigeria. Its user-friendly interface and robust functionality make it an ideal solution for educational organizations seeking to optimize their learning processes.
## Items

You can **read items**.

## Users

You will be able to:

* **Create users** (_not implemented_).
* **Read users** (_not implemented_).
"""

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
    #     "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    # },
)

users = []


class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str] = None


@app.get("/users", response_model=List[User])
async def get_users():
    return users


@app.post("/users")
async def create_user(user: User):
    users.append(user)
    return {'message': 'New user added'}


@app.get("/users/{id}")
async def get_user(
    id: int = Path(..., description="User ID", gt=2),
    q: str = Query(None, maxx_length=5)
):
    return {"user": users[id], "query": q}
