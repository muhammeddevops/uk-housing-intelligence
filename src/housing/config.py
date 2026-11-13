
import os
from pathlib import Path

from dotenv import load_dotenv

# Project directories
PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"


# Load environment variables
load_dotenv(PROJECT_ROOT / ".env")


# Database configuration
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", "5432"))
DB_NAME = os.getenv("DB_NAME", "uk_housing_intelligence")
DB_USER = os.getenv("DB_USER", "housing_user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
