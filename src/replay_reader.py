import numpy as np

from fafreplay import Parser, commands

parser = Parser(
        # Skip all commands except the ones defined here
        commands=[
                commands.Advance,  # For the tick counter
                commands.VerifyChecksum,  # For desync detection
        ],
        # Throw away commands right after we parse them. Setting this to `True` will
        # significantly increase the parse time.
        save_commands=False
)
# Or create a parser with default arguments (turn off save_commands though)
# parser = Parser(save_commands=False)

# Read replay to a `bytes` object
with open("11490480.fafreplay", "rt") as f:
    input_data = f.read()

input_list = input_data.split('\n')
header = input_list[0]
data = input_list[1].encode()

from fafreplay import body_offset, body_ticks

ticks = body_ticks(data)
print("Game time:", timedelta(milliseconds=ticks * 100))
