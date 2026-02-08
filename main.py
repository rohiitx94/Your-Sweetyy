from fastapi import FastAPI, HTTPException, BackgroundTasks, Header, Request
from pydantic import BaseModel
from typing import List, Optional
import os
from dotenv import load_dotenv
from brain import process_conversation
from utils import extract_intel, send_callback

# 1. Load Environment Variables
load_dotenv()
MY_SECRET_KEY = os.getenv("MY_SECRET_KEY")

app = FastAPI()

# --- Response Models ---
class ChatResponse(BaseModel):
    reply: str
    conversationId: str

@app.get("/")
def home():
    return {"status": "Active", "message": "Rajesh is ready to waste time."}

@app.post("/chat")
async def chat_endpoint(raw_request: Request, background_tasks: BackgroundTasks, x_api_key: str = Header(None)):
    # 2. SECURITY CHECK
    # We strip whitespace just in case
    if x_api_key is None or x_api_key.strip() != MY_SECRET_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    # 3. GOD MODE: PRINT RAW DATA
    try:
        body = await raw_request.json()
        print(f"\n🔥🔥🔥 INCOMING DATA: {body} 🔥🔥🔥\n")
    except Exception as e:
        print(f"❌ COULD NOT READ JSON: {e}")
        raise HTTPException(status_code=400, detail="Invalid JSON")

    # 4. Manual Data Handling (To avoid Validation Errors)
    user_msg = "Unknown"
    session_id = body.get("sessionId", "unknown-session")
    
    # Try to find the message text in different common places
    if "message" in body and isinstance(body["message"], dict):
        user_msg = body["message"].get("text", "")
    elif "text" in body:
        user_msg = body["text"]
    elif "input" in body:
        user_msg = body["input"]
    
    # 5. Generate AI Reply
    # We pass 'No history' because God Mode is stateless for safety
    is_scam, reply_text = process_conversation("No history", user_msg)

    # --- 6. SEND CHAT REPLY (CORRECT FORMAT FOR JUDGES) ---
    return {
        "status": "success",          # <--- THIS WAS MISSING!
        "reply": reply_text,
        "conversationId": session_id  # We keep this just in case
    }