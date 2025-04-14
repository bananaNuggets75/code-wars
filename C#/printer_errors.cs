using System;

public class Printer 
{
    /// Calculates the printer error rate by counting how many characters are not between 'a' and 'm'.
    /// <param name="s">The input control string from the printer</param>
    /// A string representing the error rate as "errors/totalLength" (e.g., "2/10")
    /// Time Complexity: O(n), where n is the length of the input string.
    public static string PrinterError(String s) 
    {
        int errors = 0;

        foreach (char c in s)
        {
            // Characters from 'n' to 'z' are considered errors
            if (c < 'a' || c > 'm')
            {
                errors++;
            }
        }

        return $"{errors}/{s.Length}";
    }
}
