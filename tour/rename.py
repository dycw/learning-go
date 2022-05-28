from pathlib import Path


PATHS = sorted(Path('tour').iterdir())
PATHS = (path for path in PATHS if path.suffix == ".go")
for i, path in enumerate(PATHS, start=1):
    cnt, name = path.name.split("_", 1)
    new_path = path.parent.joinpath('2-basics', f"{i:02}_{name}")
    print(f"Renaming\n  {path}\n> {new_path}")
    # path.rename(new_path)
