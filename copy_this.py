import sys

test_dir = r"file path"
systemPath = sys.path
if test_dir not in systemPath:
    systemPath.append(test_dir)
    
from importlib import reload
import running
reload(running)
running.run()