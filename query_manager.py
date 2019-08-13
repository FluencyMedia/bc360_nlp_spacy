from pathlib import Path
import logging
import glob
import csv
import os


# Following generators cribbed from: https://realpython.com/introduction-to-python-generators/
def generate_filenames():
    """
    generates a sequence of opened files
    matching a specific extension
    """
    for dir_path, dir_names, file_names in os.walk("sources/"):
        for file_name in file_names:
            if file_name.endswith(".csv"):
                yield open(os.path.join(dir_path, file_name))


def cat_files(files):
    """
    takes in an iterable of filenames
    """
    for fname in files:
        for line in fname:
            yield line


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%I:%M:%S %p",
    )
    logger = logging.getLogger("QueryManager")

    lh_file = logging.FileHandler(Path.cwd() / "logs" / "query_manager.log")
    lh_file.setLevel(logging.INFO)
    lh_file.setFormatter(
        logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%d-%b-%y %H:%M:%S",
        )
    )
    logger.addHandler(lh_file)

    csv_files = generate_filenames()
    csv_file = cat_files(csv_files)
    # lines = grep_files(csv_file, 'a')
    for line in csv_file:
        logger.debug(line)

    pass
