import csv

CSV_INPUT = "bihar_final_data.csv"
CSV_OUTPUT = "bihar_cleaned_15JUL2013.csv"

FIELDS_TO_DROP = [
    "district",
    "village",
    "block",
    "phone_number",
    "username",
    "last_name",
    "subcentre",
    "village",
    "first_name",
    "form|meta|username",
    "default_phone_number",
]


def readcsvfile(fname):
    """
    Takes a CSV filename and returns a python object of the contents.
    Note: REQUIRES the first row be the headers for the remaining rows.
    """
    f = open( fname, 'r' )
    reader = csv.DictReader(f)
    return [row for row in reader]


def write_csv_file(fname, data):
    """
    Takes a filename to write to and an array of dictionaries. The 
    keys must all be the same.
    """
    f = open( fname, 'w')
    
    labels = ",".join(data[0].keys())
    f.write(labels + '\n')
    
    for d in data:
        out = [d[k].replace(',', '') for k in data[0].keys()]
        f.write(",".join(out) + '\n')
    f.close()


def clean_file(incsv):
    """docstring for clean_file"""
    out = []
    for i in incsv:
        for f in FIELDS_TO_DROP:
            if f in i:
                del i[f]
        out.append(i)
    return out


# Script start
if __name__ == "__main__":
    incsv = readcsvfile(CSV_INPUT)
    outcsv = clean_file(incsv)
    write_csv_file(CSV_OUTPUT, outcsv)