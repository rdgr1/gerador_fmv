import os
import ctypes
import customtkinter as ctk
from customtkinter import CTkEntry, CTkLabel
from PIL import Image, ImageFont

os.environ['TK_USE_RENDERER'] = 'directwrite'
ctypes.windll.shcore.SetProcessDpiAwareness(1)

# Array Campos Imutáveis
campos = ['Nome Cliente:', 'CPF Cliente:', 'Endereço:', 'Tipo de Serviço:', 'Débito', 'Crédito', 'Data:', 'Data Vencimento:', 'CEP:']
campo_width = 275
campos_height = 35
button_width = 290
button_height = 50

# Configurando Aparência:
ctk.set_appearance_mode('dark')
border_color = '#7E7E7E'
fg_color = '#535353'

# Criar a janela Principal
app = ctk.CTk()
app.title('Gerador de Nota Física')
app.iconbitmap(bitmap=r'C:\Users\GustavinGG\Documents\gerador_fmv\assets\imgs\png\logo.ico')
app.geometry('450x825+750+105')

# Criar um Frame com bordas arredondadas (já que a janela não tem suporte direto para corner_radius)
frame_principal = ctk.CTkFrame(app, width=450, height=825, corner_radius=15, fg_color='#272727')
frame_principal.pack_propagate(False)  # Impede que o tamanho do frame se ajuste ao tamanho dos widgets
frame_principal.pack()

# Carregar a imagem usando Pillow
logo_image = Image.open(r'C:\Users\GustavinGG\Documents\gerador_fmv\assets\imgs\png\Logo.png')
# Criar a imagem CustomTkinter com a imagem carregada
logo_progama = ctk.CTkImage(light_image=logo_image, dark_image=logo_image, size=(300, 100))
label_logo = ctk.CTkLabel(frame_principal, image=logo_progama, text='')
label_logo.pack(pady=10)

font = ctk.CTkFont('SF Pro Display', size=16 , weight='normal')
font_secondary = ctk.CTkFont('SF Pro Display', size=15 , weight='normal')
color_font = '#9ed22c'

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

app.mainloop()
