# NUMEROS RANDOMICOS NO PYTHON COM PYGAME

import pygame, random

#Inicializa o pygame
pygame.init()

janela = pygame.display.set_mode((640, 480))
#Define o título da janela para "Formas"
pygame.display.set_caption("PROJETO BASE")
clock = pygame.time.Clock()
FPS = 120

# Gera numeros reais
velocidadeX = random.uniform(-1.5,1.5)
velocidadeY = random.uniform(-1.5,1.5)
x = 270
y = 190

run = True
#Run sempre é verdadeiro, logo o While sempre repetirá
while run:
    # Informamos a quantidade de quadro por segundo
    clock.tick(FPS)
#Analisa cada evento gerado pelo usuario enquanto o jogo roda.
    for event in pygame.event.get():
        #O tipo de Evento (QUIT) sairá do jogo, por isso run é false e While irá parar.
        if event.type == pygame.QUIT:
            #Após clicarmos no fechar, o pygame finaliza e passa para o próximo comando.
            run = False

    # Cores aleatorias (numeros inteiros)
    r = random.randrange(0,255)
    g = random.randrange(0, 255)
    b = random.randrange(0, 255)
    # Altera a todo frame a velocidade
    velocidadeX = random.uniform(-1.5, 1.5)
    velocidadeY = random.uniform(-1.5, 1.5)
    x += velocidadeX
    y += velocidadeY

    # Limpa a tela
    janela.fill((0,0,0))
    pygame.draw.rect(janela, (r,g,b), (x,y,100,100))

    #Atualiza a informação na tela
    pygame.display.update()

#Finaliza o pygame
pygame.quit()
