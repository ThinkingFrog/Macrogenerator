# Generated from Macro.g4 by ANTLR 4.13.1
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
        4,1,7,19,2,0,7,0,2,1,7,1,1,0,1,0,1,0,5,0,8,8,0,10,0,12,0,11,9,0,
        1,0,1,0,1,1,1,1,1,1,1,1,1,1,0,0,2,0,2,0,2,1,0,2,3,1,0,2,5,17,0,9,
        1,0,0,0,2,14,1,0,0,0,4,5,3,2,1,0,5,6,5,1,0,0,6,8,1,0,0,0,7,4,1,0,
        0,0,8,11,1,0,0,0,9,7,1,0,0,0,9,10,1,0,0,0,10,12,1,0,0,0,11,9,1,0,
        0,0,12,13,5,0,0,1,13,1,1,0,0,0,14,15,5,7,0,0,15,16,7,0,0,0,16,17,
        7,1,0,0,17,3,1,0,0,0,1,9
    ]

class MacroParser ( Parser ):

    grammarFileName = "Macro.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\\n'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'define'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "CHAR", "STRING", "DIGIT", 
                      "INT", "WS", "DEFINE" ]

    RULE_start_ = 0
    RULE_expr = 1

    ruleNames =  [ "start_", "expr" ]

    EOF = Token.EOF
    T__0=1
    CHAR=2
    STRING=3
    DIGIT=4
    INT=5
    WS=6
    DEFINE=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Start_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MacroParser.EOF, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MacroParser.ExprContext)
            else:
                return self.getTypedRuleContext(MacroParser.ExprContext,i)


        def getRuleIndex(self):
            return MacroParser.RULE_start_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart_" ):
                listener.enterStart_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart_" ):
                listener.exitStart_(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart_" ):
                return visitor.visitStart_(self)
            else:
                return visitor.visitChildren(self)




    def start_(self):

        localctx = MacroParser.Start_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start_)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 4
                self.expr()
                self.state = 5
                self.match(MacroParser.T__0)
                self.state = 11
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 12
            self.match(MacroParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEFINE(self):
            return self.getToken(MacroParser.DEFINE, 0)

        def CHAR(self, i:int=None):
            if i is None:
                return self.getTokens(MacroParser.CHAR)
            else:
                return self.getToken(MacroParser.CHAR, i)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(MacroParser.STRING)
            else:
                return self.getToken(MacroParser.STRING, i)

        def DIGIT(self):
            return self.getToken(MacroParser.DIGIT, 0)

        def INT(self):
            return self.getToken(MacroParser.INT, 0)

        def getRuleIndex(self):
            return MacroParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = MacroParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.match(MacroParser.DEFINE)
            self.state = 15
            _la = self._input.LA(1)
            if not(_la==2 or _la==3):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 16
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 60) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





