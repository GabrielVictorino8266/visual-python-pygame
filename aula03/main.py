import pygame

# _teste = "Ola"

# print(_teste)

#Inicializa o pygame
pygame.init()

janela = pygame.display.set_mode((500,500))
#Define o título da janela para "Formas"
pygame.display.set_caption("Formas")

#define as cores usadas nas formas
azul = (0,0,255)
vermelho = (255,0,0)
verde = (0,255,0)

#Define as dimensões das formas
largura = 200
altura = 200

#Define as posicoes
x=50
y=0


run = True
#Run sempre é verdadeiro, logo o While sempre repetirá
while run:

#Analisa cada evento gerado pelo usuario enquanto o jogo roda.
    for event in pygame.event.get():
        #O tipo de Evento (QUIT) sairá do jogo, por isso run é false e While irá parar.
        if event.type == pygame.QUIT:
            #Após clicarmos no fechar, o pygame finaliza e passa para o próximo comando.
            run = False

    pygame.draw.rect(janela, (255,255,255), (10,10,10,20))
    #pygame.draw.rect(superficie, cor, (dimensoes) -> posicaox, posicaoy, largura, altura)
    pygame.draw.rect(janela, vermelho, (10,200, largura, altura))
    pygame.draw.rect(janela, azul, (250,200, largura, altura))
    pygame.draw.rect(janela, verde, (150,0, largura, altura))

    #Desenha um circulo> circle(superfice, cor, posicao, raio, contorno_espessura)
    pygame.draw.circle(janela, vermelho, (x,y), 130, 6)

    #Atualiza a informação na tela
    pygame.display.update()

#Finaliza o pygame
pygame.quit()
