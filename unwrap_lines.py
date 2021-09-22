from textwrap import dedent
import re


NOLINEBREAK = re.compile(r'''
   (?<!\n])        # Preserve multiple linebreaks.
   (?<=.)[ ]?         # Must be *something* before the \n - But erase single trailling space
   (?<![ ]{2})          # But don't split line if it ends in two spaces.
   \n               # Good Grief - this is the actual thing we're replacing
   (?!\n|[0-9-])    # Next line can't be a new line, or bullet/numberd list.
   (?=.)            # And it shouldn't be the very last thing.
''', re.VERBOSE)        


def unwrap_lines(lines):
   return NOLINEBREAK.sub(" ",lines)


wrapped_text = """\
This is some line wrapped
text. The words have been
manually wrapped.

A second paragraph won't
be wrapped into the first."""


wrapped_text = """
This is paragraph number
one.



This is number two.
"""

wrapped_text = dedent("""
            This is a line
            that is followed by another line


            There are 2 blank lines before this
            And there was 1 before this



            And three before this one
        """).lstrip()




wrapped_text = text = """
To do:
1. Grocery shopping
2. Water the cat
3. Take out the laundry
4. Wash the television

Grocery list
- pistachio nut milk
- avocado butter
- fermented chocolate
"""
wrapped_text = dedent("""
            This is a line ends in two spaces  
            So this line doesn't wrap into it

            This line doesn't end in spaces
            So this line does wrap into it

            This line ends in 1 space 
            So this line does wrap
        """).lstrip()

print(unwrap_lines(wrapped_text).replace(" "," "))
