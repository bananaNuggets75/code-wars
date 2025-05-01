public class Kata
{
    public static string UInt32ToIP(uint ip)
    {
        // Extract each 8-bit octet from the 32-bit integer using bitwise operations
        // >> is the right shift operator, moving bits to the right
        // & 0xFF ensures only the last 8 bits are kept (masking the rest)

        uint firstOctet  = (ip >> 24) & 0xFF; // Extract the highest (leftmost) 8 bits
        uint secondOctet = (ip >> 16) & 0xFF; // Next 8 bits
        uint thirdOctet  = (ip >> 8)  & 0xFF; // Next 8 bits
        uint fourthOctet = ip & 0xFF;         // Lowest (rightmost) 8 bits

        // Convert each octet to string and join them with dots to form an IP address
        return string.Join(".",
            firstOctet,
            secondOctet,
            thirdOctet,
            fourthOctet
        );
    }
}
