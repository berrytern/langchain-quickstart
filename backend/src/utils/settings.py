import dotenv
import os

dotenv.load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PORT = int(os.getenv("PORT", "8000"))

if OPENAI_API_KEY is None:
    raise BaseException("need to setup OPENAI_API_KEY environment variable")