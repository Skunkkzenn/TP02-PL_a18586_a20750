
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDEleftCONCATASSIGNMENT CONCAT DIVIDE LPAREN MINUS NUMERO PLUS PRINT READ RPAREN SEMICOLON STRING TIMES VARIABLEprogram : statementsstatements : statements statementstatements : statementstatement : assignment_statement\n                 | print_statement\n                 | read_statementassignment_statement : VARIABLE ASSIGNMENT expression SEMICOLONprint_statement : PRINT LPAREN expression RPAREN SEMICOLONread_statement : READ LPAREN VARIABLE RPAREN SEMICOLONexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression TIMES expression\n                  | expression DIVIDE expression\n                  | expression CONCAT expressionexpression : LPAREN expression RPARENexpression : NUMEROexpression : STRINGexpression : VARIABLE'
    
_lr_action_items = {'VARIABLE':([0,2,3,4,5,6,10,11,12,13,16,21,22,23,24,25,26,36,37,],[7,7,-3,-4,-5,-6,-2,14,14,20,14,-7,14,14,14,14,14,-8,-9,]),'PRINT':([0,2,3,4,5,6,10,21,36,37,],[8,8,-3,-4,-5,-6,-2,-7,-8,-9,]),'READ':([0,2,3,4,5,6,10,21,36,37,],[9,9,-3,-4,-5,-6,-2,-7,-8,-9,]),'$end':([1,2,3,4,5,6,10,21,36,37,],[0,-1,-3,-4,-5,-6,-2,-7,-8,-9,]),'ASSIGNMENT':([7,],[11,]),'LPAREN':([8,9,11,12,16,22,23,24,25,26,],[12,13,16,16,16,16,16,16,16,16,]),'NUMERO':([11,12,16,22,23,24,25,26,],[17,17,17,17,17,17,17,17,]),'STRING':([11,12,16,22,23,24,25,26,],[18,18,18,18,18,18,18,18,]),'SEMICOLON':([14,15,17,18,28,29,30,31,32,33,34,35,],[-18,21,-16,-17,36,37,-10,-11,-12,-13,-14,-15,]),'PLUS':([14,15,17,18,19,27,30,31,32,33,34,35,],[-18,22,-16,-17,22,22,-10,-11,-12,-13,-14,-15,]),'MINUS':([14,15,17,18,19,27,30,31,32,33,34,35,],[-18,23,-16,-17,23,23,-10,-11,-12,-13,-14,-15,]),'TIMES':([14,15,17,18,19,27,30,31,32,33,34,35,],[-18,24,-16,-17,24,24,24,24,-12,-13,-14,-15,]),'DIVIDE':([14,15,17,18,19,27,30,31,32,33,34,35,],[-18,25,-16,-17,25,25,25,25,-12,-13,-14,-15,]),'CONCAT':([14,15,17,18,19,27,30,31,32,33,34,35,],[-18,26,-16,-17,26,26,26,26,26,26,-14,-15,]),'RPAREN':([14,17,18,19,20,27,30,31,32,33,34,35,],[-18,-16,-17,28,29,35,-10,-11,-12,-13,-14,-15,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statements':([0,],[2,]),'statement':([0,2,],[3,10,]),'assignment_statement':([0,2,],[4,4,]),'print_statement':([0,2,],[5,5,]),'read_statement':([0,2,],[6,6,]),'expression':([11,12,16,22,23,24,25,26,],[15,19,27,30,31,32,33,34,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statements','program',1,'p_program','main.py',89),
  ('statements -> statements statement','statements',2,'p_statements_multiple','main.py',93),
  ('statements -> statement','statements',1,'p_statements_single','main.py',97),
  ('statement -> assignment_statement','statement',1,'p_statement','main.py',102),
  ('statement -> print_statement','statement',1,'p_statement','main.py',103),
  ('statement -> read_statement','statement',1,'p_statement','main.py',104),
  ('assignment_statement -> VARIABLE ASSIGNMENT expression SEMICOLON','assignment_statement',4,'p_assignment_statement','main.py',109),
  ('print_statement -> PRINT LPAREN expression RPAREN SEMICOLON','print_statement',5,'p_print_statement','main.py',115),
  ('read_statement -> READ LPAREN VARIABLE RPAREN SEMICOLON','read_statement',5,'p_read_statement','main.py',121),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','main.py',128),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','main.py',129),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','main.py',130),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','main.py',131),
  ('expression -> expression CONCAT expression','expression',3,'p_expression_binop','main.py',132),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','main.py',145),
  ('expression -> NUMERO','expression',1,'p_expression_number','main.py',149),
  ('expression -> STRING','expression',1,'p_expression_string','main.py',153),
  ('expression -> VARIABLE','expression',1,'p_expression_variable','main.py',157),
]
