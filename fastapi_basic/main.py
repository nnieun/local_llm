# uv add "fastapi[standard]"
# 출처 : https://fastapi.tiangolo.com/ko/#typer-the-fastapi-of-clis

#uv run fastapi dev # fast api 실행할 껀데 개발자모드로 실행할꺼야 
# 이건 main.py 파일이 있는 경로에서 실행해야함
# 이거 하게 되면 file ->  Auto Save 하면 안됨 (서버띄울때 하지마세요 )

from fastapi import FastAPI
from pydantic import BaseModel,HttpUrl
# uv add pydantic
from typing import Optional

#DTO : 데이터 전송 객체
class UserCreate(BaseModel):
    username: str
    password: str
    avatar_url: Optional[HttpUrl] = None
    user_fullname: Optional[str] = None

app = FastAPI()

# http://127.0.0.1:8000
# http://127.0.0.1:8000/docs


@app.get("/")
def read_root():
    # data = "DB에서 데이터 읽어보기 "
    data = {"message": "Hello, World!"}
    return data


@app.get("/items")
def read_item():
    item_id = 1
    q = "사과"
    return {"item_id": item_id, "q": q}

# 블록잡기  + shift + alt + 방향키 -> 복사해서 붙여넣기 

# http://localhost:8000/items/300?q=치킨
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    #비즈니스로직처리
    print(f"item_id : {item_id}, q : {q}")
    return {"item_id": item_id, "q": q}


@app.post("/user_info/")
def create_user(user: UserCreate):
    #비즈니스로직처리
    print(f"user.username : {user.username}")
    print(f"user.avatar_url : {user.avatar_url}")
    print(f"user.password : {user.password}")
    print(f"user.user_fullname : {user.user_fullname}")
    return {"user": user}


@app.post("/user_info/{user_id}")
def read_item(user_id: int, q: str | None = None):
    #비즈니스로직처리
    print(f"user_id : {user_id}, q : {q}")
    return {"user_id": user_id, "q": q}










