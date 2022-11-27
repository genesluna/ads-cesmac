namespace OOPMapping.Entidades;

public class ServidorAtivo : Servidor
{
    public string Cargo { get; set; }
    public string Funcao { get; set; }
    public Orgao Orgao { get; set; }
    public int OrgaoId { get; set; }
    public List<HoleriteAtivo> Holerites { get; set; }
}
