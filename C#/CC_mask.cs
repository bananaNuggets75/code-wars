public static class Kata
{
    /// Masks all characters in the input string except for the last four, replacing them with '#'.
    /// <param name="cc">The input string (e.g., a credit card number)</param>
    /// <returns>The masked string, with all but the last four characters replaced by '#'</returns>
    /// Time Complexity: O(n), where n is the length of the input string.
    /// - Creating a string of '#' characters takes O(n - 4) time.
    /// - Substring operation takes O(4) time for the last 4 characters.
    /// - Total = O(n)
    /// Space Complexity: O(n), for the resulting masked string.
    public static string Maskify(string cc)
    {
        // If the string is 4 characters or less, return it as is
        if (cc.Length <= 4)
            return cc;

        // Generate a string of '#' with the same length as the masked portion
        string maskedPart = new string('#', cc.Length - 4);

        // Extract the last 4 characters of the original string
        string visiblePart = cc.Substring(cc.Length - 4);

        // Return the combined masked + visible parts
        return maskedPart + visiblePart;
    }
}
