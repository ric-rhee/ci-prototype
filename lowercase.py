string = "ABCDEFG"

def convert_to_lower(string_to_convert):
    return string_to_convert.lower()

def test_convert_to_lower():
    if not all(97 <= ASCII <= 122 for ASCII in [ord(ele) for ele in string.lower()]):
        assert 0

test_convert_to_lower()