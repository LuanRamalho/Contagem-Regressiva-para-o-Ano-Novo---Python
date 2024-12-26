import tkinter as tk
from datetime import datetime, timedelta


def update_timer():
    now = datetime.now()
    target_date = datetime(2025, 1, 1, 0, 0, 0)
    time_left = target_date - now
    
    if time_left.total_seconds() > 0:
        days, seconds = divmod(time_left.total_seconds(), 86400)
        hours, seconds = divmod(seconds, 3600)
        minutes, seconds = divmod(seconds, 60)
        countdown_label.config(
            text=f"{int(days)} dias\n{int(hours)} horas\n{int(minutes)} minutos\n{int(seconds)} segundos"
        )
        root.after(1000, update_timer)
    else:
        countdown_label.config(text="Feliz Ano Novo 2025!")


# Configuração da janela principal
root = tk.Tk()
root.title("Contagem Regressiva para 2025")
root.geometry("500x400")
root.configure(bg="black")

# Título do aplicativo
title_label = tk.Label(
    root,
    text="Contagem Regressiva para o Ano Novo de 2025",
    font=("Helvetica", 16, "bold"),
    fg="yellow",
    bg="black",
)
title_label.pack(pady=20)

# Label de contagem regressiva
countdown_label = tk.Label(
    root,
    text="Calculando...",
    font=("Helvetica", 30, "bold"),
    fg="cyan",
    bg="black",
)
countdown_label.pack(pady=50)

# Rodapé
footer_label = tk.Label(
    root,
    text="Prepare-se para celebrar!",
    font=("Helvetica", 12, "italic"),
    fg="green",
    bg="black",
)
footer_label.pack(side="bottom", pady=10)

# Inicializa a contagem regressiva
update_timer()

# Inicia o loop da interface gráfica
root.mainloop()
