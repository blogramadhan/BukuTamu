import os
from datetime import datetime

import pytz
from fasthtml.common import *
from supabase import create_client, Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Constants for input character limits and timestamp format
MAX_NAME_CHAR = 15
MAX_MESSAGE_CHAR = 50
TIMESTAMP_FMT = "%Y-%m-%d %I:%M:%S %p CET"

# Initialize Supabase client
supabase: Client = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))