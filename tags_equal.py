import re, shlex
def get_tags(t1):
    rdic={}
    for item in [x.upper() for x in shlex.split(t1)]:
        k,*_,v=item.partition("=")
        if not k in rdic:
            rdic[k]=v
    return rdic


def tags_equal(t1, t2):
    return get_tags(t1[1:-1]) == get_tags(t2[1:-1])
    

if __name__  == "__main__":
    assert tags_equal("<img src=cats.jpg height=40>", "<IMG SRC=cats.jpg height=40>") == True
    assert tags_equal("<img src=dogs.jpg width=99>", "<img src=dogs.jpg width=20>") == False
    assert tags_equal("<p>", "<P>") == True
    assert tags_equal("<b>", "<p>") == False
    assert tags_equal("<img height=200 width=400>", "<img width=400 height=200>")
    assert tags_equal("<LABEL FOR=id_email for=id_username>", "<LABEL FOR=id_email>") == True
    assert tags_equal("<LABEL FOR=id_email for=id_username>", "<LABEL FOR=id_username>") == False
