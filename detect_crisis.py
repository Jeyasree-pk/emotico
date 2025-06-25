from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, constr
from utils.openai_utils import detect_crisis_llm

router = APIRouter(tags=["Detect Crisis"])

class CrisisRequest(BaseModel):
    text: constr(min_length=1, max_length=2000)

@router.post("/detect_crisis", summary="Detect crisis or suicidal intent in text")
async def detect_crisis(request: CrisisRequest):
    try:
        crisis = await detect_crisis_llm(request.text)
        return {"crisis_detected": crisis}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))