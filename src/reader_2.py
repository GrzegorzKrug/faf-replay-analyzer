import base64
import json
import zlib
import zstd

import fafreplay
from fafreplay import Parser, commands

parser = Parser(
        # Skip all commands except the ones defined here
        # commands=[
        #         commands.Advance,  # For the tick counter
        #         commands.VerifyChecksum,  # For desync detection
        # ],
        commands=range(commands.MAX + 1),
        # Throw away commands right after we parse them. Setting this to `True` will
        # significantly increase the parse time.
        save_commands=True,
        limit=None,
        stop_on_desync=True,
)


def get_replay_bytes(path):
    with open(path, "rb") as f:
        header = json.loads(f.readline().decode())
        buf = f.read()
        version = header.get("version", 1)

        if version == 1:
            # print("Version 1")
            decoded = base64.decodebytes(buf)
            decoded = decoded[4:]  # skip the decoded size
            extracted = zlib.decompress(decoded)
            return extracted
        elif version == 2:
            # print("Version 2")
            extracted = zstd.decompress(buf)
            return extracted


path = r'replays\14612289.fafreplay'
data = get_replay_bytes(path)
header, body = parser.parse(data).values()
# print(repl)
# mp = header['map']
# print(mp)

# print("HEADER")
# for key, it in header.items():
#     print(key, )
#     print(it)

cmds = set()
count = 0
for act in body['commands']:
    name = act['name']
    cmds.add(name)
    if "VerifyCheck" in name:
        continue
    count += 1
    print(act)
    if count > 1000:
        break
print(cmds)

# game = parser.parse_body(extracted)
# game = parser.parse_body(extracted)
# print(game)
# print(dir(game))

# print(dir(commands))
# help(game)
# help(parser)
