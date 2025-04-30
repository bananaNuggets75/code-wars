"""Write a function that, given a string of text (possibly with punctuation and line-breaks), returns an array of the top-3 most occurring words, in descending order of the number of occurrences.

Assumptions:
A word is a string of letters (A to Z) optionally containing one or more apostrophes (') in ASCII.
Apostrophes can appear at the start, middle or end of a word ('abc, abc', 'abc', ab'c are all valid)
Any other characters (e.g. #, \, / , . ...) are not part of a word and should be treated as whitespace.
Matches should be case-insensitive, and the words in the result should be lowercased.
Ties may be broken arbitrarily.
If a text contains fewer than three unique words, then either the top-2 or top-1 words should be returned, or an empty array if a text contains no words.
Examples:
"In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income."

--> ["a", "of", "on"]


"e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"

--> ["e", "ddd", "aa"]


"  //wont won't won't"

--> ["won't", "wont"]
Bonus points (not really, but just for fun):
Avoid creating an array whose memory footprint is roughly as big as the input text.
Avoid sorting the entire array of unique words."""

using System;
using System.Collections.Generic;
using System.Text.RegularExpressions;
using System.Linq;

public class TopWords
{
    public static List<string> Top3(string s)
    {
        // Dictionary to store frequency of each word
        Dictionary<string, int> freq = new Dictionary<string, int>();

        // Use regex to find all words, considering apostrophes (e.g., won't)
        foreach (Match match in Regex.Matches(s.ToLower(), @"[a-z']+"))
        {
            string word = match.Value;

            // A word must contain at least one alphabet character
            if (word.All(c => c == '\'') || word.Trim('\'').Length == 0)
                continue;

            if (freq.ContainsKey(word))
                freq[word]++;
            else
                freq[word] = 1;
        }

        // Return the top 3 most frequent words (or fewer if less available)
        return freq
            .OrderByDescending(pair => pair.Value)  // Sort by frequency descending
            .Take(3)                                 // Take top 3
            .Select(pair => pair.Key)               // Return the words only
            .ToList();
    }
}
