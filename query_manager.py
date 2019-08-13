from pathlib import Path
import logging
import glob
import csv


class QueryManager:
    def __init__(self):
        self._logger = logging.getLogger("QueryManager")
        self._logger.info("Initializing Query Manager")
        self._files = self.load_file_list()

    def load_file_list(self):
        # Following code cribbed from: https://stackoverflow.com/questions/53032118/reading-multiple-files-containing-multiple-csvs

        p = Path.cwd() / "sources"

        files = []
        file_extensions = [".csv"]
        for file_or_directory in p.iterdir():
            if (
                file_or_directory.is_file()
                and "".join(file_or_directory.suffixes).lower() in file_extensions
            ):
                files.append(file_or_directory)
            elif file_or_directory.is_dir():
                files.extend(
                    [
                        x
                        for x in file_or_directory.iterdir()
                        if "".join(x.suffixes).lower() in file_extensions
                    ]
                )
        self._logger.debug("About to print files")
        self._logger.debug(f"{files}")
        self._logger.debug("Finished printing files")
        pass
        return files

    @property
    def files(self):
        return self._files

    def scan_files(self):
        for fl in self.files:
            with fl.open(mode="r") as f:
                reader = csv.reader(f)
                for row in reader:
                    logger.debug(row)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%I:%M:%S %p",
    )
    logger = logging.getLogger("QueryManager")

    lh_console = logging.StreamHandler()
    lh_console.setLevel(logging.DEBUG)
    # lh_console.setFormatter(
    #     logging.Formatter(
    #         fmt="%(asctime)s | %(name)s | %(levelname)s || %(message)s",
    #         datefmt="%H:%M:%S",
    #     )
    # )
    # logger.addHandler(lh_console)

    lh_file = logging.FileHandler(Path.cwd() / "logs" / "query_manager.log")
    lh_file.setLevel(logging.INFO)
    lh_file.setFormatter(
        logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%d-%b-%y %H:%M:%S",
        )
    )
    logger.addHandler(lh_file)

    logger.info("Starting 'query_manager'")
    qm = QueryManager()
    logger.info("'query_manager' loaded\n")
    qm.scan_files()

    pass
