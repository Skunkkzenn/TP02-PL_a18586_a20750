Thank you for sharing the instructions for configuring TP02-PL_a18586_a20750! Let’s break down the steps:

Install Python and Set Environment Variables:
First, install python.exe on your system.
Add the Python installation path to your environment variables.
Install Required Libraries:
Install the following Python libraries using pip:
virtualenv
ply
py-yacc
Create a Virtual Environment:
Choose a name for your folder (e.g., 'name_u_folder').
Create a virtual environment using the selected name:
virtualenv 'name_u_folder'

Activate the Virtual Environment:
Activate the virtual environment using the appropriate command based on your operating system:
.\'name_u_folder'\Scripts\activate

Using the Interpreter:
Navigate to the directory where the main.py file is located.
Execute the following command in the terminal:
py main.py entrada.fca

You’ll be prompted to enter commands. Follow the examples provided:
tmp_01 := 2*3+4 ;
a1_ := 12345 - (5191 * 15) ;
idade_valida? := 1;
mult_3! := a1_ * 3 ;
PRINT(mult_3!);

After entering the commands, press Ctrl+Z (or Ctrl+D on Linux/macOS), and then press Enter.
Wait for the commands to execute, and the results will be displayed in the terminal.
Supported Commands:
Assignment to a variable: Variable names must start with a lowercase letter or underscore (_). They can contain letters, digits, and underscores. The variable name can end with a question mark (?) or an exclamation mark (!).
Arithmetic expressions: You can assign arithmetic expressions to variables.
Reading values: Read values from user input.
Random value generation: Generate random values.
Output: Print results to the screen.
Requirements:
Python 3.x is required for running the interpreter.
Feel free to reach out if you have any further questions or need additional assistance! 😊





