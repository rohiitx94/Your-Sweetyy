import re
import aiohttp
import os

# 1. THE SPY TOOL (Extracts links & numbers)
def extract_intel(text: str):
    intel = {
        "phoneNumbers": [],
        "upiIds": [],
        "bankAccounts": [],
        "phishingLinks": [],
        "locations": []
    }
    
    # Regex Patterns
    patterns = {
        "phoneNumbers": r'\b[6-9]\d{9}\b',
        "upiIds": r'[a-zA-Z0-9.\-_]{2,256}@[a-zA-Z]{2,64}',
        "bankAccounts": r'\b\d{9,18}\b',
        "phishingLinks": r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
    }
    
    for key, pattern in patterns.items():
        found = re.findall(pattern, text)
        intel[key] = list(set(found)) # Remove duplicates
        
    return intel

# 2. THE REPORTER TOOL (Sends data back to HQ)
async def send_callback(session_id: str, summary: str, risk_score: int, intel: dict):
    callback_url = "https://hackathon.guvi.in/api/updateHoneyPotFinalResult"
    
    payload = {
        "sessionId": session_id,
        "scammerId": "unknown_scammer",
        "summary": summary,
        "riskScore": risk_score,
        "intelligence": intel
    }
    
    print(f"📡 SENDING CALLBACK for {session_id}...")
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(callback_url, json=payload) as resp:
                print(f"✅ CALLBACK STATUS: {resp.status}")
                response_text = await resp.text()
                print(f"📋 CALLBACK REPLY: {response_text}")
    except Exception as e:
        print(f"❌ CALLBACK FAILED: {e}")