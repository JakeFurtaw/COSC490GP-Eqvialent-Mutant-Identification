import os


curDirec = os.getcwd()
dataset = os.path.join(curDirec, "dataset.ttl")
cDataset = os.path.join(curDirec,"cCodeDataset.ttl")
javaDataset = os.path.join(curDirec,"javaCodeDataset.ttl")


# initialize variables to hold the text segments
startSegment = "<mb"
cEndSegment = ".c> ."
javaEndSegment = ".java> ."
segment = ""

with open(dataset, "r") as f:
    for line in f:
        if line.startswith(startSegment):
            segment = segment + line
        elif cEndSegment in line:
            segment = segment + line
            with open(cDataset,"a") as f1:
                f1.write(segment)
            segment = ""
        elif javaEndSegment in line:
            segment = segment + line
            with open(javaDataset,"a") as f2:
                f2.write(segment)
            segment = ""
        else:
            segment = segment + line
            

