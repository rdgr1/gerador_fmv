from PIL    import Image,ImageFont,ImageDraw
import  datetime
fontCorpo = ImageFont .truetype(r"/home/rdgr/rd-Personal/gerador_fmv/assets/fonts/Inter_18pt-Regular.ttf",38)
meses = {
    1: "janeiro", 2: "fevereiro", 3: "março", 4: "abril",
    5: "maio", 6: "junho", 7: "julho", 8: "agosto",
    9: "setembro", 10: "outubro", 11: "novembro", 12: "dezembro"
}
campos_pil = {
    "nota":(730,578),
    "nome":(295,770),
    "endereco":(345,871),
    "cpf":(247,972),
    "tipo_servico":(55,1150),
    "valor_debito":(825,1150),
    "valor_credito":(1110,1150),
    "total":(),
    "valor_extenso":(),
    "data_vencimento":(),
    "data_hoje":(355,670),
}
data_atual = datetime.datetime.now()
data_nota = f"{data_atual.day}-{data_atual.year}"
data_hoje = f"{data_atual.day} de {meses[data_atual.month]} de {data_atual.year}"
nota_value = f"DÉBITO - {data_nota}"
nome = "Jessica Lemos"
endereco = "Rua SVJ Quadra 2 Bloco V"
cpf = "000.000.122-33"
tipo_servico = """Serviços Prestados – Prestação de Contas 
Curatela - Número do processo: 0743111-
70.2023.8.07.0016 – Samantha Kenia Abreu
Pereira – curadora de Ana Carolina dos 
Anjos Santiago"""
valor_debito = f"R$ 950"
notaImg = Image.open(r"/home/rdgr/rd-Personal/gerador_fmv/assets/imgs/png/Nota FMV.png").convert("RGB")
draw = ImageDraw.Draw(notaImg)
draw.text(campos_pil["nota"],nota_value,fill='black',font=fontCorpo)
draw.text(campos_pil["data_hoje"],data_hoje,fill='black',font=fontCorpo)
draw.text(campos_pil["nome"],nome,fill='black',font=fontCorpo)
draw.text((campos_pil["endereco"]),endereco,fill='black',font=fontCorpo)
draw.text(campos_pil["cpf"],cpf,fill='black',font=fontCorpo)
draw.text((campos_pil["tipo_servico"]),tipo_servico,fill='black',font=fontCorpo)
draw.text((campos_pil["valor_debito"]),valor_debito,fill='black',font=fontCorpo)

notaImg.save(f"Nota : {nome}.jpg")