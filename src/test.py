from pathlib import Path
from main import parse_macro_file, parse_target_lang_file, insert_macro_defs

def test_parse_macro_file():
    test_macro_file = Path("data/test.macro")
    expected_res = {'X': '17', 'Y': '42', 'Z': '2'}

    assert parse_macro_file(test_macro_file) == expected_res


def test_parse_target_lang_file():
    test_target_file = Path("data/test.arithmetic")
    expected_res = [['(', 'X', '+', 'Y', '-', '56', ')', '/', 'Z'], ['X', '*', 'Y']]

    assert parse_target_lang_file(test_target_file) == expected_res


def test_macrogenerating():
    expected_res = [['(', '17', '+', '42', '-', '56', ')', '/', '2'], ['17', '*', '42']]
    macro_defs = parse_macro_file(Path("data/test.macro"))
    lang_tokens = parse_target_lang_file(Path("data/test.arithmetic"))
    assert insert_macro_defs(macro_defs, lang_tokens) == expected_res
    