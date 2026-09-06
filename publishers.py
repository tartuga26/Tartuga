def publish_youtube(title: str, description: str, video_path: str, privacy: str = "private"):
    # TODO: OAuth2 + YouTube Data API videos.insert
    return {
        "platform": "youtube",
        "status": "not_configured",
        "message": "أضف OAuth credentials ثم نفّذ الرفع عبر YouTube Data API.",
        "title": title,
        "video_path": video_path,
        "privacy": privacy,
    }

def publish_tiktok(title: str, description: str, video_path: str, privacy: str = "private"):
    # TODO: TikTok Content Posting API
    return {
        "platform": "tiktok",
        "status": "not_configured",
        "message": "أضف TikTok app credentials ثم فعّل Direct Post أو Upload Draft.",
        "title": title,
        "video_path": video_path,
        "privacy": privacy,
    }
