# Generated from Arithmetic.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ArithmeticParser import ArithmeticParser
else:
    from ArithmeticParser import ArithmeticParser

# This class defines a complete listener for a parse tree produced by ArithmeticParser.
class ArithmeticListener(ParseTreeListener):

    # Enter a parse tree produced by ArithmeticParser#expression.
    def enterExpression(self, ctx:ArithmeticParser.ExpressionContext):
        pass

    # Exit a parse tree produced by ArithmeticParser#expression.
    def exitExpression(self, ctx:ArithmeticParser.ExpressionContext):
        pass


    # Enter a parse tree produced by ArithmeticParser#term.
    def enterTerm(self, ctx:ArithmeticParser.TermContext):
        pass

    # Exit a parse tree produced by ArithmeticParser#term.
    def exitTerm(self, ctx:ArithmeticParser.TermContext):
        pass


    # Enter a parse tree produced by ArithmeticParser#factor.
    def enterFactor(self, ctx:ArithmeticParser.FactorContext):
        pass

    # Exit a parse tree produced by ArithmeticParser#factor.
    def exitFactor(self, ctx:ArithmeticParser.FactorContext):
        pass



del ArithmeticParser