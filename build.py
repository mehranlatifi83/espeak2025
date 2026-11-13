"""Build espeak2025-<version>.nvda-addon from the addon folder."""

import os
import re
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
ADDON = os.path.join(HERE, "addon")


def main():
	manifest = open(os.path.join(ADDON, "manifest.ini"), encoding="utf-8").read()
	version = re.search(r"^version\s*=\s*(\S+)", manifest, re.M).group(1)
	out = os.path.join(HERE, f"espeak2025-{version}.nvda-addon")
	with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
		for root, dirs, files in os.walk(ADDON):
			dirs[:] = [d for d in dirs if d != "__pycache__"]
			for name in files:
				full = os.path.join(root, name)
				z.write(full, os.path.relpath(full, ADDON))
	print(out)


if __name__ == "__main__":
	main()
