from pathlib import Path
from argparse import ArgumentParser


def main() -> None:
    # parse args
    parser = ArgumentParser()
    parser.add_argument("--do", action="store_true")
    args = parser.parse_args()
    do: bool = args.do

    # main
    paths = sorted(Path.cwd().glob("**/*.go"))
    for _, path in enumerate(paths, start=1):
        new_path = func(path)
        print(f"Renaming\n  {path}\n> {new_path}")
        if do:
            path.rename(new_path)


def func(path: Path) -> Path:
    return path.with_name(path.name.replace("_", "-"))


if __name__ == "__main__":
    main()
