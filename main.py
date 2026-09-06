from fastapi import FastAPI
from database import Base, engine
from schemas import IdeaGenerateRequest, ScriptGenerateRequest, VideoPlanRequest, PublishRequest
from ai_service import generate_ideas, generate_script, create_video_plan
from publishers import publish_youtube, publish_tiktok

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Content Factory", version="0.1.0")

@app.get("/")
def root():
    return {
        "name": "AI Content Factory",
        "version": "0.1.0",
        "status": "running"
    }

@app.post("/ideas/generate")
def ideas(req: IdeaGenerateRequest):
    return {"ideas": generate_ideas(req.niche, req.count, req.seed_topic)}

@app.post("/scripts/generate")
def scripts(req: ScriptGenerateRequest):
    return generate_script(req.idea, req.duration_seconds, req.tone)

@app.post("/videos/plan")
def video_plan(req: VideoPlanRequest):
    return create_video_plan(req.script, req.format)

@app.post("/publish/youtube")
def youtube(req: PublishRequest):
    return publish_youtube(req.title, req.description, req.video_path, req.privacy)

@app.post("/publish/tiktok")
def tiktok(req: PublishRequest):
    return publish_tiktok(req.title, req.description, req.video_path, req.privacy)

@app.get("/analytics/{post_id}")
def analytics(post_id: int):
    return {
        "post_id": post_id,
        "views": 0,
        "likes": 0,
        "comments": 0,
        "watch_time": 0,
        "status": "analytics_connector_not_configured"
    }
