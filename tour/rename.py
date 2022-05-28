from pathlib import Path
from contextlib import suppress


for path in sorted(Path("tour").iterdir()):
    with suppress(ValueError):
        i, name = path.name.split("_", 1)
        i = int(i)
        new_name = f"{i:02}_{name}"
        new_path = path.with_name(new_name)
        print(path, name, new_name, new_path)
        # path.rename(new_path)
