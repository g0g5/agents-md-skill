#!/usr/bin/env python3
import shutil
import os
from pathlib import Path

src = Path(__file__).resolve().parent / "skills" / "agents-md"
dst = Path.home() / ".claude" / "skills" / "agents-md"

if dst.exists():
    shutil.rmtree(dst)

shutil.copytree(src, dst)
print(f"Installed to {dst}")
