using System;
using System.Collections.Generic;

public class Brace
{
    /// Checks if a string of braces is valid.
    /// A valid string means every opening brace has a corresponding and correctly ordered closing brace.
    /// <param name="braces">A string containing only (), [], {}</param>
    /// <returns>True if the braces are valid; False otherwise</returns>
    /// time Complexity: O(n), where n is the length of the input string.
    /// - each character is visited once.
    /// - each push/pop operation on the stack is O(1).
    /// - the overall traversal and stack operations are linear.
    public static bool validBraces(string braces)
    {
        // Stack to keep track of opening braces
        var stack = new Stack<char>();

        // Dictionary mapping closing braces to their corresponding opening braces
        var pairs = new Dictionary<char, char>
        {
            { ')', '(' },
            { ']', '[' },
            { '}', '{' }
        };

        // Iterate over each character in the string
        foreach (char ch in braces)
        {
            // If it's an opening brace, push to stack
            if (pairs.ContainsValue(ch))
            {
                stack.Push(ch);
            }
            // If it's a closing brace, check for match
            else if (pairs.ContainsKey(ch))
            {
                // If stack is empty or top doesn't match the corresponding opening brace
                if (stack.Count == 0 || stack.Pop() != pairs[ch])
                {
                    return false;
                }
            }
        }

        // If stack is empty, all braces matched correctly
        return stack.Count == 0;
    }
}
