from pathlib import Path

import click
from antlr4 import CommonTokenStream, FileStream, InputStream

from arithmetic_parser.ArithmeticLexer import ArithmeticLexer
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
    lines = input_stream.strdata.split('\n')
    res = list()
    for line in lines:
        lexer = ArithmeticLexer(InputStream(line))
        token_stream = CommonTokenStream(lexer)
        res_line = list(
            map(
                lambda x: x.text,
                token_stream.getTokens(0, token_stream.getNumberOfOnChannelTokens()),
            ))
        res.append(res_line)
    return res


def insert_macro_defs(macro_defs: dict, lang_exprs: list):
    print(f"Macro definitions: {macro_defs}")
    print(f"Target language tokens list:")
    for expr in lang_exprs:
        print(expr)
    res = []
    for expr in lang_exprs:
        token_list = []
        for token in expr:
            if token in macro_defs.keys():
                token_list.append(macro_defs[token])
            else:
                token_list.append(token)
        res.append(token_list)

    print(f"Tokens after macro replacement:")
    for res_str in res:
        print(res_str)
    print("Result string: ")

    for res_str in res:
        print(*res_str)
    return res



@click.command("macrogenerator")
@click.option(
    "--macro-file",
    "-m",
    type=click.Path(exists=True, dir_okay=False, path_type=Path),
    required=True,
)
@click.option(
    "--target-file",
    "-t",
    type=click.Path(exists=True, dir_okay=False, path_type=Path),
    required=True,
)
def main(
    macro_file: Path,
    target_file: Path,
):
    
    macro_defs = parse_macro_file(Path(macro_file))
    lang_tokens = parse_target_lang_file(Path(target_file))
    insert_macro_defs(macro_defs, lang_tokens)


if __name__ == "__main__":
    main()
