from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root(name: str = "hihihihihi"):
    return {"message": f"Hello {name}"}