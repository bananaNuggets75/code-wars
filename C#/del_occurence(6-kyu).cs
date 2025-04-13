using System;
using System.Collections.Generic;

public class Kata
{
    /// Returns a new array that includes each number in the input array at most 'x' times.
    /// The order of the original array is preserved.
    /// <param name="arr">The input array of integers (motifs)</param>
    /// <param name="x">The maximum number of times a value can appear in the result</param>
    /// <returns>An array with values appearing at most 'x' times, preserving order</returns>
    /// Time Complexity: O(n), where n is the length of the input array.
    /// - Each element is visited once.
    /// - Dictionary lookups and updates are O(1).
    public static int[] DeleteNth(int[] arr, int x)
    {
        var result = new List<int>();              // Stores the final output
        var counts = new Dictionary<int, int>();   // Tracks how many times each number has appeared

        foreach (int num in arr)
        {
            // Get current count of 'num', or 0 if not in dictionary
            counts.TryGetValue(num, out int count);

            if (count < x)
            {
                result.Add(num);          // Add to result list
                counts[num] = count + 1;  // Update count
            }
        }

        return result.ToArray();
    }
}
