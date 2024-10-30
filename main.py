from fastapi import FastAPI

server = FastAPI()


@server.get(path="/")
def main_func():
    return "Hello from docker!"
