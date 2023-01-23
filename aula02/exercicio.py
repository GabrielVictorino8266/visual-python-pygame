
import pygame, time

pygame.init()

janela = pygame.display.set_mode((600,300))
fonte = pygame.font.SysFont("Times New Roman", 40)
texto = fonte.render("Exerício 01:", 1, (255,255,255))

janela.blit(texto, (150,50))
pygame.display.update()
time.sleep(5)

fonte = pygame.font.SysFont("Times New Roman", 20)
novoTexto = fonte.render("Aprendendo Python", 1, (255,255,255))

janela.blit(novoTexto, (150, 150))
pygame.display.update()
time.sleep(5)
pygame.quit()