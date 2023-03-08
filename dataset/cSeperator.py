import os


curDirec = os.getcwd()
dataset = os.path.join(curDirec, "dataset.ttl")
cDataset = os.path.join(curDirec,"cCodeDataset.ttl")
javaDataset = os.path.join(curDirec,"javaCodeDataset.ttl")


# initialize variables to hold the text segments
startSegment = "<mb"
cEndSegment = ".c> ."
javaEndSegment = ".java> ."
segment_1 = ""
segment_2 = ""

with open(dataset, "r") as f:
    for line in f:
        if (line.startswith(startSegment) & line.endswith(cEndSegment)):
            # add segment 1 to the C Output file
            with open(cDataset, "a") as f1:
                f1.write(segment_1 + "\n")
            segment_1 = ""

        elif (line.startswith(startSegment) & line.endswith(javaEndSegment)):
            # add segment 2 to the Java Output output file
            with open(javaDataset, "a") as f2:
                f2.write(segment_2 + "\n")
            segment_2 = ""

        else:
            # add line to the appropriate segment
            if segment_1:
                segment_1 += line
            else:
                segment_2 += line

# grabs the final part segment of code
with open(cDataset, "a") as f1, open(javaDataset, "a") as f2:
    f1.write(segment_1)
    f2.write(segment_2)