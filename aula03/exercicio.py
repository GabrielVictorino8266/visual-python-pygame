import pygame

#Inicializa o pygame
pygame.init()

janela = pygame.display.set_mode((1000, 500))
#Define o título da janela para "Formas"
pygame.display.set_caption("Formas")

#define as cores usadas nas formas
azul = (0,0,255)
vermelho = (255,0,0)
verde = (0,255,0)
amarelo = (255,255,0)

#Define as dimensões das formas
largura = 100
altura = 100

largura2 = 200
altura2 = 200

largura3 = 100
altura3 = 100

#Define as posicoes
x1=500
y1=250

run = True
#Run sempre é verdadeiro, logo o While sempre repetirá
while run:

#Analisa cada evento gerado pelo usuario enquanto o jogo roda.
    for event in pygame.event.get():
        #O tipo de Evento (QUIT) sairá do jogo, por isso run é false e While irá parar.
        if event.type == pygame.QUIT:
            #Após clicarmos no fechar, o pygame finaliza e passa para o próximo comando.
            run = False
    #pygame.draw.rect(superficie, cor, (dimensoes) -> posicaox, posicaoy, largura, altura)
    pygame.draw.rect(janela, vermelho, (450, 200, largura, altura))
    pygame.draw.rect(janela, azul, (0, 0, largura, altura))
    pygame.draw.rect(janela, verde, (900, 400, largura3, altura3))

    #Desenha um circulo> circle(superfice, cor, posicao, raio, contorno_espessura)
    pygame.draw.circle(janela, amarelo, (x1,y1), 130, 6)

    #Atualiza a informação na tela
    pygame.display.update()

#Finaliza o pygame
pygame.quit()
