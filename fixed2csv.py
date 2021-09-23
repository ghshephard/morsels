def parse_fixed_width_file(fp, lst):
    for line in fp:
        yield list(line[start:end].rstrip() for start,end in lst)

with open('cars.txt') as txt_file:
    for row in parse_fixed_width_file(txt_file, [(0,4), (6,19), (24,37)]):
        print(row)
