using System;

public class Kata
{
    /// Returns the word with the highest score from a space-separated string.
    /// Score of each letter is based on its position in the alphabet: a=1, b=2, ..., z=26.
    /// In case of a tie, returns the word that appears first.
    /// The input string of words (lowercase only)
    /// The highest scoring word
    public static string High(string s)
    {
        string[] words = s.Split(' ');
        int highestScore = 0;
        string highestWord = "";

        foreach (string word in words)
        {
            int score = 0;

            foreach (char c in word)
            {
                score += c - 'a' + 1; // Convert character to position: 'a' = 1, ..., 'z' = 26
            }

            if (score > highestScore)
            {
                highestScore = score;
                highestWord = word;
            }
        }

        return highestWord;
    }
}
