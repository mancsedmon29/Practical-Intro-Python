import shutil

name = "Edmon"

columns, lines = shutil.get_terminal_size()

for _ in range(lines):
    print(name * (columns // len(name)), end='')