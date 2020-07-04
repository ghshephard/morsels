def csv_columns(f, headers=None, missing=None):
    import csv
    from collections import defaultdict
    csvdic = defaultdict(list)
    reader = csv.DictReader(f, restval=missing, fieldnames=headers)
    for row in reader:
        for k, v in row.items():
            csvdic[k].append(v)
    return(csvdic)


rep = csv_columns(open('foo.csv'), headers=['HEAD1','HEAD2'], missing=0)
print(rep)
