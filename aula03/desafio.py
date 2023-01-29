import pygame, time

#Inicializa o pygame
pygame.init()

janela = pygame.display.set_mode((1000, 500))
#Define o título da janela para "Formas"
pygame.display.set_caption("Formas")

#define as cores usadas nas formas
preto = (0,0,0)
amarelo = (255,255,0)

#Define as dimensões das formas
largura = 50
altura = 50

x = 500
y = 250

run = True
#Run sempre é verdadeiro, logo o While sempre repetirá
while run:

#Analisa cada evento gerado pelo usuario enquanto o jogo roda.
    for event in pygame.event.get():
        #O tipo de Evento (QUIT) sairá do jogo, por isso run é false e While irá parar.
        if event.type == pygame.QUIT:
            #Após clicarmos no fechar, o pygame finaliza e passa para o próximo comando.
            run = False
    pygame.draw.circle(janela, amarelo, (x,y), 200, 0)
    pygame.draw.circle(janela, preto, (500,200), 20, 0)

    pygame.draw.polygon(janela, preto, ((500, 250), (750,100), (750,400)), 0)

    #Atualiza a informação na tela
    pygame.display.update()
    time.sleep(1)

    pygame.draw.circle(janela, amarelo, (x, y), 200, 0)
    pygame.draw.circle(janela, preto, (500, 200), 20, 0)

    pygame.draw.line(janela, preto, (500,250), (700,250), 6)

    pygame.display.update()
    time.sleep(1)
#Finaliza o pygame
pygame.quit()
