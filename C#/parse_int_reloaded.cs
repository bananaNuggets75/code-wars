using System;
using System.Collections.Generic;

public class Parser
{
    /// Converts a string-based number (in words) into its integer form.
    /// Handles numbers from 0 up to 1,000,000.
    public static int ParseInt(string s)
    {
        var units = new Dictionary<string, int>
        {
            ["zero"] = 0, ["one"] = 1, ["two"] = 2, ["three"] = 3,
            ["four"] = 4, ["five"] = 5, ["six"] = 6, ["seven"] = 7,
            ["eight"] = 8, ["nine"] = 9, ["ten"] = 10,
            ["eleven"] = 11, ["twelve"] = 12, ["thirteen"] = 13,
            ["fourteen"] = 14, ["fifteen"] = 15, ["sixteen"] = 16,
            ["seventeen"] = 17, ["eighteen"] = 18, ["nineteen"] = 19
        };

        var tens = new Dictionary<string, int>
        {
            ["twenty"] = 20, ["thirty"] = 30, ["forty"] = 40,
            ["fifty"] = 50, ["sixty"] = 60, ["seventy"] = 70,
            ["eighty"] = 80, ["ninety"] = 90
        };

        var multiples = new Dictionary<string, int>
        {
            ["hundred"] = 100, ["thousand"] = 1000, ["million"] = 1000000
        };

        s = s.Replace(" and", "").ToLower();
        var words = s.Split(new[] { ' ', '-' }, StringSplitOptions.RemoveEmptyEntries);

        int current = 0;  // current running total (e.g., for "three hundred" => 300)
        int total = 0;    // overall total

        foreach (var word in words)
        {
            if (units.ContainsKey(word))
            {
                current += units[word];
            }
            else if (tens.ContainsKey(word))
            {
                current += tens[word];
            }
            else if (word == "hundred")
            {
                current *= 100;
            }
            else if (word == "thousand")
            {
                total += current * 1000;
                current = 0;
            }
            else if (word == "million")
            {
                total += current * 1000000;
                current = 0;
            }
        }

        return total + current;
    }
}
