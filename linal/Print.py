

def Print(mask: int,
        explain: int,
        *values: object,
        sep: str | None = " ",
        end: str | None = "\n",
        file = None,
        flush = False,
) -> None:
    if Mask(mask, explain):
        print(*values, sep=sep, end=end, file=file, flush=flush)


def Mask(mask: int, explain: int) -> bool:
    return 0 < mask & explain <= 3


def CheckFlag(mask: int, explain: int) -> bool:
    return bool(mask & explain)


