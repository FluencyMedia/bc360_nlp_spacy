from query_proc import logger


class QueryManager:
    def __init__(self, query):
        logger.debug("Loading Query Manager")
        self._query_raw = query
        logger.debug("Loaded Query Manager")

    class TokenManager:
        __slots__ = [
            "token_raw",
            "token_normalized",
            "token_text",
            "token_lemma",
            "token_lemma_",
            "token_pos",
            "token_pos_",
            "token_tag",
            "token_tag_",
            "token_tag_",
            "token_dep",
            "token_dep_",
            "token_shape",
            "token_shape_",
            "token_is_alpha",
            "token_is_stop",
        ]

        token_raw: str
        token_normalized: str
        token_text: str
        token_lemma: int
        token_lemma_: str
        token_pos: int
        token_pos_: str
        token_tag: int
        token_tag_: str
        token_dep: int
        token_dep_: str
        token_shape: int
        token_shape_: str
        token_is_alpha: bool
        token_is_stop: bool


if __name__ == "__main__":
    qm = QueryManager("test query")
    pass
