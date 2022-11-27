using OOPMapping.Entidades;

var orgao = new Orgao();
var servidorAtivo = new ServidorAtivo();
var servidorInativo = new ServidorInativo();
var holeriteAtivo = new HoleriteAtivo();
var holeriteInativo = new HoleriteInativo();


orgao.ToUml();
Console.WriteLine();
servidorAtivo.ToUml();
Console.WriteLine();
servidorInativo.ToUml();
Console.WriteLine();
holeriteAtivo.ToUml();
Console.WriteLine();
holeriteInativo.ToUml();