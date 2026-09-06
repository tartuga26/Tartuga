import os, json
from typing import List, Dict

try:
    from openai import OpenAI
except Exception:
    OpenAI = None

def _client():
    key = os.getenv("OPENAI_API_KEY")
    if not key or not OpenAI:
        return None
    return OpenAI(api_key=key)

def generate_ideas(niche: str, count: int = 5, seed_topic: str | None = None) -> List[Dict]:
    client = _client()
    if not client:
        base = seed_topic or niche
        return [
            {"title": f"{base}: فكرة محتوى رقم {i+1}", "trend_score": 70+i*3, "ai_score": 75+i*2}
            for i in range(count)
        ]

    prompt = f'''أنت خبير صناعة محتوى قصير.
المجال: {niche}
موضوع مساعد: {seed_topic or "غير محدد"}
أنشئ {count} أفكار قوية ليوتيوب شورتس وتيك توك.
أرجع JSON array فقط، وكل عنصر:
title, trend_score, ai_score
والدرجات من 0 إلى 100.
'''
    r = client.responses.create(model="gpt-5-mini", input=prompt)
    text = r.output_text
    return json.loads(text)

def generate_script(idea: str, duration_seconds: int = 45, tone: str = "energetic") -> Dict:
    client = _client()
    if not client:
        return {
            "hook": f"هل تعرف السر وراء: {idea}؟",
            "body": f"ده سكربت تجريبي عن {idea}. أضف OPENAI_API_KEY للحصول على توليد فعلي.",
            "cta": "تابع للمزيد.",
            "duration_seconds": duration_seconds
        }

    prompt = f'''اكتب سكربت فيديو قصير بالعربية المصرية.
الفكرة: {idea}
المدة: {duration_seconds} ثانية
الأسلوب: {tone}
أرجع JSON فقط بالمفاتيح: hook, body, cta, duration_seconds.
'''
    r = client.responses.create(model="gpt-5-mini", input=prompt)
    return json.loads(r.output_text)

def create_video_plan(script: str, fmt: str = "9:16") -> Dict:
    client = _client()
    if not client:
        return {
            "format": fmt,
            "scenes": [
                {"scene": 1, "duration": 3, "visual": "Hook visual", "text": script[:80]},
                {"scene": 2, "duration": 7, "visual": "B-roll", "text": "Main point"},
            ]
        }

    prompt = f'''حوّل السكربت التالي إلى خطة مشاهد فيديو {fmt}.
لكل مشهد: scene, duration, visual_prompt, on_screen_text, transition.
أرجع JSON object فقط وفيه format و scenes.
السكريبت:
{script}
'''
    r = client.responses.create(model="gpt-5-mini", input=prompt)
    return json.loads(r.output_text)
