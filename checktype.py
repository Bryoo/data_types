

def data_type(data):
    """Takes one input and returns data value in respect to data type of the input  """
    input_type = type(data)
    # return (data is None)

    if data is None:
        # return no value if data is None
        return 'no value'

    if input_type is str:
        # For strings, return its length.
        return len(data)

    if input_type is bool:
        # For booleans, return boolean.
        return data

    if input_type is int:
        # For integers return a string showing how it compares to hundred
        isinstance(input_type, int)
        if data == 100:
            return 'equal to 100'

        elif data < 100:
            return 'less than 100'

        else:
            return 'more than 100'

    if input_type is list:
        # For lists return the 3rd item, or None if it doesn't exist
        try:
            if data[2]:
                return data[2]
        except IndexError:
            return None     # or None if it doesn't exist

