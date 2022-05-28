from pathlib import Path


for path in sorted(Path("tour").iterdir()):
    if path.suffix == ".go":
        try:
            i, name = path.name.split("_", 1)
        except ValueError:
            print(f"Skipping {path}")
        else:
            i = int(i)
            new_name = f"{i:02}_{name}"
            new_path = path.with_name(new_name)
            print(f"Renaming\n  {path}\n> {new_path}")
            # path.rename(new_path)
