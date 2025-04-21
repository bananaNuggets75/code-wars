using System;
using System.Collections.Generic;

public class PickPeaks
{
    public static Dictionary<string, List<int>> GetPeaks(int[] arr)
    {
        var result = new Dictionary<string, List<int>>()
        {
            { "pos", new List<int>() },
            { "peaks", new List<int>() }
        };

        int? possiblePeakPos = null;

        for (int i = 1; i < arr.Length; i++)
        {
            // check for rising edge
            if (arr[i] > arr[i - 1])
            {
                possiblePeakPos = i;
            }

            // check for falling edge
            else if (arr[i] < arr[i - 1] && possiblePeakPos != null)
            {
                result["pos"].Add(possiblePeakPos.Value);
                result["peaks"].Add(arr[possiblePeakPos.Value]);
                possiblePeakPos = null;
            }

            // if arr[i] == arr[i - 1], we are in a plateau — do nothing
        }

        return result;
    }
}
