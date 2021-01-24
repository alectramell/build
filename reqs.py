import os
import sys
import subprocess

def install(package):

	subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# The following are samples, they can be removed..

install('wget')
install('keyboard')
