from fastapi import FastAPI
from env.env import CodeReviewEnv
from env.models import Action

app = FastAPI()

env = CodeReviewEnv()

@app.post("/reset")
def reset():
    obs = env.reset()
    return obs.dict()

@app.post("/step")
def step(action: dict):
    act = Action(**action)
    obs, reward, done, info = env.step(act)
    return {
        "observation": obs.dict(),
        "reward": reward,
        "done": done,
        "info": info
    }

@app.get("/")
def root():
    return {"status": "ok"}