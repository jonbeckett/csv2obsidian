# csv2obsidian

I wrote this script largely for my own purposes, but thought the community might find use for it too. The script exports any CSV file into a collection of markdown files formatted for use in Obsidian - complete with YAML for each field value, for those using the dataview plugin.

Note that the files are named after the first column in the CSV. Also, where values have multiple lines, only the first line is picked up.

### Usage
```
python csv2obsidian.py <source_file> <output_directory> <tag>
```

### Example
```
python csv2obsidian.py c:\things.csv c:\vault\things #thing
```
