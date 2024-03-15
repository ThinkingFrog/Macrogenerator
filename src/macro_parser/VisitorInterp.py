from antlr4 import *

from macro_parser.MacroParser import MacroParser
from macro_parser.MacroVisitor import MacroVisitor


class VisitorInterp(MacroVisitor):
    def visitStart_(self, ctx: MacroParser.Start_Context):
        res = {}

        for child in ctx.expr():
            pair = self.visit(child)
            res[pair[0]] = pair[1]

        return res

    def visitExpr(self, ctx: MacroParser.ExprContext):
        return (ctx.getChild(1).getText(), ctx.getChild(2).getText())
