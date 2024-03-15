grammar Programming;

program	: (stmt ';')+ EOF;

stmt : input_stmt | print_stmt | assign_stmt ;

assign_stmt : IDENT '=' expression;

print_stmt : 'print' expression (',' expression)*;

input_stmt : 'input' IDENT;

expression : mult ( ('+' | '-') mult)*;

mult : atom (('*' | '/') atom)*;

atom : IDENT | NUMBER | '(' expression ')';

NUMBER : DIGIT + ;
	
IDENT : (LETTER | '_') (LETTER | '_' | DIGIT)* ;

fragment LETTER 	: [a-zA-Z];
	
fragment DIGIT : [0-9];

WS : [ \t\r\n]+ -> skip;