import yt_dlp
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox

def baixar_conteudo(url, tipo, pasta):
    try:
        if tipo == "Áudio":
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'outtmpl': f'{pasta}/%(title)s.%(ext)s',  # Nome do arquivo de saída
            }
        else:
            ydl_opts = {
                'format': 'bestvideo+bestaudio/best',
                'merge_output_format': 'mp4',
                'outtmpl': f'{pasta}/%(title)s.%(ext)s',
            }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Sucesso", "Download concluído!")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

def main():
    # Configurar interface
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal

    # Perguntar URL do vídeo
    video_url = simpledialog.askstring("URL do Vídeo", "Insira a URL do vídeo:")
    if not video_url:
        messagebox.showwarning("Atenção", "Nenhuma URL fornecida.")
        return

    # Perguntar se deseja baixar áudio ou vídeo
    tipo = messagebox.askquestion("Escolha", "Deseja baixar apenas o áudio?", icon='question')
    tipo = "Áudio" if tipo == "yes" else "Vídeo"

    # Perguntar pasta de destino
    pasta_destino = filedialog.askdirectory(title="Escolha a pasta de destino")
    if not pasta_destino:
        messagebox.showwarning("Atenção", "Nenhuma pasta selecionada.")
        return

    # Baixar conteúdo
    baixar_conteudo(video_url, tipo, pasta_destino)

if __name__ == "__main__":
    main()