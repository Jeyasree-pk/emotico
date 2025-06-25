from fastapi import FastAPI
from routes.analyze_mood import router as analyze_mood_router
from routes.detect_crisis import router as detect_crisis_router
from routes.summarize import router as summarize_router

app = FastAPI(
    title="MoodDecode NLP API",
    description="APIs to analyze mood, detect crisis, and summarize text using LLMs.",
    version="2.0.0"
)

# Include routers from routes/
app.include_router(analyze_mood_router)
app.include_router(detect_crisis_router)
app.include_router(summarize_router)