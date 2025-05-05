import argparse
from sort_answer import sort


def main():
    parser = argparse.ArgumentParser(description=" program.")
    parser.add_argument("--width", type=int, help="width")
    parser.add_argument("--height", type=int, help="height")
    parser.add_argument("--length", type=int, help="length")
    parser.add_argument("--mass", type=int, help="mass")
    args = parser.parse_args()
    result: str = sort(args.width, args.height, args.length, args.width)
    print(f"the package is {result}")


if __name__ == "__main__":
    main()
