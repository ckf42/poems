import os
import hashlib

def hash_and_write(fpath):
    wfpath = fpath + '.md5'
    if os.path.isfile(wfpath):
        print(f"{wfpath} already exists")
        return
    hasher = hashlib.md5()
    with open(fpath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    hash_result = hasher.hexdigest()
    print(f"{hasher.name.upper()}:\t{hash_result}")
    with open(wfpath, "wt") as f:
        f.write(f"{hash_result}\t{os.path.getsize(fpath)} bytes")

currentDir = os.getcwd()
allPoems = [fname for fname in os.listdir(currentDir) if fname.startswith('poem') and fname.endswith('.txt')]
for fname in allPoems:
    fpath = os.path.join(currentDir, fname)
    print(f"{fname}")
    hash_and_write(fpath)
print("Done")

