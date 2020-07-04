def csv_columns(f, headers=None):
    import csv
    from collections import defaultdict
    csvdic = defaultdict(list)
    reader = csv.DictReader(f)
    if headers is None:
        headers = reader.fieldnames
    else:
        csvdic = {k: [h] for k, h in zip(headers, reader.fieldnames)}
    for row in reader:
        for k, v in zip(headers, row.values()):
            csvdic[k].append(v)
    return(csvdic)


rep = csv_columns(open('foo.csv'), headers=['HEAD1','HEAD2'])
print(rep)
