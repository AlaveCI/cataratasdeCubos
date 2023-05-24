import pygame
import random

pygame.init()
ancho, alto = 800, 600
pantalla = pygame.display.set_mode((ancho, alto))
reloj = pygame.time.Clock()

FONDO = (241, 238, 238)
CUBO = (96, 249, 14)

class Cubo:
    def __init__(self):
        self.ancho = 50
        self.alto = 50
        self.x = random.randint(0, ancho - self.ancho)
        self.y = -self.alto
        self.velocidad = random.randint(1, 5)

    def actualizar(self):
        self.y += self.velocidad

    def dibujar(self):
        pygame.draw.rect(pantalla, CUBO, (self.x, self.y, self.ancho, self.alto))

cubos = []
for _ in range(50):
    cubo = Cubo()
    cubos.append(cubo)

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    pantalla.fill(FONDO)

    for cubo in cubos:
        cubo.actualizar()
        cubo.dibujar()

    pygame.display.flip()
    reloj.tick(60)
pygame.quit()
