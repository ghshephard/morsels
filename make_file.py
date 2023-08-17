import tempfile
import os

class make_file:
    def __init__(self,contents="", encoding="utf-8",mode="wt",newline=None,directory=None):
        self.contents=contents
        self.dir=directory
        self.encoding=encoding
        self.mode=mode
        self.newline=newline

    def __enter__(self):
        if not "b" in self.mode:
            args={"encoding":self.encoding, "mode":self.mode, "newline":self.newline} 
        else:
            args={"mode":self.mode}
        fp = open(tempfile.NamedTemporaryFile(dir=self.dir).name,  **args)
        fp.write(self.contents)   
        self.nam = fp.name    
        fp.close()
        return self.nam
    
    def __exit__(self, exception_type, exception, traceback):
        os.remove(self.nam)


def main(): 
    with make_file("TESTING") as filename:
        print ("FILENAME: ",filename)
        open(filename, mode='wt').write('hello!')
        assert(open(filename,mode="rt").read()=="hello!")
        
        print(open(filename).read())
        print(f'{filename} READ.')
        print("Tests all Passed.")
    with make_file(contents="STUFF",directory="/home/gshephard/morsels") as myfile:
        print("Next: ",myfile)
        fp=open(myfile, mode="at").write('More')
        print(open(myfile).read())

    with make_file(b"bytes!", mode='wb') as filename:
        print(open(filename).read())
    
    with make_file("hello!", encoding='utf-16-le') as filename:
        print(open(filename, encoding='utf-16-be').read())

if __name__ == "__main__":
    main()
