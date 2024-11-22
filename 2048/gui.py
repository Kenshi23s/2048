import pygame
import sys
import Logic2048 as resolucion

SCREENSIZE = 600

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
ZERO = (230, 230, 230)
ONE = (255, 186, 8)
TWO = (250, 163, 7)
THREE = (244, 140, 6)
FOUR = (232, 93, 4)
FIVE = (220, 47, 2)
SIX = (208, 0, 0)
SEVEN = (157, 2, 8)
EIGHT = (106, 4, 15)
NINE = (55, 6, 23)
TEN = (3, 7, 30)

COLORS = {
    0: ZERO,
    2 ** 1: ONE,
    2 ** 2: TWO,
    2 ** 3: THREE,
    2 ** 4: FOUR,
    2 ** 5: FIVE,
    2 ** 6: SIX,
    2 ** 7: SEVEN,
    2 ** 8: EIGHT,
    2 ** 9: NINE,
    2 ** 10: TEN
}

GAP = 10


def display_message(screen, message, color):
    screen.fill(WHITE)
    font = pygame.font.Font(None, 50)
    text = font.render(message, True, color)
    text_rect = text.get_rect(center=(SCREENSIZE // 2, SCREENSIZE // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()


def display_arr(screen, arr, tile_size):
    screen.fill(WHITE)
    n, _ = arr.shape
    tile_width = tile_size[0]
    for i in range(n):
        for j in range(n):
            x = GAP + tile_width / 2 + j * (tile_width + GAP)
            y = GAP + tile_width / 2 + i * (tile_width + GAP)
            num = int(arr[(i, j)])
            font = pygame.font.Font(None, int(tile_width / len(str(num)) ** 0.3))
            color = COLORS.get(num, BLACK)
            rect = pygame.Rect(0, 0, *tile_size)
            rect.center = (x, y)
            bg_surface = pygame.Surface(tile_size)
            bg_surface.fill(color)
            screen.blit(bg_surface, rect)
            if num != 0:
                text = font.render(str(num), True, BLACK if num < 128 else WHITE)
                offset = tile_width / 2
                text_rect = text.get_rect(center=(x, y + 0.05 * tile_width))
                screen.blit(text, text_rect)

    pygame.display.flip()


def main(n):
    # Initialize Pygame
    pygame.init()

    # Set up display
    screen = pygame.display.set_mode((SCREENSIZE, SCREENSIZE))

    tablero = resolucion.crear_tablero(n)
    tablero = resolucion.llenar_pos_vacias(tablero, 2)
    tile_width = (SCREENSIZE - (n + 1) * GAP) / n
    tile_size = (tile_width, tile_width)
    print("a \n", tablero)
    # Initial screen setup
    screen.fill(WHITE)
    pygame.display.flip()

    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    resolucion.mover(tablero, "derecha")
                elif event.key == pygame.K_LEFT:
                    resolucion.mover(tablero, "izquierda")
                elif event.key == pygame.K_UP:
                    print("inputArriba")
                    resolucion.mover(tablero, "arriba")
                elif event.key == pygame.K_DOWN:
                    resolucion.mover(tablero, "abajo")
                elif event.key == pygame.K_RETURN and resolucion.esta_atascado(tablero):
                    print("tablero atascado con",tablero)
                    tablero = resolucion.crear_tablero(n)
                    tablero = resolucion.llenar_pos_vacias(tablero, 2)

        if resolucion.esta_atascado(tablero):
            display_message(screen, "Presioná Enter para volver a jugar", RED)
        else:
            display_arr(screen, tablero, tile_size)


main(4)
