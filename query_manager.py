from pathlib import Path
import logging
import csv
import os
import spacy
from spacy import displacy


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
            yield line.rstrip()


def proc_queries(queries):
    """
    Serially processes queries
    """

    logger.debug("Clearing '\\renders\\'")
    for dir_path, dir_names, file_names in os.walk("renders/"):
        for file_name in file_names:
            os.remove(os.path.join(dir_path, file_name))
            logger.debug(f"Removed file: {file_name}")

    nlp = spacy.load("en_core_web_sm")
    i = 1

    for current_query in queries:
        print()
        logger.info(f"QUERY: {current_query} [{len(current_query)}]")
        q = nlp(current_query)
        svg = displacy.render(q, style="dep", page=False)
        fname = f"{i:08d} - {'_'.join([w.text for w in q if not w.is_punct])}" ".html"
        # f = format(i, "08d") + "-".join([w.text for w in q if not w.is_punct]) + ".html"
        output_path = Path.cwd().joinpath("renders") / fname
        with output_path.open("w", encoding="utf-8") as f:
            f.write(svg)
        # displacy.serve(q, style="ent")
        logger.info(f"Text | Lemma | PoS | Label | Tag | Dep_ | Shape | Alpha? | Stop?")
        for token in q:
            logger.info(
                f"{token.text} | {token.lemma_} | {token.pos_} | {token} | {token.tag_} | {token.dep_} | {token.shape_} | {token.is_alpha} | {token.is_stop}"
            )
        i += 1
        breakpoint()


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

    query_files = generate_filenames()
    q_file = cat_files(query_files)
    # lines = grep_files(csv_file, 'a')
    proc_queries(q_file)

    pass
