import logging
import sys

logging.basicConfig(level=logging.INFO)


def main():
    user_id = sys.argv[1] if len(sys.argv) > 1 else None
    base_flavor = sys.argv[2] if len(sys.argv) > 2 else None
    logging.info(
        "reflex_session placeholder executed for user %s with base flavor %s",
        user_id,
        base_flavor,
    )


if __name__ == "__main__":
    main()
