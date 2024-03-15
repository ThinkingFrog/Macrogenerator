grammar Arithmetic;

// Lexer Rules
DIGIT: [0-9]+;
CHAR: 'A' ..'Z';
PLUS: '+';
MINUS: '-';
MULTIPLY: '*';
DIVIDE: '/';

// Parser Rules
expression: term ((PLUS | MINUS) term)*;
term: factor ((MULTIPLY | DIVIDE) factor)*;
factor: (DIGIT+ | CHAR) | '(' expression ')';

// Skip whitespaces and tabs
WS: [ \t\n\r]+ -> skip;