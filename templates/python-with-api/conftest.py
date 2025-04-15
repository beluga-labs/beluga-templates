import sys
from pathlib import Path

# This is a workaround to add the parent directory to the sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))
