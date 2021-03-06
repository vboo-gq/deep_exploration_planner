"""Deep Exploration Planner"""

import os
import logging

import telegram
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from apscheduler.schedulers.background import BackgroundScheduler


load_dotenv()

# Telegram
TELEGRAM_BOT = telegram.Bot(os.environ['TELEGRAM_KEY'])

# database
ENGINE = create_engine(os.environ["DATABASE_URI"])
SESSION = sessionmaker(bind=ENGINE)

# scheduler
SCHEDULER = BackgroundScheduler(
    daemon=True,
    job_defaults={'misfire_grace_time': 300},
)
SCHEDULER.start()

# get logger
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)
SCHEDULER_LOGGER = logging.getLogger('apscheduler')
SCHEDULER_LOGGER.setLevel(logging.DEBUG)

# create file handler
FILE_HANDLER = logging.FileHandler('output.log')
FILE_HANDLER.setLevel(logging.DEBUG)

# create console handler
STREAM_HANDLER = logging.StreamHandler()
STREAM_HANDLER.setLevel(logging.INFO)

# create formatter and add it to the handlers
FORMATTER = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
STREAM_HANDLER.setFormatter(FORMATTER)
FILE_HANDLER.setFormatter(FORMATTER)

# add the handlers to logger
LOGGER.addHandler(STREAM_HANDLER)
LOGGER.addHandler(FILE_HANDLER)
SCHEDULER_LOGGER.addHandler(STREAM_HANDLER)
SCHEDULER_LOGGER.addHandler(FILE_HANDLER)

# api
BASE_URL = os.environ["API_URL"]
HEADERS = {
    'Authorization': os.environ["AUTHORIZATION"]
}

RESOURCE_IDS = {
    0: 'gold',
    3: 'oil',
    4: 'ore',
    11: 'uranium',
    15: 'diamond',
}

RESOURCE_NAMES = {
    'gold': 0,
    'oil': 3,
    'ore': 4,
    'uranium': 11,
    'diamond': 15,
    'diamonds': 15,
}

DEEP_EXPLORATION_MAX = {
    0: 637,
    3: 371,
    4: 356,
    11: 25,
    15: 27,
}

RESOURCE_MAX = {
    0: 2500,
    3: 600,
    4: 500,
    11: 60,
    15: 75,
}

KOEF_FACTOR = {
    0: 0.4,
    3: 0.65,
    4: 0.65,
    11: 0.75,
    15: 0.75,
}
