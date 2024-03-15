grammar Macro;

// Lexer Rules
CHAR: 'A' ..'Z';
STRING: CHAR+;
DIGIT: [0-9];
INT: DIGIT+;
WS: [ \t\n\r] -> skip;

DEFINE: 'define';

// Parser Rules
start_: (expr '\n')* expr '\n'* EOF;
expr: DEFINE (CHAR | STRING) (CHAR | STRING | DIGIT | INT);