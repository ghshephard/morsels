from textwrap import dedent
import re
def unwrap_lines(lines):
    return re.sub("(?<!\n)(?<=.) ?(?<!  )\n(?!\n)(?=.)"," ",lines, flags=re.MULTILINE)


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


wrapped_text = dedent("""
            This is a line ends in two spaces  
            So this line doesn't wrap into it

            This line doesn't end in spaces
            So this line does wrap into it

            This line ends in 1 space 
            So this line does wrap
        """).lstrip()

print(unwrap_lines(wrapped_text))
