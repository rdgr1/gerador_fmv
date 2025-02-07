import datetime
import os
import customtkinter as ctk
from PIL import Image, ImageFont, ImageDraw



##os.environ['TK_USE_RENDERER'] = 'directwrite'
# Funcao Número por extenso
def numero_por_extenso(n):
    if n < 0 or n > 999999:
        return "Número fora do intervalo suportado (0 a 999999)"

    unidades = ["", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
    especiais = ["dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
    dezenas = ["", "dez", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
    centenas = ["", "cento", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seiscentos", "setecentos",
                "oitocentos", "novecentos"]

    def converter_ate_999(num):
        if num == 100:
            return "cem"
        elif num == 0:
            return "zero"

        partes = []
        c, d, u = num // 100, (num % 100) // 10, num % 10

        if c > 0:
            partes.append(centenas[c])

        if d == 1:  # Caso especial de 10 a 19
            partes.append(especiais[u])
        else:
            if d > 0:
                partes.append(dezenas[d])
            if u > 0:
                partes.append(unidades[u])

        return " e ".join([p for p in partes if p])  # Remove vazios e adiciona "e" onde necessário

    if n == 0:
        return "zero"

    partes_final = []

    milhar, resto = divmod(n, 1000)

    if milhar > 0:
        if milhar == 1:
            partes_final.append("mil")
        else:
            partes_final.append(converter_ate_999(milhar) + " mil")

    if resto > 0:
        if milhar > 0 and resto < 100:  # Adiciona "e" entre milhares e unidades/dezenas
            partes_final.append("e")
        partes_final.append(converter_ate_999(resto))

    return " ".join(partes_final)
# Array Campos Imutáveis
campos = ['Nome Cliente:', 'CPF Cliente:', 'Endereço:', 'Tipo de Serviço:', 'Débito', 'Crédito', 'Data:', 'Data Vencimento:', 'CEP:']
campo_width = 275
campos_height = 35
button_width = 290
button_height = 50
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
meses = {
    1: "janeiro", 2: "fevereiro", 3: "março", 4: "abril",
    5: "maio", 6: "junho", 7: "julho", 8: "agosto",
    9: "setembro", 10: "outubro", 11: "novembro", 12: "dezembro"
}
# Configurando Aparência:
ctk.set_appearance_mode('dark')
border_color = '#7E7E7E'
fg_color = '#535353'

# Criar a janela Principal
app = ctk.CTk()
app.title('Gerador de Nota Física')
app.iconbitmap(bitmap='/Users/rdgr777/rdPersonal/gerador_fmv/assets/imgs/png/logo.ico')
app.geometry('450x825+750+105')

# Criar um Frame com bordas arredondadas (já que a janela não tem suporte direto para corner_radius)
frame_principal = ctk.CTkFrame(app, width=450, height=825, corner_radius=15, fg_color='#272727')
frame_principal.pack_propagate(False)  # Impede que o tamanho do frame se ajuste ao tamanho dos widgets
frame_principal.pack()

# Carregar a imagem usando Pillow
logo_image = Image.open("/Users/rdgr777/rdPersonal/gerador_fmv/assets/imgs/png/Logo.png")
# Criar a imagem CustomTkinter com a imagem carregada
logo_progama = ctk.CTkImage(light_image=logo_image, dark_image=logo_image, size=(300, 100))
label_logo = ctk.CTkLabel(frame_principal, image=logo_progama, text='')
label_logo.pack(pady=10)

font_path = 'assets/fonts/Inter_18pt-Regular.ttf'
font_family = 'Inter'

try:
    font = ctk.CTkFont(font_family, size=16, weight='normal')
    font_secondary = ctk.CTkFont(font_family, size=15, weight='normal')
except:
    font = ("Arial", 16)
    font_secondary = ("Arial", 15)

color_font = '#9ed22c'
# Função para Emitir Recibo
def criar_nota():
    notaImg = Image.open(r"/Users/rdgr777/rdPersonal/gerador_fmv/assets/imgs/png/Nota FMV.png").convert("RGB")
    draw = ImageDraw.Draw(notaImg)
    # Formatando Datas
    data_atual = datetime.datetime.now()
    data_hoje = f"{data_atual.day} de {meses[data_atual.month]} de {data_atual.year}"
    data_nota = f"{data_atual.day}-{data_atual.year}"
    draw.text(campos_pil["data_hoje"], data_hoje, fill='black', font=font)
    draw.text(campos_pil["nome"], input_nome.get(), fill='black', font=font)
    draw.text((campos_pil["endereco"]), input_endereco.get(), fill='black', font=font)
    draw.text(campos_pil["cpf"], input_cpf.get(), fill='black', font=font)
    draw.text((campos_pil["tipo_servico"]), input_servico.get(), fill='black', font=font)
    draw.text((campos_pil["valor_debito"]), combo_box_debito_credito.get(), fill='black', font=font)
    draw.text(campos_pil["total"], valor_debito, fill='black', font=font)
    draw.text(campos_pil["valor_extenso"], valor_extenso, fill='black', font=font)
    draw.text(campos_pil["data_vencimento"], data_vencimento, fill='black', font=font)
    notaImg.save(f"Nota : {nome}.jpg")
# Função para formatar CPF
def formatar_cpf(event):
    texto = input_cpf.get().replace(".", "").replace("-", "")
    if len(texto) <= 3:
        input_cpf.delete(0, ctk.END)
        input_cpf.insert(0, texto)
    elif len(texto) <= 6:
        input_cpf.delete(0, ctk.END)
        input_cpf.insert(0, f"{texto[:3]}.{texto[3:]}")
    elif len(texto) <= 9:
        input_cpf.delete(0, ctk.END)
        input_cpf.insert(0, f"{texto[:3]}.{texto[3:6]}.{texto[6:]}")
    elif len(texto) <= 11:
        input_cpf.delete(0, ctk.END)
        input_cpf.insert(0, f"{texto[:3]}.{texto[3:6]}.{texto[6:9]}-{texto[9:]}")

# Função para formatar CEP
def formatar_cep(event):
    texto = input_cep.get().replace("-", "")
    if len(texto) <= 5:
        input_cep.delete(0, ctk.END)
        input_cep.insert(0, texto)
    elif len(texto) <= 8:
        input_cep.delete(0, ctk.END)
        input_cep.insert(0, f"{texto[:5]}-{texto[5:]}")

# Função para formatar Data
def formatar_data(event):
    texto = input_data.get().replace("/", "")
    if len(texto) <= 2:
        input_data.delete(0, ctk.END)
        input_data.insert(0, texto)
    elif len(texto) <= 4:
        input_data.delete(0, ctk.END)
        input_data.insert(0, f"{texto[:2]}/{texto[2:]}")
    elif len(texto) <= 8:
        input_data.delete(0, ctk.END)
        input_data.insert(0, f"{texto[:2]}/{texto[2:4]}/{texto[4:]}")
# Campos
label_nome = ctk.CTkLabel(frame_principal, corner_radius=8, width=campo_width, height=campos_height, text=campos[0], text_color=color_font, anchor='w', font=font)
label_nome.pack()
input_nome = ctk.CTkEntry(frame_principal, corner_radius=8, font=font_secondary, placeholder_text_color='#FFFFFF', fg_color=fg_color, border_color=border_color, border_width=2, width=campo_width, height=campos_height, placeholder_text='Insira o nome')
input_nome.pack()

label_cpf = ctk.CTkLabel(frame_principal, corner_radius=8, font=font, width=campo_width, height=campos_height, text=campos[1], text_color=color_font, anchor='w')
label_cpf.pack()

# Campo CPF com a máscara
input_cpf = ctk.CTkEntry(frame_principal, corner_radius=8, font=font_secondary, placeholder_text_color='#FFFFFF', fg_color=fg_color, border_color=border_color, border_width=2, width=campo_width, height=campos_height, placeholder_text='Insira o CPF')

# Bind para formatar o CPF enquanto digita
input_cpf.bind("<KeyRelease>", formatar_cpf)

input_cpf.pack()

label_cep = ctk.CTkLabel(frame_principal, corner_radius=8, font=font, width=campo_width, height=campos_height, text=campos[8], text_color=color_font, anchor='w')
label_cep.pack()

# Campo CEP com a máscara
input_cep = ctk.CTkEntry(frame_principal, corner_radius=8, font=font_secondary, placeholder_text_color='#FFFFFF', fg_color=fg_color, border_color=border_color, border_width=2, width=campo_width, height=campos_height, placeholder_text='Insira o CEP')

# Bind para formatar o CEP enquanto digita
input_cep.bind("<KeyRelease>", formatar_cep)

input_cep.pack()

label_endereco = ctk.CTkLabel(frame_principal, corner_radius=8, font=font, width=campo_width, height=campos_height, text=campos[2], text_color=color_font, anchor='w')
label_endereco.pack()

input_endereco = ctk.CTkTextbox(frame_principal, corner_radius=8, width=campo_width, height=60, wrap="word", fg_color=fg_color, border_color=border_color, text_color='#FFFFFF', border_width=2, font=font_secondary)
input_endereco.pack()

label_servico = ctk.CTkLabel(frame_principal, corner_radius=8, font=font, width=campo_width, height=campos_height, text=campos[3], text_color=color_font, anchor='w')
label_servico.pack()

input_servico = ctk.CTkEntry(frame_principal, corner_radius=8, font=font_secondary, placeholder_text_color='#FFFFFF', fg_color=fg_color, border_color=border_color, border_width=2, width=campo_width, height=campos_height, placeholder_text='Insira o Tipo de Serviço')
input_servico.pack()

label_debito_credito = ctk.CTkLabel(frame_principal, corner_radius=8, font=font, width=campo_width, height=campos_height, text='Tipo de Nota', text_color=color_font, anchor='w')
label_debito_credito.pack()

combo_box_debito_credito = ctk.CTkComboBox(frame_principal, dropdown_font=font, dropdown_text_color='#FFFFFF', dropdown_fg_color=fg_color, dropdown_hover_color='#5d7528', corner_radius=8, width=campo_width, height=campos_height, values=[campos[4], campos[5]], fg_color=fg_color, border_color=border_color, text_color='#FFFFFF', font=font_secondary)
combo_box_debito_credito.pack()

label_data = ctk.CTkLabel(frame_principal, corner_radius=8, font=font, width=campo_width, height=campos_height, text=campos[6], text_color=color_font, anchor='w')
label_data.pack()

# Campo Data com a máscara
input_data = ctk.CTkEntry(frame_principal, corner_radius=8, font=font_secondary, placeholder_text_color='#FFFFFF', fg_color=fg_color, border_color=border_color, border_width=2, width=campo_width, height=campos_height, placeholder_text='Insira a Data XX/XXXX')

# Bind para formatar a Data enquanto digita
input_data.bind("<KeyRelease>", formatar_data)
input_data.pack()

label_data_vencimento = ctk.CTkLabel(frame_principal, corner_radius=8, font=font, width=campo_width, height=campos_height, text=campos[7], text_color=color_font, anchor='w')
label_data_vencimento.pack()

input_data_vencimento = ctk.CTkEntry(frame_principal, corner_radius=8, font=font_secondary, placeholder_text_color='#FFFFFF', fg_color=fg_color, border_color=border_color, border_width=2, width=campo_width, height=campos_height, placeholder_text='Insira a Data de Vencimento XX/XXXX')
input_data_vencimento.bind("<KeyRelease>", formatar_data)
input_data_vencimento.pack()

button_salvar = ctk.CTkButton(frame_principal, width=button_width, corner_radius=8, height=button_height, fg_color='transparent', text_color=color_font, text='Salvar', font=('SF Pro Display', 18), border_color=color_font, border_width=2, hover_color='#5d7528')
button_salvar.pack(pady=25)

app.update_idletasks()
app.update()
app.mainloop()