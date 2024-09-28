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
        4,1,14,20,2,0,7,0,2,1,7,1,1,0,1,0,1,0,5,0,8,8,0,10,0,12,0,11,9,0,
        1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,0,0,2,0,2,0,0,18,0,9,1,0,0,0,2,15,
        1,0,0,0,4,5,3,2,1,0,5,6,5,13,0,0,6,8,1,0,0,0,7,4,1,0,0,0,8,11,1,
        0,0,0,9,7,1,0,0,0,9,10,1,0,0,0,10,12,1,0,0,0,11,9,1,0,0,0,12,13,
        3,2,1,0,13,14,5,0,0,1,14,1,1,0,0,0,15,16,5,1,0,0,16,17,5,11,0,0,
        17,18,5,11,0,0,18,3,1,0,0,0,1,9
    ]

class MacroParser ( Parser ):

    grammarFileName = "Macro.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'define'", "<INVALID>", "<INVALID>", 
                     "'_'", "'('", "')'", "','", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'\\n'" ]

    symbolicNames = [ "<INVALID>", "DEFINE_KEYWORD", "UPPER_CHAR", "LOWER_CHAR", 
                      "UNDERSCORE", "LEFT_BRACKET", "RIGHT_BRACKET", "ARGS_SEPARATOR", 
                      "NON_ZERO_DIGIT", "DIGIT", "INT", "STRING", "WS", 
                      "NL", "MACRO_ARGS" ]

    RULE_start_ = 0
    RULE_expr = 1

    ruleNames =  [ "start_", "expr" ]

    EOF = Token.EOF
    DEFINE_KEYWORD=1
    UPPER_CHAR=2
    LOWER_CHAR=3
    UNDERSCORE=4
    LEFT_BRACKET=5
    RIGHT_BRACKET=6
    ARGS_SEPARATOR=7
    NON_ZERO_DIGIT=8
    DIGIT=9
    INT=10
    STRING=11
    WS=12
    NL=13
    MACRO_ARGS=14

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

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MacroParser.ExprContext)
            else:
                return self.getTypedRuleContext(MacroParser.ExprContext,i)


        def EOF(self):
            return self.getToken(MacroParser.EOF, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(MacroParser.NL)
            else:
                return self.getToken(MacroParser.NL, i)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 4
                    self.expr()
                    self.state = 5
                    self.match(MacroParser.NL) 
                self.state = 11
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 12
            self.expr()
            self.state = 13
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

        def DEFINE_KEYWORD(self):
            return self.getToken(MacroParser.DEFINE_KEYWORD, 0)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(MacroParser.STRING)
            else:
                return self.getToken(MacroParser.STRING, i)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self.match(MacroParser.DEFINE_KEYWORD)
            self.state = 16
            self.match(MacroParser.STRING)
            self.state = 17
            self.match(MacroParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





