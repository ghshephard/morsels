from textwrap import dedent
import re
def unwrap_lines(lines):
    return re.sub("(?<!\n)(?<=.)\n(?!\n)(?=.)"," ",lines, flags=re.MULTILINE)


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

print(unwrap_lines(wrapped_text))
