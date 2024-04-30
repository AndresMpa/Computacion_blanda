import os
from pathlib import Path
from dotenv import load_dotenv
from os.path import join, dirname


project_path = Path(dirname(__file__))
env_file = join(project_path.parent.absolute(), ".env")

load_dotenv(env_file)

config = {
    "stage": os.environ.get("STAGE"),

    "dataset_dir": os.environ.get("DATASET_DIR"),
    "save_dir": os.environ.get("SAVE_DIR"),

    "web_site": os.environ.get("WEB_SITE"),
    "amount_of_pages": int(os.environ.get("AMOUNT_OF_PAGES")),

    "verbose": os.environ.get("VERBOSE") == "1",
}
