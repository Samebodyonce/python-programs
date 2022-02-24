import argparse
import json
import os
import tempfile


def read_data(st_path):
    if not os.path.exists(st_path):
        return {}

    with open(st_path, 'r') as file:
        raw_data = file.read()
        if raw_data:
            return json.loads(raw_data)
        return {}


def write_data(st_path, data):
    with open(st_path, 'w') as f:
        f.write(json.dumps(data))


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', help='Key')
    parser.add_argument('--val', help='Value')
    return parser.parse_args()


def put(st_path, key, value):
    data = read_data(st_path)
    data[key] = data.get(key, list())
    data[key].append(value)
    write_data(st_path, data)


def get(st_path, key):
    data = read_data(st_path)
    return data.get(key, [])


def main(st_path):
    args = parse()

    if args.key and args.val:
        put(st_path, args.key, args.val)
    elif args.key:
        print(*get(st_path, args.key), sep=', ')
    else:
        print('The program is called with invalid parameters.')


if __name__ == '__main__':
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    main(st_path)
