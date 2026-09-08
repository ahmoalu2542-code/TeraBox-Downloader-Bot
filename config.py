# ================== TELEGRAM API CONFIG ==================
# Get these from https://my.telegram.org/apps
API_ID = 22210381
API_HASH = "711f5af4daf6e93382e1e0c5dbcf3cee"

# Bot token from @BotFather
BOT_TOKEN = "8614639817:AAHWQvW9ZUWF4jVqzOtl587hq34vGdNm39A"


# ================== REDIS DATABASE CONFIG ==================

# Redis Host / Port / Password
HOST = "ample-cup-sense-29951.db.redis.io"
PORT = 18767
PASSWORD = "YKwDTv4oECA0JECJqAdt1PyE2ziULvEW"   # Set to None if Redis has no password


# ================== BOT SETTINGS ==================

# Private storage chat where files are uploaded
# Use your private channel / chat ID (must be integer)
PRIVATE_CHAT_ID = -5115087937

# Folder where downloaded videos are stored on the VPS
DOWNLOAD_DIR = "downloads"


# ================== ADMIN & OWNER ==================

# Owner — only this user can run /update, /setstorage, /panic, /addadmin
OWNER_ID = 6780677991

# Admin user IDs (MUST be integers)
# Owner is automatically admin
ADMINS = [
    123456789,
]


# ================== FORCE JOIN CHANNELS & GROUPS ==================

# Users must join these before using the bot
# Use username (e.g. "@your_channel") or chat ID (e.g. -1001234567890)
FORCE_CHANNELS = [
    "@your_channel",
]

FORCE_GROUPS = [
    "@your_group",
]


# ================== TERA BOX API ==================

TERABOX_API_BASE = "https://ntmtbapi.saiyanprojects.com/"
TERABOX_API_TOKEN = "ntmtbapi0011"

TERABOX_API_TEMPLATE = (
    f"{TERABOX_API_BASE}?authkey={TERABOX_API_TOKEN}&url={{url}}"
)

# Fallback API — used when primary API returns no files
TERABOX_FALLBACK_API_BASE = "https://your-fallback-api.com/"
TERABOX_FALLBACK_API_TEMPLATE = (
    f"{TERABOX_FALLBACK_API_BASE}?authkey={TERABOX_API_TOKEN}&url={{url}}"
)

# Self-hosted Telegram Bot API server (replaces https://api.telegram.org)
# Enables high-speed uploads up to 2GB via the Bot HTTP API.
TG_API_BASE = "https://your-bot-api-server.com"


# ================== UPDATE SETTINGS ==================

GITHUB_REPO = "https://github.com/your-username/your-repo"
