import tkinter as tk
from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import messagebox
from random import randint
from tkinter.scrolledtext import *
from PIL import ImageTk, Image





def regras():
    regras = """
        ---------Bem-vindo ao Craps------

        Craps é um jogo de dois dados com o objetivo de tirar um somatório específico na jogada inicial ou, em caso de outros valores, você pode continuar e ter a chance de vencer.

        Regras:
        1 - Seu objetivo inicial é tirar um 7 ou 11.
        2 - Em caso de um 2, 3 ou 12, você automaticamente perde.
        3 - Em caso de um 4, 5, 6, 8, 9 ou 10, você continua jogando até tirar o mesmo número novamente.
        4 - Se tirar um 7 antes de tirar o mesmo número, você perde.
        """

    janela_regras = tk.Toplevel()
    janela_regras.title("Regras do Craps")

    caixa_texto = tk.Text(janela_regras, wrap=tk.WORD)
    caixa_texto.pack()
    caixa_texto.insert("0.0", regras)
    caixa_texto['state'] = 'disabled'


def change_color():
    colors = askcolor(title="Tkinter Color Chooser")
    root.configure(bg=colors[1])
    # tk.Button.configure(root, fg=colors[1])
    ScrolledText.configure(root,bg=colors[1])


class jogo:
    def __init__(self):
        self.vitoria = 0
        self.derrota = 0


    def craps(self, caixa_texto):

        caixa_texto.configure(state='normal')
        rolagem_1 = self.dados()
        rolagem_2 = self.dados()
        soma = rolagem_1 + rolagem_2
        caixa_texto.insert(tk.END, f"Soma: {soma}\n\n")
        caixa_texto.yview(tk.END)
        if(soma in(7,11)):

            caixa_texto.insert(tk.END, "Parabéns você venceu!!!\n\n")
            caixa_texto.yview(tk.END)
            self.vitoria+=1

            # print("soma {}".format(rolagem_1+rolagem_2))
            # print("Parabéns você venceu!!!!")


        elif (soma in(2,3,12)):

            caixa_texto.insert(tk.END,"Que pena você perdeu na primeira rodada :(\n\n")
            caixa_texto.yview(tk.END)
            self.derrota+=1



        else :
            # caixa_texto.insert(tk.END, f"Soma: {soma}\n")
            caixa_texto.insert(tk.END, "Continue Jogando até tirar o mesmo número para vencer\n\n")
            caixa_texto.yview(tk.END)

            while True:
                rolagem_1 = self.dados()
                rolagem_2 = self.dados()
                soma_02 = rolagem_1 + rolagem_2

                if soma_02 == soma:
                    caixa_texto.insert(tk.END, f"Você tirou um {soma} novamente. Você ganhou!\n\n")
                    caixa_texto.yview(tk.END)
                    self.vitoria+=1
                    break
                elif soma_02 == 7:
                    caixa_texto.insert(tk.END,"Você tirou um 7. Você perdeu!\n\n")
                    caixa_texto.yview(tk.END)
                    self.derrota+=1
                    break
                else:
                    caixa_texto.insert(tk.END, f"Soma: {soma_02}\n\n")
                    caixa_texto.insert(tk.END, "Você continua jogando...\n\n")
                    caixa_texto.yview(tk.END)
        caixa_texto.insert(tk.END,
                           "___________________________________________________________________________________________\n\n")
        caixa_texto.configure(state='disabled')

    def dados(self):
        return randint(1,6)

    @property

    @property
    def soma_vitoria(self):
        self.vitoria += 1

    @property
    def soma_derrota(self):
        self.derrota += 1

    def placar(self):
        string = (f"Vitória: {self.vitoria}\n"
                  f"Derrota: {self.derrota}")
        messagebox.showinfo("Placar",string)
        return print("Vitória: {} \nDerrota: {}".format(self.vitoria, self.derrota))



if(__name__ == "__main__"):

    root = tk.Tk()
    root.title('Craps')
    root.geometry('800x600')
    # root.resizable(False, False)
    root.configure(background="black")
    root.maxsize(width=850, height=700)
    root.minsize(width=400, height=300)


    # root.columnconfigure(0,weight=2)
    # root.rowconfigure(3, weight=3)

    jogar = jogo()

    image = Image.open("dados.jpg")
    imagem = image.resize((400, 520), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(imagem)





    frame1 = tk.Frame(root, borderwidth=4, bg= "#fff",
                        highlightbackground="blue", highlightthickness=3)
    frame1.place(relx=0.25, rely=0.02, relwidth=0.50, relheight=0.40)

    frame2 = Frame(root, bd=4, bg="#fff",
                        highlightbackground="#317535", highlightthickness=3)
    frame2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    label_imagem = tk.Label(frame1, image=photo)
    label_imagem.pack()
    label_imagem.config(image=photo)


    botao_regras = tk.Button(frame1, text="Regras", command=regras, width=20)
    # botao_regras.grid(column=0, row=1, pady=(0,15), padx=(0,100))
    botao_regras.place(relx=0.02, rely=0.1, relwidth=0.22, relheight=0.15)

    botao_pontuacao = tk.Button(frame1, text="Pontuação", command=lambda: jogar.placar(), width=15)
    # botao_pontuacao.grid(column=1, row=1, pady=(0, 15))
    botao_pontuacao.place(relx=0.73, rely=0.1, relwidth=0.22, relheight=0.15)

    selecao_cor = tk.Button(frame1,text='Cor de fundo',command=change_color,width=15)
    # selecao_cor.grid(column=0, row=2,padx=(0, 100))
    selecao_cor.place(relx=0.02, rely=0.80, relwidth=0.25, relheight=0.15)

    botao_jogar = tk.Button(frame1, text="Lançar Dados", command=lambda: jogar.craps(caixa_texto),width=15)
    # botao_jogar.grid(column=1, row=2)
    botao_jogar.place(relx=0.36, rely=0.43, relwidth=0.25, relheight=0.15)

    caixa_texto = ScrolledText(frame2, width=50, height=22)
    # caixa_texto.grid(column=0, row=3, rowspan=3, columnspan=3)
    caixa_texto.place(relx=0.0, rely=0.1, relwidth=1, relheight=0.8)
    caixa_texto.configure(state='disabled')

    botao_close = tk.Button(frame1, text="Sair", command=lambda :root.destroy(), width=20)
    # botao_close.grid(column=1, row = 7,)
    botao_close.place(relx=0.73, rely=0.80, relwidth=0.22, relheight=0.15)


    root.mainloop()



