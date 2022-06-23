import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgDFhFw814pbes49RyXoLqh_pmzvy5DnH09ZFG-xQnZThh4DMkZbfsTbmXt-wGvumEnQYOLDyh2U26FT_KQ6S40Dc8MvbCtwmFDDM-xXr5FYY2iv-oeEOy9p6zkq3hSFb74o7S9f176zD9rq_QoAPT11osa0mqlsLZYrWip6RwzhuhB6TivPOInHbUCA6F-hrdXBAkk_g3-i894q-jAwFZIIfkkLZeXN3hyGVInEGjcbpZQeNwU4ux-NwuA0iGzA3oYXm6f4u6r4DAek2h3zweP4fOMAGHVATvUq1h5U2v5xVKmQMCRLdMqcjZKZu5pR2xoA8Jho36R3ZXo6iw52Q40mAAAAATtJ9AIA")
BOT_TOKEN = getenv("BOT_TOKEN", "5457201440:AAHInLbclae0s2yuhP3BfwwXv9yhS4WtTH8")
BOT_NAME = getenv("BOT_NAME", "test song")
API_ID = int(getenv("API_ID", "14717801"))
API_HASH = getenv("API_HASH", "2128a1b9db325d6c1211a57d4bd60a3d")
OWNER_NAME = getenv("OWNER_NAME", "Taha")
OWNER_USERNAME = getenv("OWNER_USERNAME", "TTTTZ9")
ALIVE_NAME = getenv("ALIVE_NAME", "TAHA")
BOT_USERNAME = getenv("BOT_USERNAME", "testtahabot")
OWNER_ID = getenv("OWNER_ID"٫ "5564738618")
ASSISTANT_NAME = getenv("ASSISTANT_NAME"٫ "een6e")
GROUP_SUPPORT = getenv("GROUP_SUPPORT"٫ "ttttz9")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5564738618").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/a79d792baacc982ff57bd.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/8951a422fad655259d86a.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ERTWF/WASDF")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/e53f65a49c4ee5553fab9.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/880f7e9706591af8d0bfa.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/324399325cf48ff25a494.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/a79d792baacc982ff57bd.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/e53f65a49c4ee5553fab9.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/a79d792baacc982ff57bd.jpg")
