import customtkinter as ctk
from customtkinter import CTkEntry, CTkLabel
from PIL import Image
# Array Campos Imutaveis
campos = ['Nome Cliente:','CPF Cliente:','Endereco:','Tipo de Servico:','Debito','Credito','Data:','Data Vencimento:']
campo_width =  250
campos_height = 30
# Configurando Aparencia:
ctk.set_appearance_mode('dark')
# Criar a janela Principal
app = ctk.CTk()
app.title('Gerador de Nota Fisica')
app.iconbitmap(bitmap=r'C:\Users\GustavinGG\Documents\gerador_fmv\assets\imgs\png\logo.ico')
app.geometry('400x725+750+200')
# Carregar a imagem usando Pillow
logo_image = Image.open(r'C:\Users\GustavinGG\Documents\gerador_fmv\assets\imgs\png\Logo.png')
# Criar a imagem CustomTkinter com a imagem carregada
logo_progama = ctk.CTkImage(light_image=logo_image,dark_image=logo_image, size=(300,91))
label_logo = ctk.CTkLabel(app,image=logo_progama,text='')
label_logo.pack(pady=10)
ctk.CTkFont('SF Pro Display',size=16)
color_font = '#9ed22c'
# Campos
label_nome = ctk.CTkLabel(app,width=campo_width,height=campos_height,text=campos[0], text_color=color_font,anchor='w')
label_nome.pack(pady=10)
input_nome = ctk.CTkEntry(app,width=campo_width,height=campos_height,placeholder_text='Insira o nome')
input_nome.pack()
label_cpf = ctk.CTkLabel(app,width=campo_width,height=campos_height,text=campos[1],text_color=color_font,anchor='w')
label_cpf.pack()
input_cpf = ctk.CTkEntry(app,width=campo_width,height=campos_height,placeholder_text='Insira o CPF')
input_cpf.pack()
label_endereco = ctk.CTkLabel(app,width=campo_width,height=campos_height,text=campos[2],text_color=color_font,anchor='w')
label_endereco.pack()
# Criando o Textbox com quebra automática de linha
input_endereco = ctk.CTkTextbox(app, width=campo_width, height=60, wrap="word")
input_endereco.pack()
label_servico = ctk.CTkLabel(app,width=campo_width,height=campos_height,text=campos[3],text_color=color_font,anchor='w')
label_servico.pack()
input_servico = ctk.CTkEntry(app,width=campo_width,height=campos_height,placeholder_text='Insira o Tipo de Servico')
input_servico.pack()
label_debito_credito = CTkLabel(app,width=campo_width,height=campos_height,text='Tipo de Nota',text_color=color_font,anchor='w')
label_debito_credito.pack()
combo_box_debito_credito = ctk.CTkComboBox(app,width=campo_width,height=campos_height,values=[campos[4],campos[5]])
combo_box_debito_credito.pack()
label_data = ctk.CTkLabel(app,width=campo_width,height=campos_height,text=campos[6],text_color=color_font,anchor='w')
label_data.pack()
input_data = ctk.CTkEntry(app,width=campo_width,height=campos_height,placeholder_text='Insira a Data')
input_data.pack()
label_data_vencimento = ctk.CTkLabel(app,width=campo_width,height=campos_height,text=campos[7],text_color=color_font,anchor='w')
label_data_vencimento.pack()
input_data_vencimento = ctk.CTkEntry(app,width=campo_width,height=campos_height,placeholder_text='Insira a Data de Vencimento')
input_data_vencimento.pack()
label_aviso = ctk.CTkLabel(app,width=campo_width,height=campos_height,text='Caso os Campos de Data Forem Vazios Teram a Data de Hoje !',text_color='red',wraplength=250)
label_aviso.pack(pady=10)
button_salvar = ctk.CTkButton(app,width=campo_width,height=campos_height,fg_color=color_font,text_color='white',text='Salvar')
button_salvar.pack(pady=25)
app.mainloop()