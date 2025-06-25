from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, constr
from utils.openai_utils import analyze_mood_llm

router = APIRouter(tags=["Analyze Mood"])

class MoodRequest(BaseModel):
    text: constr(min_length=1, max_length=2000)

@router.post("/analyze_mood", summary="Detect emotion from text")
async def analyze_mood(request: MoodRequest):
    try:
        emotion = await analyze_mood_llm(request.text)
        return {"emotion": emotion}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))