# Generated from Programming.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,14,71,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,1,0,1,0,4,0,20,8,0,11,0,12,0,21,1,0,1,0,1,1,1,1,1,
        1,3,1,29,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,5,3,39,8,3,10,3,12,
        3,42,9,3,1,4,1,4,1,4,1,5,1,5,1,5,5,5,50,8,5,10,5,12,5,53,9,5,1,6,
        1,6,1,6,5,6,58,8,6,10,6,12,6,61,9,6,1,7,1,7,1,7,1,7,1,7,1,7,3,7,
        69,8,7,1,7,0,0,8,0,2,4,6,8,10,12,14,0,2,1,0,6,7,1,0,8,9,70,0,19,
        1,0,0,0,2,28,1,0,0,0,4,30,1,0,0,0,6,34,1,0,0,0,8,43,1,0,0,0,10,46,
        1,0,0,0,12,54,1,0,0,0,14,68,1,0,0,0,16,17,3,2,1,0,17,18,5,1,0,0,
        18,20,1,0,0,0,19,16,1,0,0,0,20,21,1,0,0,0,21,19,1,0,0,0,21,22,1,
        0,0,0,22,23,1,0,0,0,23,24,5,0,0,1,24,1,1,0,0,0,25,29,3,8,4,0,26,
        29,3,6,3,0,27,29,3,4,2,0,28,25,1,0,0,0,28,26,1,0,0,0,28,27,1,0,0,
        0,29,3,1,0,0,0,30,31,5,13,0,0,31,32,5,2,0,0,32,33,3,10,5,0,33,5,
        1,0,0,0,34,35,5,3,0,0,35,40,3,10,5,0,36,37,5,4,0,0,37,39,3,10,5,
        0,38,36,1,0,0,0,39,42,1,0,0,0,40,38,1,0,0,0,40,41,1,0,0,0,41,7,1,
        0,0,0,42,40,1,0,0,0,43,44,5,5,0,0,44,45,5,13,0,0,45,9,1,0,0,0,46,
        51,3,12,6,0,47,48,7,0,0,0,48,50,3,12,6,0,49,47,1,0,0,0,50,53,1,0,
        0,0,51,49,1,0,0,0,51,52,1,0,0,0,52,11,1,0,0,0,53,51,1,0,0,0,54,59,
        3,14,7,0,55,56,7,1,0,0,56,58,3,14,7,0,57,55,1,0,0,0,58,61,1,0,0,
        0,59,57,1,0,0,0,59,60,1,0,0,0,60,13,1,0,0,0,61,59,1,0,0,0,62,69,
        5,13,0,0,63,69,5,12,0,0,64,65,5,10,0,0,65,66,3,10,5,0,66,67,5,11,
        0,0,67,69,1,0,0,0,68,62,1,0,0,0,68,63,1,0,0,0,68,64,1,0,0,0,69,15,
        1,0,0,0,6,21,28,40,51,59,68
    ]

class ProgrammingParser ( Parser ):

    grammarFileName = "Programming.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'='", "'print'", "','", "'input'", 
                     "'+'", "'-'", "'*'", "'/'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "NUMBER", "IDENT", "WS" ]

    RULE_program = 0
    RULE_stmt = 1
    RULE_assign_stmt = 2
    RULE_print_stmt = 3
    RULE_input_stmt = 4
    RULE_expression = 5
    RULE_mult = 6
    RULE_atom = 7

    ruleNames =  [ "program", "stmt", "assign_stmt", "print_stmt", "input_stmt", 
                   "expression", "mult", "atom" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    NUMBER=12
    IDENT=13
    WS=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ProgrammingParser.EOF, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProgrammingParser.StmtContext)
            else:
                return self.getTypedRuleContext(ProgrammingParser.StmtContext,i)


        def getRuleIndex(self):
            return ProgrammingParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = ProgrammingParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 16
                self.stmt()
                self.state = 17
                self.match(ProgrammingParser.T__0)
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 8232) != 0)):
                    break

            self.state = 23
            self.match(ProgrammingParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def input_stmt(self):
            return self.getTypedRuleContext(ProgrammingParser.Input_stmtContext,0)


        def print_stmt(self):
            return self.getTypedRuleContext(ProgrammingParser.Print_stmtContext,0)


        def assign_stmt(self):
            return self.getTypedRuleContext(ProgrammingParser.Assign_stmtContext,0)


        def getRuleIndex(self):
            return ProgrammingParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)




    def stmt(self):

        localctx = ProgrammingParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        try:
            self.state = 28
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.input_stmt()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.print_stmt()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 3)
                self.state = 27
                self.assign_stmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(ProgrammingParser.IDENT, 0)

        def expression(self):
            return self.getTypedRuleContext(ProgrammingParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ProgrammingParser.RULE_assign_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign_stmt" ):
                listener.enterAssign_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign_stmt" ):
                listener.exitAssign_stmt(self)




    def assign_stmt(self):

        localctx = ProgrammingParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(ProgrammingParser.IDENT)
            self.state = 31
            self.match(ProgrammingParser.T__1)
            self.state = 32
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Print_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProgrammingParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ProgrammingParser.ExpressionContext,i)


        def getRuleIndex(self):
            return ProgrammingParser.RULE_print_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint_stmt" ):
                listener.enterPrint_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint_stmt" ):
                listener.exitPrint_stmt(self)




    def print_stmt(self):

        localctx = ProgrammingParser.Print_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_print_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(ProgrammingParser.T__2)
            self.state = 35
            self.expression()
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 36
                self.match(ProgrammingParser.T__3)
                self.state = 37
                self.expression()
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Input_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(ProgrammingParser.IDENT, 0)

        def getRuleIndex(self):
            return ProgrammingParser.RULE_input_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInput_stmt" ):
                listener.enterInput_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInput_stmt" ):
                listener.exitInput_stmt(self)




    def input_stmt(self):

        localctx = ProgrammingParser.Input_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_input_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(ProgrammingParser.T__4)
            self.state = 44
            self.match(ProgrammingParser.IDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mult(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProgrammingParser.MultContext)
            else:
                return self.getTypedRuleContext(ProgrammingParser.MultContext,i)


        def getRuleIndex(self):
            return ProgrammingParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = ProgrammingParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.mult()
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6 or _la==7:
                self.state = 47
                _la = self._input.LA(1)
                if not(_la==6 or _la==7):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 48
                self.mult()
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProgrammingParser.AtomContext)
            else:
                return self.getTypedRuleContext(ProgrammingParser.AtomContext,i)


        def getRuleIndex(self):
            return ProgrammingParser.RULE_mult

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMult" ):
                listener.enterMult(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMult" ):
                listener.exitMult(self)




    def mult(self):

        localctx = ProgrammingParser.MultContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_mult)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.atom()
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8 or _la==9:
                self.state = 55
                _la = self._input.LA(1)
                if not(_la==8 or _la==9):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 56
                self.atom()
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(ProgrammingParser.IDENT, 0)

        def NUMBER(self):
            return self.getToken(ProgrammingParser.NUMBER, 0)

        def expression(self):
            return self.getTypedRuleContext(ProgrammingParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ProgrammingParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)




    def atom(self):

        localctx = ProgrammingParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_atom)
        try:
            self.state = 68
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.match(ProgrammingParser.IDENT)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.match(ProgrammingParser.NUMBER)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 64
                self.match(ProgrammingParser.T__9)
                self.state = 65
                self.expression()
                self.state = 66
                self.match(ProgrammingParser.T__10)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





