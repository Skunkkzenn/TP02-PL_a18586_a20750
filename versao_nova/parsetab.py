
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftMAISMENOSleftMULTIPLICADIVIDEALEATORIO CONCATENACAO DIVIDE DOISPONTOS ENTRADA ESCREVER FIM FUNCAO IGUAL LPAREN MAIS MENOS MULTIPLICA NUMERO PONTOVIRGULA RPAREN STRING STRINGESPECIAL VARIAVEL VIRGULAS : comandoscomandos : comandos comandocomandos : comandocomando : decl_variavel\n               | comando_escrever\n               | comando_funcaocomando_escrever : ESCREVER LPAREN expressao RPAREN PONTOVIRGULA\n                        | ESCREVER LPAREN decl_variavel RPAREN PONTOVIRGULAcomando_funcao : FUNCAO expressao LPAREN parametros RPAREN VIRGULA DOISPONTOS expressao PONTOVIRGULA \n                      | FUNCAO expressao LPAREN parametros RPAREN DOISPONTOS corpo FIMparametros : parametro\n                  | parametro VIRGULA parametrosparametro :  expressaocorpo : expressao\n             | expressao PONTOVIRGULA corpodecl_variavel : VARIAVEL IGUAL expressao PONTOVIRGULA\n                     | VARIAVEL IGUAL ENTRADA LPAREN RPAREN PONTOVIRGULA\n                     | VARIAVEL IGUAL ALEATORIO LPAREN expressao RPAREN PONTOVIRGULAexpressao : expressao MAIS expressao\n                 | expressao MENOS expressao\n                 | expressao MULTIPLICA expressao\n                 | expressao DIVIDE expressao\n                 | expressao CONCATENACAO expressaoexpressao : LPAREN expressao RPARENexpressao : NUMEROexpressao : VARIAVELexpressao : STRINGexpressao : STRINGESPECIAL'
    
