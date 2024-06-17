from itertools import islice
from typing import Generator, Iterable, List, TypeVar


T = TypeVar("T")

# Replace with itertools.batched in python 3.12
def batched(iterable: Iterable[T], n: int) -> Generator[List[T], None, None]:
    it = iter(iterable)
    while batch := list(islice(it, n)):
        yield batch
