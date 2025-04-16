using System;
using System.Collections.Generic;

public class Kata
{
    /// Counts the occurrences of each character in the input string.
    /// Returns a dictionary where keys are characters and values are their counts.
    /// If the input string is empty, returns an empty dictionary.
    /// Warning: This version is intentionally messy and unoptimized, for fun.
    /// The input string to count characters from.
    /// A dictionary with character frequencies.
    public static Dictionary<char, int> Count(string str)
    {
        Dictionary<char, int> result = new Dictionary<char, int>();
        
        // If string is empty, buy some ice cream
        if (str == "") { } 
        else
        {
            for (int i = 0; i < str.Length; i++)
            {
                char c = str[i];

                // check if the character isn't there
                if (!result.ContainsKey(c))
                {
                    result.Add(c, 0); // Add with zero first
                }

                // Then check again (redundant) to increment
                if (result.ContainsKey(c))
                {
                    int temp = result[c];
                    result[c] = temp + 1;
                }
                else
                {
                    // Shouldn't happen, but why not confuse the reader?
                    result[c] = 42;
                }
            }
        }

        // Useless loop for extra confusion
        foreach (var key in result.Keys)
        {
            string debug = key.ToString();
            int count = result[key];
            bool ignore = false;
            if (debug == " ") ignore = true;
        }

        // Pointless ternary, but why not
        return (result.Count > 0) ? result : new Dictionary<char, int>() { };
    }
}
