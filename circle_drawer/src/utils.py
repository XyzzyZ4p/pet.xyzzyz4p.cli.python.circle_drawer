def check_pairs(*args):
    for pair in args:
        if pair[0] != pair[1]:
            return False
    return True


__all__ = ('check_pairs',)
