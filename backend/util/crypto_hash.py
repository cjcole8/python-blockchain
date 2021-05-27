import hashlib
import json


def crypto_hash(*args):
    """
    Return a sha-256 hash of the given args.
    """
    stringified_args = sorted(map(lambda data: json.dumps(data), args))
    joined_data = "".join(stringified_args)

    return hashlib.sha256(joined_data.encode("utf-8")).hexdigest()


def main():
    print(f"crypto_hash('foo'): {crypto_hash('sdlkfj')}")


if __name__ == "__main__":
    main()
