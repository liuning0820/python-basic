import hashlib
import sys


def object_path(content):
    header = f"blob {len(content)}\0"
    data = header.encode() + content
    print(data)
    digest = hashlib.sha1(data).hexdigest()
    print(digest)
    return f".git/objects/{digest[:2]}/{digest[2:]}"


with open(sys.argv[1], "rb") as f:
    print(object_path(f.read()))


# python3 find-git-object.py ./get-ip.py