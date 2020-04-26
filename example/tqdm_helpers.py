from datetime import datetime, timedelta
from time import sleep

from tqdm import tqdm

DEFAULT_BAR_FORMAT = "{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}{postfix}, EST={est}]"


class TqdmExtraFormat(tqdm):
    @property
    def format_dict(self):
        d = super(TqdmExtraFormat, self).format_dict

        est_seconds = (d["total"] - d["n"]) * (d["elapsed"] / max(d["n"], 1))
        est = datetime.now() + timedelta(seconds=est_seconds)
        d.update(est=est.strftime("%H:%M:%S") if d["n"] > 0 else "?")

        return d


def trange(*args, **kwargs):
    if "bar_format" not in kwargs:
        kwargs.update(bar_format=DEFAULT_BAR_FORMAT)
    return TqdmExtraFormat(range(*args), **kwargs)


if __name__ == "__main__":
    from random import choice

    for i in trange(9):
        sleep(choice([1, 2]))
