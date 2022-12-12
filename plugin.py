import sys
import platform
import subprocess
import os


print(sys.argv[-1])
assert len(sys.argv) != 0
f = sys.argv[-1]
assert os.path.exists(f)
assert os.path.isfile(f)
assert f.endswith('.py')
command = f'python3 "{f}"'
renpyDir = os.path.join(os.path.dirname(f), 'renpy')
assert os.path.exists(renpyDir) and os.path.isdir(renpyDir)
if platform.system() == 'Linux' or platform.system() == 'Darwin':
    shPath = f.replace('.py', '.sh')
    if os.path.exists(shPath) and os.path.isfile(shPath):
        assert os.access(shPath, os.X_OK)
        command = shPath
    else:
        pass  # TODO: create sh file
elif platform.system() == 'Windows':
    exePath = f.replace('.py', '.exe')
    if os.path.exists(exePath) and os.path.isfile(exePath):
        command = exePath

print(command)
print(subprocess.run(f'{command}', shell=True))
