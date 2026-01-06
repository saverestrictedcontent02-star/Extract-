from config import Config
from pyrogram import Client, idle
import asyncio, logging, os, threading
from serverV1 import app   # Flask app

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)
LOGGER.info("Live log streaming to telegram.")

plugins = dict(root="plugins")

bot = Client(
    "Master",
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    sleep_threshold=120,
    plugins=plugins,
    workers=10000,
)

async def start_bot():
    await bot.start()
    bot_info = await bot.get_me()
    LOGGER.info(f"<--- @{bot_info.username} Started --->")
    await idle()
    LOGGER.info("<--- Bot Stopped --->")

def run_bot():
    asyncio.run(start_bot())

if __name__ == "__main__":
    # Bot thread
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.start()

    # Flask server (Render ke liye mandatory)
    port = int(os.environ.get("PORT", 10000))
    LOGGER.info(f"🌐 Web Server running on port {port}")
    app.run(host="0.0.0.0", port=port)