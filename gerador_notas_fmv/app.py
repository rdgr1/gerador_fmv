import datetime
from pathlib import Path
import platform
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from PIL import Image, ImageFont, ImageDraw
from textwrap import fill as wrap_text
import os 
# Configuração de diretórios usando pathlib
BASE_DIR = Path(__file__).resolve().parent
NOTAS_DIR = BASE_DIR / "notas"
NOTAS_DIR.mkdir(exist_ok=True)
IS_WINDOWS = platform.system() == "Windows" and "MacOs"

# Uso
LOGO_ICO = Path ("/Users/rdgr777/rdPersonal/gerador_fmv/assets/imgs/png/logo.ico")
LOGO_IMG = Path ("/Users/rdgr777/rdPersonal/gerador_fmv/assets/imgs/png/Logo.png")
NOTA_IMG = Path('/Users/rdgr777/rdPersonal/gerador_fmv/assets/imgs/png/Nota-FMV.png')
FONT_PATH = Path ("/Users/rdgr777/rdPersonal/gerador_fmv/assets/fonts/Inter_18pt-Regular.ttf")

if not os.path.exists(FONT_PATH):
    print(f"⚠️ Arquivo de fonte não encontrado: {FONT_PATH}. Usando fonte padrão.")
    FONT_PATH = None  # Define como None para carregar fonte padrão depois
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
# Função para limpar e formatar valores monetários corretamente
def limpar_valor(valor_str):
    """ Remove 'R$', espaços e converte vírgula para ponto antes da conversão """
    valor_limpo = valor_str.replace("R$", "").replace(".", "").replace(",", ".").strip()
    try:
        return int(float(valor_limpo))  # Converte para float primeiro, depois para int
    except ValueError:
        return 0  # Retorna 0 caso a conversão falhe
# Função para desenhar texto quebrado em múltiplas linhas
def desenhar_texto_com_quebra(draw, posicao, texto, largura_max, font, fill="black"):
    """ Desenha o texto quebrando em múltiplas linhas para não sair da borda """
    texto_formatado = wrap_text(texto, width=largura_max)  # Quebra o texto em linhas menores
    draw.text(posicao, texto_formatado, font=font, fill=fill)
