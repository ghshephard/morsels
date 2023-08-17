import tempfile
import os

class make_file:
    def __init__(self,contents):
        self.contents=contents

    def __enter__(self):
        fp = open(tempfile.NamedTemporaryFile().name,'wt')
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

if __name__ == "__main__":
    main()
