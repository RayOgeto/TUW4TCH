import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get your API key from environment variables
TMDB_API_KEY = os.getenv('TMDB_API_KEY')
