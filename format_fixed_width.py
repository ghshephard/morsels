from collections import defaultdict
def format_fixed_width_v1(rows, padding = 2, widths=None, alignments=None):

    align = {}
    maxleng=defaultdict(int)
    if widths:
        for i,w in enumerate(widths):
            maxleng[i] = w
    else:
        for row in rows:
            for i,col in enumerate(row):
                maxleng[i] = max([len(col), maxleng[i]])
    if alignments:
        for i,a in enumerate(alignments):
            align[i]=a
    else: 
        for c in range(len(maxleng)):
            align[c] = "L"

                
    ret=""
    for row in rows:
        for i,item in enumerate(row):
            if align[i] == "L":
                ret+=item+" "*(maxleng[i] - len(item)+padding)
            else:
                ret+=" "*(maxleng[i] - len(item))+item+"  "*padding

        ret =  ret.rstrip() + "\n"
    return ret.rstrip()   


def format_fixed_width(rows,widths=None,padding=2, alignments=None):

    
    if not widths:
        widths = [ max(len(cell) for cell in row) for row in zip(*rows)]
    if alignments:
         aligns = [ str.ljust if a=="L" else str.rjust for a in alignments ]
    else: 
        aligns = [ str.ljust for _ in range(len(widths))]
    ret=""
    for row in rows:
        for cell,clen,align in zip(row,widths,aligns):
            ret+=align(cell, clen)+padding*" "
        ret = ret.rstrip() + "\n"
    return ret.rstrip()


if __name__ == "__main__":
    print(format_fixed_width([['green', 'red'], ['blue', 'purple']]))
    print(format_fixed_width([["Hello"]]))
    print(format_fixed_width([["hi", "there"]]))
    print(format_fixed_width([["Jane"],["Mark"]]))
    rows = [["Jane", "", "Austen"], ["Samuel", "Langhorne", "Clemens"]]
    print(format_fixed_width(rows,widths=[10,15,20]))

    print(format_fixed_width(rows, alignments=['R', 'L', 'R']))