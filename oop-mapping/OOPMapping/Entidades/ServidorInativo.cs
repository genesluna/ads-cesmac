namespace OOPMapping.Entidades;

public class ServidorInativo : Servidor
{
    public string Vinculo { get; set; }
    public List<HoleriteInativo> Holerites { get; set; }
}
