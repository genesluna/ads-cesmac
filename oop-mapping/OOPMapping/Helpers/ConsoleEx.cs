namespace OOPMapping.Helpers;

public static class ConsoleEx
{
    public static void WriteDashedLine(int length)
    {
        for (int i = 0; i < length; i++)
        {
            Console.Write("-");
        }
    }
}
