from fastapi import FastAPI
from fastapi import Request
import uvicorn
app = FastAPI()

@app.get("/health")
def read_root():
    return {"message": "AgentAtlas is running"}

@app.post("/get_agent_response")
def get_agent_response(request: Request):
    user_input = request.json()["user_input"]
    return {"message": f"Agent response: {user_input}"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)