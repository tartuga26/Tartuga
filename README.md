# AI Content Factory MVP

نسخة أولية قابلة للتطوير لنظام إنشاء الأفكار، كتابة السكربت، تجهيز المحتوى، ثم النشر على YouTube وTikTok.

## المكونات
- FastAPI backend
- PostgreSQL database
- SQLAlchemy models
- OpenAI-ready AI service layer
- YouTube/TikTok publisher stubs
- n8n starter workflow
- Docker Compose
- REST API endpoints

## التشغيل السريع
1. انسخ `.env.example` إلى `.env`
2. أضف مفاتيح الـAPI الخاصة بك
3. شغّل:
   docker compose up --build

ثم افتح:
- API: http://localhost:8000
- Swagger: http://localhost:8000/docs
- n8n: http://localhost:5678

## أهم Endpoints
- POST /ideas/generate
- POST /scripts/generate
- POST /videos/plan
- POST /publish/youtube
- POST /publish/tiktok
- GET /analytics/{post_id}

## ملاحظة
النشر الحقيقي يحتاج OAuth وربط حسابات YouTube وTikTok وموافقة التطبيقات حسب متطلبات كل منصة.
