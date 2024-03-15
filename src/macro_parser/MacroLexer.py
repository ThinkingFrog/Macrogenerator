# Generated from Macro.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,7,42,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,1,0,1,0,1,1,1,1,1,2,4,2,21,8,2,11,2,12,2,22,1,3,1,3,1,4,4,
        4,28,8,4,11,4,12,4,29,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,0,0,7,1,1,3,2,5,3,7,4,9,5,11,6,13,7,1,0,2,1,0,48,57,3,0,9,10,13,
        13,32,32,43,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,
        1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,1,15,1,0,0,0,3,17,1,0,0,0,5,20,
        1,0,0,0,7,24,1,0,0,0,9,27,1,0,0,0,11,31,1,0,0,0,13,35,1,0,0,0,15,
        16,5,10,0,0,16,2,1,0,0,0,17,18,2,65,90,0,18,4,1,0,0,0,19,21,3,3,
        1,0,20,19,1,0,0,0,21,22,1,0,0,0,22,20,1,0,0,0,22,23,1,0,0,0,23,6,
        1,0,0,0,24,25,7,0,0,0,25,8,1,0,0,0,26,28,3,7,3,0,27,26,1,0,0,0,28,
        29,1,0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,30,10,1,0,0,0,31,32,7,1,0,
        0,32,33,1,0,0,0,33,34,6,5,0,0,34,12,1,0,0,0,35,36,5,100,0,0,36,37,
        5,101,0,0,37,38,5,102,0,0,38,39,5,105,0,0,39,40,5,110,0,0,40,41,
        5,101,0,0,41,14,1,0,0,0,3,0,22,29,1,6,0,0
    ]

class MacroLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    CHAR = 2
    STRING = 3
    DIGIT = 4
    INT = 5
    WS = 6
    DEFINE = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'\\n'", "'define'" ]

    symbolicNames = [ "<INVALID>",
            "CHAR", "STRING", "DIGIT", "INT", "WS", "DEFINE" ]

    ruleNames = [ "T__0", "CHAR", "STRING", "DIGIT", "INT", "WS", "DEFINE" ]

    grammarFileName = "Macro.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


