import re, sys
from datetime import datetime

if (len(sys.argv) - 1) > 0:
  fileName = sys.argv[1]
  captions = open(fileName, "r")

  transcription = ""

  for line in captions:
    if re.search("^\d\d:\d\d:\d\d\s", line) is not None:
      trimmedLine = re.sub("^\d\d:\d\d:\d\d\s", "", line)
      transcription += trimmedLine.strip("\n")
    else:
      transcription += ("\n\n" + line.strip("\n"))

  now = datetime.now()
  newFileName = "formatted-transcription-" + now.strftime("%m-%d-%Y-%H-%M-%S") + ".txt"
  newFile = open(newFileName, "w")
  newFile.write(transcription)
  newFile.close()

  print(f"The formatted transcript has been saved in this folder as {newFileName}.")

else:
  print("Please provide a file to convert. The command should be: python3 caption-convert.py your-file-name.txt")