
import nbformat.current as nbf
import os

def convert(f):
    with open(f) as fpin:
        text = fpin.read()
    nbook = nbf.reads_py(text)
    jsonform = nbf.writes(nbook) + "\n"
    with open(os.path.splitext(fn)[0] + '.ipynb', "w") as fpout:
        fpout.write(jsonform)

directory = "/Users/swa/Desktop/Python-Machine-Learning-Cookbook/Chapter12"
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".py"):
        fn = os.path.join(directory, filename)
        convert(fn)
        continue
    else:
        continue