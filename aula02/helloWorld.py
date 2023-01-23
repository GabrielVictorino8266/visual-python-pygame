#importa os módulos pygame e time (usado para aguardar ao executar uma ação)
import pygame, time

#inicia o pygame module
pygame.init()
#define o tamanho da janela a ser criada
janela = pygame.display.set_mode((600, 300))
#define a fonte a ser usada e seu tamanho -> SysFont("Fonte", tamanho)
fonte = pygame.font.SysFont("Inter", 60)
#define o texto, que receberá a fonte definida anteriormente e aplica algumas propriedades.
#Entre as propriedades, temos 1 ou 0 (define se o texto será serrilhado) e a cor
texto = fonte.render("Olá, Mundo!", 1, (255, 255, 255))

janela.blit(texto, (125, 100))
pygame.display.update()
time.sleep(5)
pygame.quit()

####Entendendo alguns comandos####
#Blit (sobreposição) a superfície na tela na posição correta
#Agora a parte mais importante. Precisamos pegar essa superfície (fundo) e
# desenhá-la na janela. Para fazer isso, vamos chamar screen.blit(background,(x,y))where (x,y) é
# a posição dentro da janela onde queremos que o canto superior esquerdo da
# superfície esteja. Esta função diz para pegar a superfície de fundo e desenhá-la
# na tela e posicioná-la em (x,y).
