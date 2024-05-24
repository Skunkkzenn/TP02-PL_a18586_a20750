<h1 align="center"> Análisado Léxico IPCA_LESI </h1>

Instructions:
## Instructions

That start configuration, this necessary instalation pyton.exe and add the path in variables ambient.
To start the configuration, it is necessary to install `python.exe` and add the path in environment variables.

Install the following libraries:
```sh
pip install virtualenv
pip install ply
pip install py-yacc

Select one name for u folder:
virtualenv 'name_u_folder' 
Activate the venv: .\'name_u_folder'\Scripts\activate

Activate the virtual environment:
.\'name_u_folder'\Scripts\activate
```
Executing commands in terminal:
```sh
py .\master.py .\testingFiles\exemplo-A-01.fca
Result: Variáveis finais: {'tmp_01': 10, 'a1_': -65520, 'idade_valida?': 1, 'mult_3!': -196560}

py .\master.py .\testingFiles\exemplo-B-01.fca
Result:
0
730
Ola Mundo
Olá, ESI
Variáveis finais: {'curso': 'ESI'}

py .\master.py .\testingFiles\exemplo-B-02.fca
Result:
Olá, EST IPCA!
Variáveis finais: {'escola': 'EST', 'inst': 'IPCA'}

py .\master.py .\testingFiles\exemplo-B-03.fca
Result:
Variáveis finais: {'valor': 'ENTRADA', 'ate10': 'ALEATORIO'}
```

