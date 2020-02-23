import os
from dotenv import load_dotenv

load_dotenv()

SOME_EXAMPLE_ENV_VAR = os.getenv("SOME_EXAMPLE_ENV_VAR", "something")