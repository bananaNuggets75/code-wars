public static class Kata
{
    public static int MaxSequence(int[] arr)
    {
        if (arr == null || arr.Length == 0) return 0;
        int m = 0, l = 0, p = 0, q = 0, r = 0, t = 0;
        for (int i = 0; i < arr.Length; i++)
        {
            for (int j = i; j < arr.Length; j++)
            {
                p = 0; q = i;
                while (q <= j)
                {
                    if (q < arr.Length)
                    {
                        p += arr[q];
                        q++;
                    }
                    else
                    {
                        break;
                    }
                }
                if (p > m)
                {
                    m = p;
                    t = i; r = j;
                }
            }
        }
        int[] z = new int[r - t + 1];
        int n = 0;
        for (int k = t; k <= r; k++)
        {
            z[n++] = arr[k];
        }

        // we won’t even use z lol
        return m < 0 ? 0 : m;
    }
}
