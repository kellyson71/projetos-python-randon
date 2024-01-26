import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Configurações da janela
WIDTH, HEIGHT = 800, 600
FPS = 60

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Configurações da raquete
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 100
PADDLE_SPEED = 8

# Configurações da bola
BALL_SIZE = 15
BALL_SPEED_X = 5
BALL_SPEED_Y = 5

# Criando a tela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

# Inicializando as posições
player1_y = HEIGHT // 2 - PADDLE_HEIGHT // 2
player2_y = HEIGHT // 2 - PADDLE_HEIGHT // 2
ball_x = WIDTH // 2 - BALL_SIZE // 2
ball_y = HEIGHT // 2 - BALL_SIZE // 2
ball_dx = BALL_SPEED_X
ball_dy = BALL_SPEED_Y

# Loop principal do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Movimentação das raquetes
    if keys[pygame.K_w] and player1_y > 0:
        player1_y -= PADDLE_SPEED
    if keys[pygame.K_s] and player1_y < HEIGHT - PADDLE_HEIGHT:
        player1_y += PADDLE_SPEED
    if keys[pygame.K_UP] and player2_y > 0:
        player2_y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and player2_y < HEIGHT - PADDLE_HEIGHT:
        player2_y += PADDLE_SPEED

    # Movimentação da bola
    ball_x += ball_dx
    ball_y += ball_dy

    # Verifica colisões com as paredes
    if ball_y <= 0 or ball_y >= HEIGHT - BALL_SIZE:
        ball_dy = -ball_dy

    # Verifica colisões com as raquetes
    if (
        (ball_x <= PADDLE_WIDTH and player1_y < ball_y < player1_y + PADDLE_HEIGHT)
        or (ball_x >= WIDTH - PADDLE_WIDTH - BALL_SIZE and player2_y < ball_y < player2_y + PADDLE_HEIGHT)
    ):
        ball_dx = -ball_dx

    # Verifica se a bola saiu do campo
    if ball_x < 0 or ball_x > WIDTH:
        ball_x = WIDTH // 2 - BALL_SIZE // 2
        ball_y = HEIGHT // 2 - BALL_SIZE // 2

    # Preenche a tela com a cor de fundo
    screen.fill(BLACK)

    # Desenha as raquetes e a bola
    pygame.draw.rect(screen, WHITE, (0, player1_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (WIDTH - PADDLE_WIDTH, player2_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.ellipse(screen, WHITE, (ball_x, ball_y, BALL_SIZE, BALL_SIZE))

    # Atualiza a tela
    pygame.display.flip()

    # Limita a taxa de quadros por segundo
    clock.tick(FPS)
