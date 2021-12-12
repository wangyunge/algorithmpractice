/*
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:

Input: s = "1 + 1"
Output: 2
Example 2:

Input: s = " 2-1 + 2 "
Output: 3
Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
 */




import java.util.*;

class Solution {
    public int calculate(String s) {
        char[] chars = s.toCharArray();
        Stack<Integer> signStack = new Stack<Integer>();
        signStack.push(1);
        int sign = 1;
        int digtValue = 0;
        int res = 0;

        for (char ch : chars){
            if(ch == ' '){
                continue;
            }
            else if (Character.isDigit(ch)) {
                digtValue = digtValue * 10 + ch - '0';
            }
            else if(ch == '('){
                signStack.push(sign * signStack.peek());
                sign = 1;
                digtValue = 0;
            }
            else{
                res += digtValue * sign * signStack.peek();
                digtValue = 0;
                sign = 1;
                if (ch == '-'){
                    sign = -1 ;
                } 
                else if (ch == '+') {
                    continue    ;
                }
                else if (ch == ')') {
                    signStack.pop() ;
                }

            }
        }

        res += digtValue * signStack.pop() * sign;
        return res;
        
    }
}
