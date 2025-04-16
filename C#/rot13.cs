using System;
using System.Text;

public class Kata
{
    /// Applies the ROT13 cipher to the input message.
    /// Letters from 'a' to 'z' and 'A' to 'Z' are shifted 13 places in the alphabet.
    /// Non-alphabetic characters are returned unchanged.
    /// The input string to encode.
    /// The encoded string after applying ROT13.
    public static string Rot13(string message)
    {
        StringBuilder result = new StringBuilder();

        foreach (char c in message)
        {
            if (c >= 'a' && c <= 'z')
            {
                // Rotate lowercase letters
                char shifted = (char)(((c - 'a' + 13) % 26) + 'a');
                result.Append(shifted);
            }
            else if (c >= 'A' && c <= 'Z')
            {
                // Rotate uppercase letters
                char shifted = (char)(((c - 'A' + 13) % 26) + 'A');
                result.Append(shifted);
            }
            else
            {
                // Leave non-letter characters unchanged
                result.Append(c);
            }
        }

        return result.ToString();
    }
}
