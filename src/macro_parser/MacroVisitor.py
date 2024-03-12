# Generated from Macro.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MacroParser import MacroParser
else:
    from MacroParser import MacroParser

# This class defines a complete generic visitor for a parse tree produced by MacroParser.

class MacroVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MacroParser#start_.
    def visitStart_(self, ctx:MacroParser.Start_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MacroParser#expr.
    def visitExpr(self, ctx:MacroParser.ExprContext):
        return self.visitChildren(ctx)



del MacroParser