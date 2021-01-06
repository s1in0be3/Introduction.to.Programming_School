Numbers
Integer: used to store whole numbers, e.g. 50.
Float: used to store numbers with decimals, e.g. 50.12.
Boolean: used to store True or False values.
Complex: the definition for complex numbers is outside the scope of this lesson.
  
Strings and characters:
A character is a single letter, digit or punctuation symbol.
A string is basically a sequence of characters.

Note that the values are printed with spaces between them.
It is, however, possible to override the separator between the listed items from the default single space by
using the statement sep= as an extra variable in the print() statement.

Every print() statement ends in a newline character \n at a default.
It is possible to override this by adding an end= statement as an extra variable to the print() statement.
This may be used to remove the line break or newline functionality.

Not all programs are based on predefined values statically assigned to variables.
In many cases, there is a need to capture input from a (human) user, e.g. their name, surname and or age.
User input is gathered using the input () statement. The input statement returns a value, which may then be assigned to a variable.

||| Syntax errors: A syntax error occurs when there is an actual error within a line of
||| code, i.e. it doesn't conform to Python language rules:
|||
||| print("This will cause an error)
||| Output:
||| File "<ipython-input-54-9548305d1f8b>", line 1
||| print("This will cause an error)
|||                                  ^
|||SyntaxError: EOL while scanning string literal
           
||| Runtime errors:These are not always easy to spot, as the code will run without
||| causing a syntax error, i.e. it is correctly coded. The problem comes in
||| during execution of the program when it tries to access something  
||| that is unavailable, such as a file, or perform a task that cannot be
||| completed given specific values.
|||
||| The following example demonstrates what happens when the
||| interpreter tries to divide by zero. We haven't covered the / symbol
||| yet, so for now just take note of the error and not the actual use of
||| the / symbol. Although there are different types of runtime errors,
||| they are generally referred to as Exceptions. The reason for calling
||| these errors Exceptions is because the error should only occur under
||| exceptional circumstances and not every time the code / script is
||| executed.
||| print (50/0)
|||            
||| Output:
||| ZeroDivisionError                         
||| Traceback (most recent call last)
||| <ipython-input-55-4e5a6e69318c> in <module>
||| ----> 1 print (50/0)
||| ZeroDivisionError: division by zero
          
||| Semantic errors:The last type of error is a semantic error. These errors occur
||| whenever the program performs unexpectedly, but does not result in
||| a syntax or runtime error. In the following example, the programmer
||| wants to display a student's test result as a percentage, but has
||| forgotten to multiply the result by 100.
|||          
||| student_mark = 34
||| test_max = 50
||| print("Student percentage:",student_mark / test_max)
