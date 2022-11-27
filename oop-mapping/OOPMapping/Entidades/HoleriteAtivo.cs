namespace OOPMapping.Entidades;

public class HoleriteAtivo : Holerite
{
    public string Cargo { get; set; }
    public string HorasExtras { get; set; }
    public string Funcao { get; set; }
    public string RemuneracaoBase { get; set; }
    public string Comissao { get; set; }
    public string Beneficios { get; set; }
    public int ServidorAtivoId { get; set; }
    public ServidorAtivo ServidorAtivo { get; set; }
}
