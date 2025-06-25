from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, constr
from utils.openai_utils import summarize_llm

router = APIRouter(tags=["Summarize"])

class SummarizeRequest(BaseModel):
    text: constr(min_length=10, max_length=3000)

@router.post("/summarize", summary="Summarize long input text")
async def summarize(request: SummarizeRequest):
    try:
        summary = await summarize_llm(request.text)
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))