# Aula05 - Textos
# importar pygame

import pygame, random


# A função Blit desenha texto na tela
    # blit()

pygame.init()

janela_altura = 480
janela_largura = 640

janela = pygame.display.set_mode((janela_largura, janela_altura))
pygame.display.set_caption('Formas - Aula 05')
clock = pygame.time.Clock()
FPS = 60

# Texto
fonteGrande = pygame.font.SysFont('Arial',20,True,True)
fontePequena = pygame.font.SysFont('Verdana',12)

# Cores Texto
branco = (255,255,255)
titulo = fonteGrande.render("Movimento Aleatório!",1,branco)
titulo_rect = titulo.get_rect(center=(janela_largura/2, 40))

# azul = (0,0,255)
# vermelho = (255,0,0)
# verde = (0,255,0)
# amarelo = (255,255,0)

#Define as posicoes
x=500
y=250

# Altera a todo frame a velocidade
velocidadeX = random.uniform(-1.5, 1.5)
velocidadeY = random.uniform(-1.5, 1.5)
x += velocidadeX
y += velocidadeY


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
    texto_x = fontePequena.render("Vel-X: "+ str(velocidadeX),1,branco)
    texto_y = fontePequena.render("Vel-Y: "+ str(velocidadeY),1,branco)
    x += velocidadeX
    y += velocidadeY

    # Limpa a tela
    janela.fill(((0,0,0)))
    janela.blit(titulo, (titulo_rect))
    janela.blit(texto_x, (15,410))
    janela.blit(texto_y, (15,425))
    pygame.draw.rect(janela, (r, g, b), (x,y,100,100))

    #Atualiza a informação na tela
    pygame.display.update()

pygame.QUIT()