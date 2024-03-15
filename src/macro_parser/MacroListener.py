# Generated from Macro.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MacroParser import MacroParser
else:
    from MacroParser import MacroParser

# This class defines a complete listener for a parse tree produced by MacroParser.
class MacroListener(ParseTreeListener):

    # Enter a parse tree produced by MacroParser#start_.
    def enterStart_(self, ctx:MacroParser.Start_Context):
        pass

    # Exit a parse tree produced by MacroParser#start_.
    def exitStart_(self, ctx:MacroParser.Start_Context):
        pass


    # Enter a parse tree produced by MacroParser#expr.
    def enterExpr(self, ctx:MacroParser.ExprContext):
        pass

    # Exit a parse tree produced by MacroParser#expr.
    def exitExpr(self, ctx:MacroParser.ExprContext):
        pass



del MacroParser