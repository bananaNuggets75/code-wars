public class Kata
{
  /// 
  /// Calculates the average of the squared absolute differences between 
  /// corresponding elements of two integer arrays of equal length.
  /// 
  /// <param name="firstArray">First integer array.</param>
  /// <param name="secondArray">Second integer array of the same length as the first.</param>
  /// Average of squared differences as a double.
  public static double Solution(int[] firstArray, int[] secondArray)
  {
    int length = firstArray.Length;
    double total = 0;

    for (int i = 0; i < length; i++)
    {
      int difference = firstArray[i] - secondArray[i];
      total += difference * difference;
    }

    return total / length;
  }
}
