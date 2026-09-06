from pydantic import BaseModel
from typing import Optional, List

class IdeaGenerateRequest(BaseModel):
    niche: str = "music"
    count: int = 5
    seed_topic: Optional[str] = None

class IdeaOut(BaseModel):
    title: str
    trend_score: float
    ai_score: float

class ScriptGenerateRequest(BaseModel):
    idea: str
    duration_seconds: int = 45
    tone: str = "energetic"

class VideoPlanRequest(BaseModel):
    script: str
    format: str = "9:16"

class PublishRequest(BaseModel):
    title: str
    description: str = ""
    video_path: str
    privacy: str = "private"
