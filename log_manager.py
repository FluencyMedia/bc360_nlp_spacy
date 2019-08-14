from pathlib import Path
import logging


def load_logger():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%I:%M:%S %p",
    )
    new_logger = logging.getLogger("QueryManager")

    lh_file = logging.FileHandler(Path.cwd() / "logs" / "query_manager.log")
    lh_file.setLevel(logging.INFO)
    lh_file.setFormatter(
        logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%d-%b-%y %H:%M:%S",
        )
    )
    new_logger.addHandler(lh_file)
    return new_logger


logger = load_logger()
