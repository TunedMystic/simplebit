from hashlib import sha1


def batch(iterable, n=1):
    """
    Split an iterable into constant-size chunks.
    Ref: https://stackoverflow.com/a/8290508
    """
    length = len(iterable)
    for ndx in range(0, length, n):
        yield iterable[ndx:min(ndx + n, length)]


def make_asset_hash(name, symbol):
    content = f'{name.lower()}:{symbol.lower()}'
    return sha1(content.encode('utf-8')).hexdigest()
