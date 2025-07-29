import logging
import sys

logging.basicConfig(level=logging.INFO)


def main():
    logging.info("flavor_sync placeholder executed with args: %s", sys.argv[1:])


if __name__ == "__main__":
    main()
