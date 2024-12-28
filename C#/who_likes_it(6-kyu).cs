using System;

public static class Kata
{
    public static string Likes(string[] name)
    {
        if (name == null || name.Length == 0)
        {
            return "no one likes this";
        }
        else if (name.Length == 1)
        {
            return $"{name[0]} likes this";
        }
        else if (name.Length == 2)
        {
            return $"{name[0]} and {name[1]} like this";
        }
        else if (name.Length == 3)
        {
            return $"{name[0]}, {name[1]} and {name[2]} like this";
        }
        else
        {
            return $"{name[0]}, {name[1]} and {name.Length - 2} others like this";
        }
    }
}

/* using System;

public static class Kata
{
    public static string Likes(string[] name)
    {
        int count = name?.Length ?? 0; // Handle null array

        return count switch
        {
            0 => "no one likes this",
            1 => $"{name[0]} likes this",
            2 => $"{name[0]} and {name[1]} like this",
            3 => $"{name[0]}, {name[1]} and {name[2]} like this",
            _ => $"{name[0]}, {name[1]} and {count - 2} others like this"
        };
    }
} */

