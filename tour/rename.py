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
    paths = (path for path in paths if is_process(path))
    for _, path in enumerate(paths, start=1):
        func(path, do=do)


def is_process(path: Path) -> bool:
    return (
        path.name != "main.go"
        and path.suffix == ".go"
        and path.parent.is_dir()
        and len(list(path.parent.iterdir())) > 1
    )


def func(path: Path, *, do: bool) -> None:
    i, name = path.with_suffix("").name.split("-", 1)
    i = int(i)
    new_path = path.parent.joinpath(f"{i}-{name}", "main.go")
    print(f"Propose\n    {path}\n--> {new_path}")

    if do:
        new_path.parent.mkdir()
        path.rename(new_path)
        print("...done")


if __name__ == "__main__":
    main()
