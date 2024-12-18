

"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""
import os


IDENTICAL = -1

def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    len1 = len(line1)
    len2 = len(line2)
    for idx in range(max(len1,len2)):
        if idx < min(len1 , len2) and line1[idx] != line2[idx]:
            return idx
        elif idx >= min(len1,len2):
            return idx
    return  IDENTICAL

line_1 ="single i line string"
Line_2 = "single line string"

singleline_diff(line_1,Line_2)



def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    if '\r' in line1 or '\r' in line2:
        return ""

    if '\n' in line1 or '\n' in line2:
        return ""

    if idx > min(len(line1), len(line2)) or idx < 0:
        return ""

    diff_result = "{0}\n{1}\n{2}\n" .format(line1, "=" * idx + "^", line2)
    return diff_result



def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    len_1 = len(lines1)
    len_2 = len(lines2)

    used_range = min(len_1, len_2)

    if not lines1 and not lines2:
        return (IDENTICAL, IDENTICAL)
    elif not lines1 or not lines2:
        return (0, 0)
    else:
        pass

    for line_number in range(used_range):
        diff_idx = singleline_diff(lines1[line_number], lines2[line_number])
        if diff_idx == IDENTICAL and line_number == used_range - 1 and len_1 == len_2:
            return (IDENTICAL, IDENTICAL)
        elif diff_idx == IDENTICAL and line_number == used_range -1:
            return (used_range, 0)
        elif diff_idx == IDENTICAL:
            continue
        else:
            return(line_number, diff_idx)




def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    open_file = open(filename,"rt")

    file_text = open_file.read().splitlines()

    return file_text




def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    file1 = get_file_lines(filename1)
    file2 = get_file_lines(filename2)

    # check if one of the file is empty 
    if os.stat(filename1).st_size == 0 and os.stat(filename2).st_size == 0:
        return "No differences\n"
    elif os.stat(filename1).st_size == 0:
        return "Line 0:\n" + "{0}\n{1}\n{2}\n" .format("", "^", file2[0])
    elif os.stat(filename2).st_size == 0:
        return "Line 0:\n" + "{0}\n{1}\n{2}\n" .format(file1[0], "^", "")
    else:
        pass

    # find the first difference between the two lists
    diff = multiline_diff(file1, file2)

    item, idx = diff

    if item == idx == -1:
        return "No differences\n"
    else:
        result = "Line " + str(item) + ":\n" + singleline_diff_format(file1[item], file2[item], idx)
        return result