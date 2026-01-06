from database import getserver
import logging

LOGGER = logging.getLogger(__name__)

def connect_server():
    try:
        getserver.connect_v1()
        LOGGER.info("✅ Database Server Connected")
    except Exception as e:
        LOGGER.error(f"❌ Database Connection Failed: {e}")

if __name__ == "__main__":
    connect_server()