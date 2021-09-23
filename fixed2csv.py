from argparse import ArgumentParser
import csv

def parse_fixed_width_file(fp, lst):
    for line in fp:
        yield list(line[start:end].rstrip() for start,end in lst)

def parse_columns(cols):
    return [ tuple([int(c) for c in col.split(':')]) for col in cols.split(",")]

def main(lst):
    parser = ArgumentParser()
    parser.add_argument('--cols')
    parser.add_argument('infile')
    parser.add_argument('outfile')
    args = parser.parse_args(lst)
    cols = parse_columns(args.cols)
    with open(args.outfile,'w') as outfile:
        csvwriter = csv.writer(outfile, delimiter =',')
        with open(args.infile,'r') as infile:
            for row  in parse_fixed_width_file(infile, cols):
                csvwriter.writerow(row)






with open('cars.txt') as txt_file:
    for row in parse_fixed_width_file(txt_file, [(0,4), (6,19), (24,37)]):
        print(row)

print(parse_columns('0:4,6:19,24:37'))

columns = '0:4,6:19,24:37'

main(['--cols=0:4,6:19,24:37', 'cars.txt', 'cars.csv'])
print(open('cars.csv').read())

main(['--cols=0:2,4:19,21:44,46:50', 'bands.txt','bands.csv'])
print(open('bands.csv').read())