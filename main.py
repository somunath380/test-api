from fastapi import FastAPI

app = FastAPI()

@app.get("/_healthz")
def read_root():
    return {"message": "success"}

@app.get("/{msg}")
def echo_msg(msg: str):
    return {"msg":msg}