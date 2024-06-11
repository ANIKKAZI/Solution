# Command Line Utility Solution for Numerical Adjustments using Python
Compute.py is a command-line tool that accepts numerical inputs and processes them according to two command-line parameters: a threshold and a limit. The Python script uses the specified threshold and limit to apply modifications to up to 100 numerical values that it reads from standard input. It then publishes the changed values to standard output.

## Components of compute.py
  * The script reads numerical values from standard input.
  * Accepts two numerical command line arguments:
      * A threshold value to compare against the input values.
      * A limit value that determines how much the input values can be reduced.
  * Transformation Logic:
  * If the input value is less than or equal to the threshold, it prints 0.0.
  * If the remaining limit is greater than the input value minus the threshold, it prints the input value minus the threshold and reduces 
    the remaining limit.
  * If the remaining limit is less than or equal to the input value minus the threshold, it prints the remaining limit and sets the 
    remaining limit to 0.0.
  * Output:
     * Prints the transformed values.
     * Prints the total reduction applied from the initial limit.

## Standard Input
Up to 100 lines of numerical input are supported by the script; each value must fall between 0.0 and 1,000,000,000.0.
### Example input
 **python compute.py 1000.0 20000000.00**

 After running the command, provide numerical input values line by line:

 19.0  
 0.0  
 1000   
 1001.5  
 20000  
 25000000.0  

 **Press Ctrl+D (or Ctrl+Z on Windows) to end the input.**

 ## Example Output
  Given the command and input values above, the output will be:

  0.0  
  0.0  
  0.0  
  1.5  
  19000.0  
  19980998.5  
  20000000.0  

## Error Handling 
 * The script verifies that the command line arguments fall under the designated range and are valid numerical values. If not, it exits 
   after printing an error message.
 *  The script verifies that every input value falls inside the designated range and is a valid number. It prints an error message and        ignores the value if an input value is invalid or outside of range.
 *  The script stops processing additional input and produces a notice stating that the maximum number of inputs has been reached if more 
    than 100 lines of input are supplied.

