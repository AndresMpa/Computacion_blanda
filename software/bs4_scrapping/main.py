import time
from util.env_vars import config
from stages.main import select_stage


if __name__ == '__main__':
    timestamp = str(time.time())

    stage = select_stage(config["stage"])

    if stage == "Error":
        raise Exception(
            "Hay un error en la definicion del estados 'stage', revise el archivo .env")

    stage(timestamp)
