from pathlib import Path
import __main__ as main
P = Path(main.__file__)

if __name__ == '__main__':
    P.unlink()
    print('Self deleted:', main.__file__)
