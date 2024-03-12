from pathlib import Path
from typing import List

from antlr4 import CommonTokenStream, FileStream

from arithmetic_parser.ArithmeticLexer import ArithmeticLexer
from arithmetic_parser.ArithmeticParser import ArithmeticParser
from macro_parser.MacroLexer import MacroLexer
from macro_parser.MacroParser import MacroParser
from macro_parser.VisitorInterp import VisitorInterp


def parse_macro_file(path: Path) -> dict:
    input_stream = FileStream(str(path))
    lexer = MacroLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MacroParser(token_stream)
    tree = parser.start_()

    if parser.getNumberOfSyntaxErrors() > 0:
        print("Syntax errors")
        return None

    visitor = VisitorInterp()

    return visitor.visit(tree)


def parse_target_lang_file(path: Path):
    input_stream = FileStream(str(path))
    lexer = ArithmeticLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    # parser = ArithmeticParser(token_stream)
    # tree = parser.expression()

    return list(
        map(
            lambda x: x.text,
            token_stream.getTokens(0, token_stream.getNumberOfOnChannelTokens()),
        )
    )


def main():
    macro_defs = parse_macro_file(Path("data/test.macro"))
    print(macro_defs)

    lang_tokens = parse_target_lang_file(Path("data/test.arithmetic"))
    print(lang_tokens)
    # for t in lang_tokens:
    #     print(t.text)

    res_list = []
    for token in lang_tokens:
        if token in macro_defs.keys():
            res_list.append(macro_defs[token])
        else:
            res_list.append(token)

    print(res_list)


if __name__ == "__main__":
    main()
