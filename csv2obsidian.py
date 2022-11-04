import csv
import sys
import os

# Converts a CSV file to a collection of markdown files

if (len(sys.argv)!=4):
    print("\ncsv2obsidian.py - by Jonathan Beckett\n\npython csv2obsidian.py <source_file> <output_directory> <tag>\n\nExample : python csv2obsidian.py file.csv c:\\my\\vault\\subfolder #foo\n\n")
    sys.exit(0)

source_file = sys.argv[1]
output_path = sys.argv[2]
tag = sys.argv[3]


with open(source_file,newline="") as csvfile:
    csvreader = csv.DictReader(csvfile,delimiter=",",quotechar="\"")
    for row in csvreader:

        print("Processing " + row[csvreader.fieldnames[0]])

        # build the yaml
        output_text = "---\n"
        for fieldname in csvreader.fieldnames:
            if (row[fieldname]):
                output_text += fieldname.replace(" ","").lower() + ": " + "".join(row[fieldname].split("\n")[0]) + "\n"
        output_text += "---\n"

        # build the human readable version
        for fieldname in csvreader.fieldnames:
            if(row[fieldname]):
                output_text += "\n### " + fieldname + "\n"
                output_text += row[fieldname] + "\n"

        # append the tag on the end
        output_text += "\n" + tag + "\n"
        
        # create an output file name from the first column
        file_path = os.path.join(output_path,row[csvreader.fieldnames[0]]) + ".md"       
        print(" > " + file_path)
        
        # output to a file        
        output_file_path = file_path
        output_file = open(output_file_path, 'wb')
        output_file.write(bytes(output_text,'utf-8'))
        output_file.close()
