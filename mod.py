import argparse

parser = argparse.ArgumentParser()

parser.add_argument("folder")
parser.add_argument("--csv")

args = parser.parse_args()

print("args.folder")
print("args.--csv")