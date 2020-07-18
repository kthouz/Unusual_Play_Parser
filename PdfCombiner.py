# Import necessary modules
import os, PyPDF2 as pypdf, logging
from pathlib import Path
logging.basicConfig(level=logging.DEBUG)
# logging.disable(logging.DEBUG)

folders = []
folderBase = "/Users/X/Uncompressed"
os.chdir(folderBase)

for name in os.listdir():
    if os.path.isdir(name):
        folders.append(name)

folders.sort()

logging.debug("Folders:")

for name in folders:
    logging.debug(name)

logging.debug("-------------------")

# The folder name will be the name of the resulting pdf
# Open folders
for name in folders:
    os.chdir(folderBase + '/' + name)
    files = {"FileName": [], "PdfObject": [], "BookNumber": [], "StartPage": [], "EndPage": [], "EvenOdd": []}

    for file in os.listdir():
        if os.path.isfile(file) and file.endswith(".pdf"):
            files["FileName"].append(file)

    if name == "YellowPacket":  # Files are organized differently, needs special care

        writer = pypdf.PdfFileWriter()

        for file in ["YellowPacket.pdf", "YellowPacket0001.pdf", "YellowPacket0002.pdf", "YellowPacket0003.pdf", "YellowPacket0004.pdf"]:
            pdf_file = open(file, "rb")
            logging.debug("Working on packet " + str(file))
            reader = pypdf.PdfFileReader(file)
            for pageNum in range(reader.numPages):
                pageNum = reader.getPage(pageNum)
                writer.addPage(pageNum)

        outputFile = open("/Users/X/Uncompressed/Final/YellowFolder.pdf", "wb")
        writer.write(outputFile)
        outputFile.close()
        pdf_file.close()

    else:
        even = [[], [], []]
        odd = [[], [], []]
        count = 0

        for file in os.listdir(folderBase + '/' + name):
            if "_O" in file:
                newfile = file[:(file.index("_E") + 2)] + ".pdf"
                newfile = newfile.replace('-', '_')
                newfile = newfile.replace("TO", "0")
                os.rename(file, newfile)
                odd[0].append(newfile)
                split = odd[0][count].split('_')

                odd[1].append(int(split[1]))
                odd[2].append(int(split[2]))

            elif "_E" in file:
                newfile = file[:(file.index("_E") + 2)] + ".pdf"
                newfile = newfile.replace('-', '_')
                newfile = newfile.replace("TO", "0")
                os.rename(file, newfile)
                even[0].append(newfile)
                split = even[0][count].split('_')

                if split[1] == "TO":
                    split[1] = 0

                even[1].append(int(split[1]))
                even[2].append(int(split[2]))

            count += 1

            # odd["StartPage"].sort()
            # odd["StartPage"].index()
    print("\n-----------------------------------------------------------------")
