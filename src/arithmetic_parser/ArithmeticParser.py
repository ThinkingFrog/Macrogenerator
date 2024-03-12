# Generated from Arithmetic.g4 by ANTLR 4.13.1
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
        4,1,9,37,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,5,0,10,8,0,10,0,12,
        0,13,9,0,1,1,1,1,1,1,5,1,18,8,1,10,1,12,1,21,9,1,1,2,4,2,24,8,2,
        11,2,12,2,25,1,2,3,2,29,8,2,1,2,1,2,1,2,1,2,3,2,35,8,2,1,2,0,0,3,
        0,2,4,0,2,1,0,5,6,1,0,7,8,38,0,6,1,0,0,0,2,14,1,0,0,0,4,34,1,0,0,
        0,6,11,3,2,1,0,7,8,7,0,0,0,8,10,3,2,1,0,9,7,1,0,0,0,10,13,1,0,0,
        0,11,9,1,0,0,0,11,12,1,0,0,0,12,1,1,0,0,0,13,11,1,0,0,0,14,19,3,
        4,2,0,15,16,7,1,0,0,16,18,3,4,2,0,17,15,1,0,0,0,18,21,1,0,0,0,19,
        17,1,0,0,0,19,20,1,0,0,0,20,3,1,0,0,0,21,19,1,0,0,0,22,24,5,3,0,
        0,23,22,1,0,0,0,24,25,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,29,
        1,0,0,0,27,29,5,4,0,0,28,23,1,0,0,0,28,27,1,0,0,0,29,35,1,0,0,0,
        30,31,5,1,0,0,31,32,3,0,0,0,32,33,5,2,0,0,33,35,1,0,0,0,34,28,1,
        0,0,0,34,30,1,0,0,0,35,5,1,0,0,0,5,11,19,25,28,34
    ]

class ArithmeticParser ( Parser ):

    grammarFileName = "Arithmetic.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "<INVALID>", "<INVALID>", 
                     "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "DIGIT", "CHAR", 
                      "PLUS", "MINUS", "MULTIPLY", "DIVIDE", "WS" ]

    RULE_expression = 0
    RULE_term = 1
    RULE_factor = 2

    ruleNames =  [ "expression", "term", "factor" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    DIGIT=3
    CHAR=4
    PLUS=5
    MINUS=6
    MULTIPLY=7
    DIVIDE=8
    WS=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArithmeticParser.TermContext)
            else:
                return self.getTypedRuleContext(ArithmeticParser.TermContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(ArithmeticParser.PLUS)
            else:
                return self.getToken(ArithmeticParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(ArithmeticParser.MINUS)
            else:
                return self.getToken(ArithmeticParser.MINUS, i)

        def getRuleIndex(self):
            return ArithmeticParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = ArithmeticParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.term()
            self.state = 11
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5 or _la==6:
                self.state = 7
                _la = self._input.LA(1)
                if not(_la==5 or _la==6):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 8
                self.term()
                self.state = 13
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArithmeticParser.FactorContext)
            else:
                return self.getTypedRuleContext(ArithmeticParser.FactorContext,i)


        def MULTIPLY(self, i:int=None):
            if i is None:
                return self.getTokens(ArithmeticParser.MULTIPLY)
            else:
                return self.getToken(ArithmeticParser.MULTIPLY, i)

        def DIVIDE(self, i:int=None):
            if i is None:
                return self.getTokens(ArithmeticParser.DIVIDE)
            else:
                return self.getToken(ArithmeticParser.DIVIDE, i)

        def getRuleIndex(self):
            return ArithmeticParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = ArithmeticParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.factor()
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7 or _la==8:
                self.state = 15
                _la = self._input.LA(1)
                if not(_la==7 or _la==8):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 16
                self.factor()
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHAR(self):
            return self.getToken(ArithmeticParser.CHAR, 0)

        def DIGIT(self, i:int=None):
            if i is None:
                return self.getTokens(ArithmeticParser.DIGIT)
            else:
                return self.getToken(ArithmeticParser.DIGIT, i)

        def expression(self):
            return self.getTypedRuleContext(ArithmeticParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ArithmeticParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = ArithmeticParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.state = 34
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [3]:
                    self.state = 23 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 22
                        self.match(ArithmeticParser.DIGIT)
                        self.state = 25 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==3):
                            break

                    pass
                elif token in [4]:
                    self.state = 27
                    self.match(ArithmeticParser.CHAR)
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.match(ArithmeticParser.T__0)
                self.state = 31
                self.expression()
                self.state = 32
                self.match(ArithmeticParser.T__1)
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





