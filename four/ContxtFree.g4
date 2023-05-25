grammar ContxtFree;


PT : '.';
NUMBER: [0-9]+;
DBL : NUMBER+ PT NUMBER+
    | PT NUMBER+
    | NUMBER+;


expr
    : expr '(' expr ')'
    | expr '(' expr ')' '^'
    | expr '*' expr
    | expr '/' expr
    | expr '>' expr
    | expr '<' expr
    | expr '&' expr
    | NUMBER
    | DBL;

