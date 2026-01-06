import os

class Config(object):

    # ===== REQUIRED (Render ENV se aayega) =====
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    API_ID = int(os.environ.get("API_ID", 0))
    API_HASH = os.environ.get("API_HASH")

    DB_URL = os.environ.get("DB_URL")
    DB_NAME = os.environ.get("DB_NAME", "WARRIOR_EXTRACTOR")

    # ===== ADMINS =====
    ADMIN = os.environ.get("ADMIN", "752140,59194").split(",")
    ADMIN_ID = [int(i) for i in ADMIN if i.isdigit()]

    # ===== LOG CHANNELS =====
    TXT_LOG = int(os.environ.get("TXT_LOG", -10023125))
    AUTH_LOG = int(os.environ.get("AUTH_LOG", -10023802))
    HIT_LOG = int(os.environ.get("HIT_LOG", -100247596))
    DRM_DUMP = int(os.environ.get("DRM_DUMP", -10024562))

    # ===== CHANNEL INFO =====
    CHANNEL = int(os.environ.get("CHANNEL", -10022752))
    CH_URL = os.environ.get("CH_URL", "https://t.me/+vX1JFN-Mzhl")
    OWNER = os.environ.get("OWNER", "https://t.me/mrcraacker")

    # ===== EXTRA =====
    THUMB_URL = os.environ.get(
        "THUMB_URL",
        "https://vault.pictures/media/images/b9/ad/12/b9ad123d95cd49465fcb954d.jpg"
    )

    HOST = os.environ.get(
        "HOST",
        "https://drm-api-five.vercel.app"
    )