import tempfile
import os

class make_file:
    def __init__(self,contents="", directory=None):
        self.contents=contents
        self.dir=directory

    def __enter__(self):
        fp = open(tempfile.NamedTemporaryFile(dir=self.dir).name,'wt')
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
if __name__ == "__main__":
    main()
