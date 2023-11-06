import tkinter as tk
from pytube import YouTube

# Função para baixar o vídeo
def baixar_video():
    url_do_video = entrada_url.get()
    try:
        yt = YouTube(url_do_video)
        stream = yt.streams.get_highest_resolution()
        stream.download()
        rotulo_status.config(text="Download concluído")
    except Exception as e:
        rotulo_status.config(text=f"Erro: {str(e)}")

# Configuração da janela
janela = tk.Tk()
janela.title("Instalador de Vídeos MP4")

# Rótulo e entrada para o link do vídeo
rotulo_url = tk.Label(janela, text="Digite o link do vídeo:")
rotulo_url.pack()
entrada_url = tk.Entry(janela)
entrada_url.pack()

# Botão de download
botao_baixar = tk.Button(janela, text="Baixar Vídeo", command=baixar_video)
botao_baixar.pack()

# Rótulo para exibir o status
rotulo_status = tk.Label(janela, text="")
rotulo_status.pack()

janela.mainloop()
