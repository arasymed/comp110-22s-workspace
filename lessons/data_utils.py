"""Some helpful utility functions for working with CSV files."""

from csv import DictReader
# there are many ways to know how to use it on google


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    
    # A variable, this is more nuance so we let python infer the type and we assign the result of opening the filename parameter.
    # The filename came in as a parameter
    # A second argument for the open function call is the string r, which is short for read, so we will read the filename from our disk
    # then a keyword parameter "encoding = utf8" as a parameter, there are lots of parameters for this open function. Don't worry about the details of this.
    # To know how to open a file in a programming language we just need to google it. 
    # Open a handle to the data file 
    file_handle = open(filename, "r", encoding="utf8")
    # We opened a file and now we want to read it. When we open a file we are using resources from operating system of computer.
    # When we open a file here, we need something that allows us to read each line of the CSV into a dictionary with python capabilities. 
    # So we use the CSV package of python, so we import (look above)
    # Prepare to read a data file as a csv rather than just strings. 
    csv_reader = DictReader(file_handle)
    # Here we are setting our csv reader to be a new dictionary reader and we are giving it a file.
    # We give it a file, so that from this file handle set up a dictionary reader that will allow us to read the data into our program row by row.
    # We also need to close it once we stop reading it, called to the close method of the file. Close to free its resources.
    # csv_reader does not have a type but hover over it and we can see that the type is str. No need to worry about this. Reference this details on google.
    # Now that we have this reader we can loop through each of the rows:
    # row is now going to be assign a dict where the key is the colum name and the value is the value for each row.
    # We want to append that to the result table.
    # Read each row of the CSV line by line. 
    for row in csv_reader:
        result.append(row)
    # Close the file when we are done, to free its resources. 
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table: 
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result 