import os
import pathlib

parent = pathlib.Path("./extra")
filenames = list(filter(lambda item: item.is_file(), parent.rglob("*")))
# filenames = os.listdir("extra")
print(filenames)