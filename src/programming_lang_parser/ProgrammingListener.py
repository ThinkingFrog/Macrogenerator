# Generated from Programming.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ProgrammingParser import ProgrammingParser
else:
    from ProgrammingParser import ProgrammingParser

# This class defines a complete listener for a parse tree produced by ProgrammingParser.
class ProgrammingListener(ParseTreeListener):

    # Enter a parse tree produced by ProgrammingParser#program.
    def enterProgram(self, ctx:ProgrammingParser.ProgramContext):
        pass

    # Exit a parse tree produced by ProgrammingParser#program.
    def exitProgram(self, ctx:ProgrammingParser.ProgramContext):
        pass


    # Enter a parse tree produced by ProgrammingParser#stmt.
    def enterStmt(self, ctx:ProgrammingParser.StmtContext):
        pass

    # Exit a parse tree produced by ProgrammingParser#stmt.
    def exitStmt(self, ctx:ProgrammingParser.StmtContext):
        pass


    # Enter a parse tree produced by ProgrammingParser#assign_stmt.
    def enterAssign_stmt(self, ctx:ProgrammingParser.Assign_stmtContext):
        pass

    # Exit a parse tree produced by ProgrammingParser#assign_stmt.
    def exitAssign_stmt(self, ctx:ProgrammingParser.Assign_stmtContext):
        pass


    # Enter a parse tree produced by ProgrammingParser#print_stmt.
    def enterPrint_stmt(self, ctx:ProgrammingParser.Print_stmtContext):
        pass

    # Exit a parse tree produced by ProgrammingParser#print_stmt.
    def exitPrint_stmt(self, ctx:ProgrammingParser.Print_stmtContext):
        pass


    # Enter a parse tree produced by ProgrammingParser#input_stmt.
    def enterInput_stmt(self, ctx:ProgrammingParser.Input_stmtContext):
        pass

    # Exit a parse tree produced by ProgrammingParser#input_stmt.
    def exitInput_stmt(self, ctx:ProgrammingParser.Input_stmtContext):
        pass


    # Enter a parse tree produced by ProgrammingParser#expression.
    def enterExpression(self, ctx:ProgrammingParser.ExpressionContext):
        pass

    # Exit a parse tree produced by ProgrammingParser#expression.
    def exitExpression(self, ctx:ProgrammingParser.ExpressionContext):
        pass


    # Enter a parse tree produced by ProgrammingParser#mult.
    def enterMult(self, ctx:ProgrammingParser.MultContext):
        pass

    # Exit a parse tree produced by ProgrammingParser#mult.
    def exitMult(self, ctx:ProgrammingParser.MultContext):
        pass


    # Enter a parse tree produced by ProgrammingParser#atom.
    def enterAtom(self, ctx:ProgrammingParser.AtomContext):
        pass

    # Exit a parse tree produced by ProgrammingParser#atom.
    def exitAtom(self, ctx:ProgrammingParser.AtomContext):
        pass



del ProgrammingParser