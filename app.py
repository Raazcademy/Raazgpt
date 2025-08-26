from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
import uvicorn

app = FastAPI(title="RaazGPT Chatbot")

@app.get("/")
def home():
    return HTMLResponse("""
    <h1>✨🤖 Welcome to RaazGPT 📚🔱🚀</h1>
    <p>आपका online exam mentor और AI chatbot!</p>
    """)

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_message = data.get("message", "")
    response = f"आपने पूछा: {user_message} | (यहाँ chatbot response आएगा)"
    return JSONResponse({"response": response})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
