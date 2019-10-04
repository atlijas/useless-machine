from pathlib import Path
import __main__ as main
P = Path(main.__file__)
P.unlink()
print('Self deleted:', main.__file__)