_lr_action_items = {'VARIAVEL':([0,2,3,4,5,6,9,10,11,12,14,25,26,27,28,29,30,32,34,48,49,51,52,55,57,58,62,63,64,],[7,7,-3,-4,-5,-6,16,-2,16,24,16,16,16,16,16,16,16,-16,16,-7,-8,16,-17,16,-18,16,16,-10,-9,]),'ESCREVER':([0,2,3,4,5,6,10,32,48,49,52,57,63,64,],[8,8,-3,-4,-5,-6,-2,-16,-7,-8,-17,-18,-10,-9,]),'FUNCAO':([0,2,3,4,5,6,10,32,48,49,52,57,63,64,],[9,9,-3,-4,-5,-6,-2,-16,-7,-8,-17,-18,-10,-9,]),'$end':([1,2,3,4,5,6,10,32,48,49,52,57,63,64,],[0,-1,-3,-4,-5,-6,-2,-16,-7,-8,-17,-18,-10,-9,]),'IGUAL':([7,24,],[11,11,]),'LPAREN':([8,9,11,12,13,14,15,16,17,18,20,21,25,26,27,28,29,30,34,40,41,42,43,44,45,51,55,58,62,],[12,14,14,14,25,14,-25,-26,-27,-28,33,34,14,14,14,14,14,14,14,-19,-20,-21,-22,-23,-24,14,14,14,14,]),'NUMERO':([9,11,12,14,25,26,27,28,29,30,34,51,55,58,62,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'STRING':([9,11,12,14,25,26,27,28,29,30,34,51,55,58,62,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'STRINGESPECIAL':([9,11,12,14,25,26,27,28,29,30,34,51,55,58,62,],[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'ENTRADA':([11,],[20,]),'ALEATORIO':([11,],[21,]),'MAIS':([13,15,16,17,18,19,22,24,31,37,40,41,42,43,44,45,47,59,61,],[26,-25,-26,-27,-28,26,26,-26,26,26,-19,-20,-21,-22,26,-24,26,26,26,]),'MENOS':([13,15,16,17,18,19,22,24,31,37,40,41,42,43,44,45,47,59,61,],[27,-25,-26,-27,-28,27,27,-26,27,27,-19,-20,-21,-22,27,-24,27,27,27,]),'MULTIPLICA':([13,15,16,17,18,19,22,24,31,37,40,41,42,43,44,45,47,59,61,],[28,-25,-26,-27,-28,28,28,-26,28,28,28,28,-21,-22,28,-24,28,28,28,]),'DIVIDE':([13,15,16,17,18,19,22,24,31,37,40,41,42,43,44,45,47,59,61,],[29,-25,-26,-27,-28,29,29,-26,29,29,29,29,-21,-22,29,-24,29,29,29,]),'CONCATENACAO':([13,15,16,17,18,19,22,24,31,37,40,41,42,43,44,45,47,59,61,],[30,-25,-26,-27,-28,30,30,-26,30,30,-19,-20,-21,-22,30,-24,30,30,30,]),'PONTOVIRGULA':([15,16,17,18,19,35,36,40,41,42,43,44,45,46,53,59,61,],[-25,-26,-27,-28,32,48,49,-19,-20,-21,-22,-23,-24,52,57,62,64,]),'RPAREN':([15,16,17,18,22,23,24,31,32,33,37,38,39,40,41,42,43,44,45,47,52,56,57,],[-25,-26,-27,-28,35,36,-26,45,-16,46,-13,50,-11,-19,-20,-21,-22,-23,-24,53,-17,-12,-18,]),'VIRGULA':([15,16,17,18,37,39,40,41,42,43,44,45,50,],[-25,-26,-27,-28,-13,51,-19,-20,-21,-22,-23,-24,54,]),'FIM':([15,16,17,18,40,41,42,43,44,45,59,60,65,],[-25,-26,-27,-28,-19,-20,-21,-22,-23,-24,-14,63,-15,]),'DOISPONTOS':([50,54,],[55,58,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'S':([0,],[1,]),'comandos':([0,],[2,]),'comando':([0,2,],[3,10,]),'decl_variavel':([0,2,12,],[4,4,23,]),'comando_escrever':([0,2,],[5,5,]),'comando_funcao':([0,2,],[6,6,]),'expressao':([9,11,12,14,25,26,27,28,29,30,34,51,55,58,62,],[13,19,22,31,37,40,41,42,43,44,47,37,59,61,59,]),'parametros':([25,51,],[38,56,]),'parametro':([25,51,],[39,39,]),'corpo':([55,62,],[60,65,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> S","S'",1,None,None,None),
  ('S -> comandos','S',1,'p_inicio','grammar.py',13),
  ('comandos -> comandos comando','comandos',2,'p_comandos_multiplos','grammar.py',18),
  ('comandos -> comando','comandos',1,'p_comandos_unico','grammar.py',24),
  ('comando -> decl_variavel','comando',1,'p_comando','grammar.py',28),
  ('comando -> comando_escrever','comando',1,'p_comando','grammar.py',29),
  ('comando -> comando_funcao','comando',1,'p_comando','grammar.py',30),
  ('comando_escrever -> ESCREVER LPAREN expressao RPAREN PONTOVIRGULA','comando_escrever',5,'p_comando_escrever','grammar.py',45),
  ('comando_escrever -> ESCREVER LPAREN decl_variavel RPAREN PONTOVIRGULA','comando_escrever',5,'p_comando_escrever','grammar.py',46),
  ('comando_funcao -> FUNCAO expressao LPAREN parametros RPAREN VIRGULA DOISPONTOS expressao PONTOVIRGULA','comando_funcao',9,'p_comando_funcao','grammar.py',55),
  ('comando_funcao -> FUNCAO expressao LPAREN parametros RPAREN DOISPONTOS corpo FIM','comando_funcao',8,'p_comando_funcao','grammar.py',56),
  ('parametros -> parametro','parametros',1,'p_parametros','grammar.py',63),
  ('parametros -> parametro VIRGULA parametros','parametros',3,'p_parametros','grammar.py',64),
  ('parametro -> expressao','parametro',1,'p_parametro','grammar.py',71),
  ('corpo -> expressao','corpo',1,'p_corpo','grammar.py',75),
  ('corpo -> expressao PONTOVIRGULA corpo','corpo',3,'p_corpo','grammar.py',76),
  ('decl_variavel -> VARIAVEL IGUAL expressao PONTOVIRGULA','decl_variavel',4,'p_decl_variavel','grammar.py',82),
  ('decl_variavel -> VARIAVEL IGUAL ENTRADA LPAREN RPAREN PONTOVIRGULA','decl_variavel',6,'p_decl_variavel','grammar.py',83),
  ('decl_variavel -> VARIAVEL IGUAL ALEATORIO LPAREN expressao RPAREN PONTOVIRGULA','decl_variavel',7,'p_decl_variavel','grammar.py',84),
  ('expressao -> expressao MAIS expressao','expressao',3,'p_expressao_aritmetica','grammar.py',99),
  ('expressao -> expressao MENOS expressao','expressao',3,'p_expressao_aritmetica','grammar.py',100),
  ('expressao -> expressao MULTIPLICA expressao','expressao',3,'p_expressao_aritmetica','grammar.py',101),
  ('expressao -> expressao DIVIDE expressao','expressao',3,'p_expressao_aritmetica','grammar.py',102),
  ('expressao -> expressao CONCATENACAO expressao','expressao',3,'p_expressao_aritmetica','grammar.py',103),
  ('expressao -> LPAREN expressao RPAREN','expressao',3,'p_expressao_parentheses','grammar.py',132),
  ('expressao -> NUMERO','expressao',1,'p_expressao_numero','grammar.py',136),
  ('expressao -> VARIAVEL','expressao',1,'p_expressao_variavel','grammar.py',141),
  ('expressao -> STRING','expressao',1,'p_expressao_string','grammar.py',148),
  ('expressao -> STRINGESPECIAL','expressao',1,'p_expressao_string_especial','grammar.py',152),
]