# Site para escolher uma cor aleatória
###https://www.rapidtables.com/web/color/RGB_Color.html

#Crie um programa que troque o texto e exiba a cor vermelha
# ou outra de sua preferência

import pygame, time

pygame.init()
janela = pygame.display.set_mode((600,600))
fonte = pygame.font.SysFont("Arial", 60)
texto = fonte.render("Aprendendo Python", 1, (193,71,71))

janela.blit(texto, (150,150))
pygame.display.update()
time.sleep(5)

fonte = pygame.font.SysFont("Arial", 40)
texto = fonte.render("Desafio 01", 1, (0,204,0))

janela.fill(pygame.Color("black"))

janela.blit(texto, (150,150))
pygame.display.update()
time.sleep(5)
pygame.quit()


