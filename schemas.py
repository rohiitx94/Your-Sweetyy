from pydantic import BaseModel, validator
from typing import List, Optional, Any

# --- 1. RESPONSE MODELS ---
class APIResponse(BaseModel):
    status: str
    reply: str

class ChatResponse(BaseModel):
    reply: str
    conversationId: str

# --- 2. INCOMING REQUEST MODELS (Bulletproof) ---
class Metadata(BaseModel):
    channel: Optional[str] = "SMS"
    language: Optional[str] = "English"
    locale: Optional[str] = "IN"

class MessageItem(BaseModel):
    sender: Optional[str] = "scammer"
    text: str 
    timestamp: Optional[str] = None

class IncomingRequest(BaseModel):
    sessionId: str
    message: MessageItem
    conversationHistory: Optional[List[MessageItem]] = []
    metadata: Optional[Metadata] = None

    # --- SAFETY VALIDATORS (The Magic Fix) ---
    # These force 'null' values to become empty lists/objects
    # preventing "NoneType" crashes in main.py
    
    @validator('conversationHistory', pre=True, always=True)
    def handle_null_history(cls, v):
        if v is None:
            return []
        return v

    @validator('metadata', pre=True, always=True)
    def handle_null_metadata(cls, v):
        if v is None:
            return Metadata()
        return v

# --- 3. INTELLIGENCE MODELS ---
class ExtractedIntelligence(BaseModel):
    phoneNumbers: List[str] = []
    upiIds: List[str] = []
    bankAccounts: List[str] = []
    phishingLinks: List[str] = []
    locations: List[str] = []
    
class FinalCallbackPayload(BaseModel):
    sessionId: str
    scammerId: str
    summary: str
    riskScore: int
    intelligence: ExtractedIntelligence