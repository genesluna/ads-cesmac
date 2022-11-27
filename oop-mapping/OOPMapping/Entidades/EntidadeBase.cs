using OOPMapping.Helpers;

namespace OOPMapping.Entidades;

public abstract class EntidadeBase
{
    public int Id { get; set; }
    public DateTimeOffset CriadoEm { get; set; }
    public DateTimeOffset AtualizadoEm { get; set; }

    public void ToUml()
    {
        int maxPropLength = 0;
        int maxPropTypeLength = 0;

        foreach (var prop in this.GetType().GetProperties())
        {
            if (prop.Name.Length > maxPropLength) 
                maxPropLength = prop.Name.Length;

            if (prop.PropertyType.ToString().Split(".")[1].Length > maxPropTypeLength) 
                maxPropTypeLength = prop.PropertyType.ToString().Split(".").LastOrDefault().Length;
        }

        ConsoleEx.WriteDashedLine(maxPropLength + maxPropTypeLength + 7);

        Console.WriteLine();    

        Console.Write("| Classe: {0}", this.ToString().Split(".").LastOrDefault());

        Console.SetCursorPosition(maxPropLength + maxPropTypeLength + 6, Console.GetCursorPosition().Top);

        Console.WriteLine("|");

        ConsoleEx.WriteDashedLine(maxPropLength + maxPropTypeLength + 7);

        foreach (var prop in this.GetType().GetProperties())
        {

            Console.WriteLine();

            Console.Write("| {0}", prop.Name);

            Console.SetCursorPosition(maxPropLength + 3, Console.GetCursorPosition().Top);

            Console.Write("| {0}", prop.PropertyType.ToString().Split(".").LastOrDefault());

            Console.SetCursorPosition(maxPropLength + maxPropTypeLength + 6, Console.GetCursorPosition().Top);

            Console.Write("|");

        }

        Console.WriteLine();

        ConsoleEx.WriteDashedLine(maxPropLength + maxPropTypeLength + 7);
    }
}
