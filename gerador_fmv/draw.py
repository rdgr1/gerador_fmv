from PIL    import Image,ImageFont,ImageDraw
import  datetime
fontCorpo = ImageFont .truetype(r"/Users/rdgr777/rdPersonal/gerador_fmv/assets/fonts/Inter_18pt-Regular.ttf",38)




campos_pil = {
    "nota":(730,578),
    "nome":(295,770),
    "endereco":(345,871),
    "cpf":(247,972),
    "tipo_servico":(55,1150),
    "valor_debito":(825,1150),
    "valor_credito":(1110,1150),
    "total":(247,1435),
    "valor_extenso":(247,1524),
    "data_vencimento":(530,1623),
    "data_hoje":(355,670),
}
data_atual = datetime.datetime.now()
nota_value = f"DÉBITO - {data_nota}"
nome = "Jessica Lemos"
endereco = "Rua SVJ Quadra 2 Bloco V"
cpf = "000.000.122-33"
tipo_servico = """Serviços Prestados – Prestação de Contas 
Curatela - Número do processo: 0743111-
70.2023.8.07.0016 – Samantha Kenia Abreu
Pereira – curadora de Ana Carolina dos 
Anjos Santiago"""
valor = 950
valor_debito = f"R$ {valor}"
valor_extenso = f"({numero_por_extenso(valor)} reais)"
data_vencimento = "27/08/2025"
