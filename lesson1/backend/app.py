from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root(name: str = "nononononono"):
    return {"message": f"Hello {name}"}