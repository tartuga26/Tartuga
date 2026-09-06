from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey
from sqlalchemy.sql import func
from .database import Base

class Idea(Base):
    __tablename__ = "ideas"
    id = Column(Integer, primary_key=True)
    title = Column(String(300), nullable=False)
    niche = Column(String(100), default="general")
    trend_score = Column(Float, default=0)
    ai_score = Column(Float, default=0)
    status = Column(String(50), default="new")
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Script(Base):
    __tablename__ = "scripts"
    id = Column(Integer, primary_key=True)
    idea_id = Column(Integer, ForeignKey("ideas.id"), nullable=False)
    hook = Column(Text)
    body = Column(Text)
    cta = Column(Text)
    duration_seconds = Column(Integer, default=45)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    platform = Column(String(50), nullable=False)
    external_post_id = Column(String(255))
    title = Column(String(300))
    status = Column(String(50), default="draft")
    views = Column(Integer, default=0)
    likes = Column(Integer, default=0)
    comments = Column(Integer, default=0)
    watch_time = Column(Float, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
