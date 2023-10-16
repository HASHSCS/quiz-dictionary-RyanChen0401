def get_value(data_dict, key):
    """
    Returns the value for the given key in the dictionary.
    If the key is not in the dictionary, return None.
    """
    if key in data_dict:
        return data_dict[key]
    else:
        return None


def remove_key(data_dict, key):
    """
    Removes the entry with the specified key from the dictionary.
    If the key is not found, the dictionary should remain unchanged.
    Returns the modified dictionary.
    """
    if key in data_dict:
        del data_dict[key]
    return data_dict
    