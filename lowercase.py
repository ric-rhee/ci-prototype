string = "ABCDEFG"

def convert_to_lower(string_to_convert):
    converted_string = string_to_convert.upper()
    return converted_string

def test_convert_to_lower():
    string_lower = convert_to_lower(string)
    for ch in string_lower:
        if ch.islower():
            pass
        else:
            assert 0