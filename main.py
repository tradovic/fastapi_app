from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users")
async def users():
    users = [
        {
            "name": "Harry Potter",
            "city": "London"
        },
        {
            "name": "Don Quixote",
            "city": "Madrid"
        },
        {
            "name": "Joan of Arc",
            "city": "Paris"
        },
        {
            "name": "Rosa Park",
            "city": "Alabama"
        }
    ]

    return users