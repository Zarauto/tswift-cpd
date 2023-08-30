import tkinter as tk
from tkinter import scrolledtext
from tkinter import filedialog

# Função para abrir um arquivo e exibir seu conteúdo no widget de rolagem
def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            text_widget.delete('1.0', tk.END)  # Limpar o conteúdo atual
            text_widget.insert(tk.END, content)  # Inserir o novo conteúdo

# Função para processar a entrada do usuário e exibir opções
def process_input():
    input_text = input_entry.get("1.0", tk.END).strip()
    options_text = ""

    if input_text:
        # Processar a entrada do usuário para gerar opções
        options_text = f"Opção 1: {input_text.upper()}\nOpção 2: {input_text.lower()}"

    options_widget.delete('1.0', tk.END)
    options_widget.insert(tk.END, options_text)

# Função para exibir o conteúdo de uma opção selecionada em uma nova janela
def show_selected_option():
    selected_option = options_widget.get("1.0", tk.END).strip()
    if selected_option.startswith("Opção 1:"):
        open_file()

# Criar a janela principal
root = tk.Tk()
root.title("Aplicativo Interativo")

# Criar widgets para entrada e processamento
input_label = tk.Label(root, text="Digite uma string:")
input_label.pack(pady=5)

input_entry = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=3)
input_entry.pack(padx=10, pady=5)

process_button = tk.Button(root, text="Processar", command=process_input)
process_button.pack(pady=5)

# Criar widget para exibir opções
options_widget = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=5)
options_widget.pack(padx=10, pady=5)

# Botão para abrir opção selecionada
open_option_button = tk.Button(root, text="Abrir Opção", command=show_selected_option)
open_option_button.pack(pady=5)

# Iniciar o loop de eventos
root.mainloop()