from tkinter import *
import pygame

pygame.mixer.init()

musicas = ['musica_1.mp3', 'musica_2.mp3', 'musica_3.mp3', 'musica_4.mp3', 'musica_5.mp3']

#Classe Tela
class Tela:
    def __init__(self):
        self.root = root
        self.configura_Tela()
        self.widgets()
        root.mainloop()
    def configura_Tela(self):
        self.root.configure(bg='#353535')
        self.root.geometry('400x600')
    def widgets(self):
        self.imagem = PhotoImage(file='foto.png')
        self.img_Principal = Label(self.root, image=self.imagem)
        self.img_Principal.place(x=105, y=120, height = 250, width= 190)

        #Botôes-------------------------------------------------------------------------------
        #tocar
        self.tocar = Button(self.root, command=self.tocar1, text='play')
        self.tocar.place(x = 150, y = 475)
        #pausar
        self.pausa = Button(self.root, command=self.pausa1, text='pause')
        self.pausa.place(x=200, y = 475)
        #prox musica
        self.prox = Button(self.root, command=self.prox1, text='proxima')
        self.prox.place(x=300,y=475)
        #voltar musica
        self.ant = Button(self.root, command= self.ant1, text='anterior')
        self.ant.place(x= 50, y=475)

    def tocar1(self):
        print('Tocar1 funcionando!')
        pygame.mixer.music.load(musicas[0])
        pygame.mixer.music.play()
    def pausa1(self):
        print('\033[34mPausa1 Funcionando!\033[m')
        pygame.mixer.music.pause()
    def prox1(self):
        print('\033[31mprox funcionando!\033[m')
        global musicas
        musicas = musicas[1:] + [musicas[0]] #move a música atual para o final da lista
    def ant1(self):
        print('\033[33mant funcionando!\033[m')
        global musicas
        musicas = [musicas[4]] + musicas[:4]
root = Tk()
Tela()