# Array Campos Imutáveis
campos = ['Nome Cliente:', 'CPF Cliente:', 'Endereço:', 'Tipo de Serviço:', 'Débito', 'Crédito', 'Data:', 'Data Vencimento:', 'CEP:','Valor']
campo_width = 275
campos_height = 35
button_width = 290
button_height = 50
campos_pil = {
    "nota":(730,578),
    "nome":(295,770),
    "endereco":(345,871),
    "cpf":(247,972),
    "tipo_servico":(140,1150),
    "valor_debito":(825,1150),
    "valor_credito":(1110,1150),
    "total":(247,1435),
    "valor_extenso":(247,1524),
    "data_vencimento":(530,1623),
    "data_hoje":(355,670)
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
if IS_WINDOWS and os.path.exists(LOGO_ICO):
    app.iconbitmap(bitmap=LOGO_ICO)
app.geometry('450x800+750+135')

# Criar um Frame com bordas arredondadas (já que a janela não tem suporte direto para corner_radius)
frame_principal = ctk.CTkFrame(app, width=450, height=825, corner_radius=15, fg_color='#272727')
frame_principal.pack()

if IS_WINDOWS and os.path.exists(LOGO_IMG):
    # Carregar a imagem usando Pillow
    logo_image = Image.open(LOGO_IMG)
    # Criar a imagem CustomTkinter com a imagem carregada
    logo_progama = ctk.CTkImage(light_image=logo_image, dark_image=logo_image, size=(150, 60))
    label_logo = ctk.CTkLabel(frame_principal, image=logo_progama, text='')
    label_logo.pack(pady=10)

font_path = FONT_PATH
font_family = 'Inter'

try:
    font = ctk.CTkFont(font_family, size=16, weight='normal')
    font_secondary = ctk.CTkFont(font_family, size=15, weight='normal')
except:
    font = ("Arial", 16)
    font_secondary = ("Arial", 15)

color_font = '#9ed22c'

# Função para emitir o recibo
def criar_nota():
    try:
        fontCorpo = ImageFont.truetype(FONT_PATH, 38) if FONT_PATH  else ImageFont.load_default()
    except OSError:
        print("⚠️ Erro ao carregar a fonte. Usando fonte padrão.")
        fontCorpo = ImageFont.truetype('Arial',38)

    notaImg = Image.open(NOTA_IMG).convert("RGB")
    draw = ImageDraw.Draw(notaImg)

    # Formatando Datas
    data_atual = datetime.datetime.now()
    data_hoje = f"{data_atual.day} de {meses[data_atual.month]} de {data_atual.year}"
    data_nota = f"{combo_box_debito_credito.get().upper()} {data_atual.day}-{data_atual.year}"
    draw.text(campos_pil["nota"], data_nota, fill='black', font=fontCorpo)
    draw.text(campos_pil["data_hoje"], data_hoje, fill='black', font=fontCorpo)
    draw.text(campos_pil["nome"], input_nome.get(), fill='black', font=fontCorpo)
    draw.text(campos_pil["endereco"], input_endereco.get('1.0', 'end-1c').strip(), fill='black', font=fontCorpo)
    draw.text(campos_pil["cpf"], input_cpf.get(), fill='black', font=fontCorpo)

    # Quebra de texto para Tipo de Serviço
    desenhar_texto_com_quebra(draw, campos_pil["tipo_servico"], input_servico.get(), largura_max=25, font=fontCorpo,
                              fill='black')

    # Obtém o valor selecionado no ComboBox
    tipo_pagamento = combo_box_debito_credito.get()

    # Escolhe a posição correta com base no valor selecionado
    if tipo_pagamento == "Débito":
        campos_credito_debito_pil = campos_pil["valor_debito"]
    else:
        campos_credito_debito_pil = campos_pil["valor_credito"]

    # Processamento do valor correto
    valor_formatado = limpar_valor(input_valor.get())

    draw.text(campos_credito_debito_pil, f"R$ {valor_formatado}", fill='black', font=fontCorpo)
    draw.text(campos_pil["total"], f"R$ {valor_formatado}", fill='black', font=fontCorpo)

    valor_extenso = numero_por_extenso(valor_formatado)
    draw.text(campos_pil["valor_extenso"], f"({valor_extenso} reais)", fill='black', font=fontCorpo)
    draw.text(campos_pil["data_vencimento"], input_data_vencimento.get(), fill='black', font=fontCorpo)

    caminho_nota = f"notas/Nota_{input_nome.get()}.jpg"
# Salvar a imagem no diretório "notas"
    try:
        notaImg.save(caminho_nota)
        if os.path.exists(caminho_nota):
            CTkMessagebox(title="Sucesso", message=f"Nota emitida para {input_nome.get()}!", icon="check")
        else:
            raise FileNotFoundError(f"Erro ao salvar a nota em {caminho_nota}")
    except Exception as e:
        CTkMessagebox(title="Erro", message=f"Falha ao emitir a nota: {e}", icon="cancel")
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
# Funçao para Formatar Valor
def limpar_valor(valor_str):

    """ Remove 'R$', espaços e converte vírgula para ponto antes da conversão """
    valor_limpo = valor_str.replace("R$", "").replace(".", "").replace(",", ".").strip()

    try:
        return int(float(valor_limpo))  # Converte para float primeiro, depois para int
    except ValueError:
        return 0  # Retorna 0 caso a conversão falhe

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
# Funçao para formatar Data Vencimento
def formatar_data_vencimento(event):
    texto = input_data_vencimento.get().replace("/", "")
    if len(texto) <= 2:
        input_data_vencimento.delete(0, ctk.END)
        input_data_vencimento.insert(0, texto)
    elif len(texto) <= 4:
        input_data_vencimento.delete(0, ctk.END)
        input_data_vencimento.insert(0, f"{texto[:2]}/{texto[2:]}")
    elif len(texto) <= 8:
        input_data_vencimento.delete(0, ctk.END)
        input_data_vencimento.insert(0, f"{texto[:2]}/{texto[2:4]}/{texto[4:]}")

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
input_data = ctk.CTkEntry(frame_principal, corner_radius=8, font=font_secondary, placeholder_text_color='#FFFFFF', fg_color=fg_color, border_color=border_color, border_width=2, width=campo_width, height=campos_height, placeholder_text='Insira a Data')

# Bind para formatar a Data enquanto digita
input_data.bind("<KeyRelease>", formatar_data)
input_data.pack()

label_data_vencimento = ctk.CTkLabel(frame_principal, corner_radius=8, font=font, width=campo_width, height=campos_height, text=campos[7], text_color=color_font, anchor='w')
label_data_vencimento.pack()

input_data_vencimento = ctk.CTkEntry(frame_principal, corner_radius=8, font=font_secondary, placeholder_text_color='#FFFFFF', fg_color=fg_color, border_color=border_color, border_width=2, width=campo_width, height=campos_height, placeholder_text='Insira a Data de Vencimento')
input_data_vencimento.bind("<KeyRelease>", formatar_data_vencimento)
input_data_vencimento.pack()

label_valor = ctk.CTkLabel(frame_principal,corner_radius=8,font=font,width=campo_width,height=campos_height,text_color=color_font,text=campos[9],anchor='w')
label_valor.pack()
input_valor = ctk.CTkEntry(frame_principal,corner_radius=8,font=font,width=campo_width,height=campos_height,placeholder_text_color='#FFFFFF',fg_color=fg_color,border_color=border_color,border_width=2,placeholder_text='Insira o Valor da Nota')
input_valor.pack()
button_salvar = ctk.CTkButton(frame_principal, width=button_width, corner_radius=8, height=button_height, fg_color='transparent', text_color=color_font, text='Salvar', font=font, border_color=color_font, border_width=2, hover_color='#5d7528',command=criar_nota)
button_salvar.pack(pady=25)
app.update_idletasks()
app.update()
app.mainloop()