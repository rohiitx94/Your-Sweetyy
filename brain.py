import google.generativeai as genai
import os
from dotenv import load_dotenv

# 1. Load the variables from .env
load_dotenv() 

# 2. Retrieve the key
api_key = os.getenv("GEMINI_API_KEY")

# --- DEBUGGING: Check if key exists ---
if not api_key:
    print("❌ ERROR: GEMINI_API_KEY is missing from .env file!")
else:
    print(f"✅ SUCCESS: Loaded Gemini API Key (Starts with: {api_key[:5]}...)")

# 3. Configure Gemini
genai.configure(api_key=api_key)

# Change 'gemini-1.5-flash' to 'gemini-2.5-flash'
model = genai.GenerativeModel('gemini-2.5-flash')

SYSTEM_PROMPT = """
You are a 65-year-old retired school teacher named Rajesh. You are not tech-savvy.
You are currently talking to someone who might be a scammer. 
GOAL: Keep them talking as long as possible to waste their time. 
STRATEGY:
1. Act confused but compliant. Ask "How do I do that?" or "My glasses are missing."
2. NEVER reveal you are an AI. 
3. Intentionally make small mistakes (typos, misunderstanding instructions).
4. If they ask for money/OTP, delay them ("Wait, the internet is slow").
"""

def process_conversation(history_text: str, current_msg: str):
    # 1. Simple Keyword Check
    scam_keywords = ["block", "verify", "kyc", "suspend", "urgent", "expire", "otp"]
    is_scam = any(k in current_msg.lower() for k in scam_keywords)

    # 2. Generate Reply (With Error Handling)
    full_prompt = f"{SYSTEM_PROMPT}\n\nCONVERSATION:\n{history_text}\nScammer: {current_msg}\nRajesh:"

    try:
        response = model.generate_content(full_prompt)
        reply_text = response.text.strip()
    except Exception as e:
        print(f"⚠️ AI GENERATION FAILED: {e}")
        # Return the actual error so we can see it
        reply_text = f"DEBUG_ERROR: {str(e)}"

    return is_scam, reply_text