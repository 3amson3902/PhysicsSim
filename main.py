import pygame
import math

# Constants
WIDTH, HEIGHT = 800, 600
DIPOLE_MOMENT = 50.0
FIELD_STRENGTH = 10.0
INERTIA = 200.0
TIME_STEP = 0.01
DIPOLE_LENGTH = 80
DAMPING = 0.995  # To simulate energy loss

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dipole Torque Simulator")
clock = pygame.time.Clock()

# Initial state
angle = math.pi / 2  # 90 degrees in radians
angular_velocity = 0.0

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Physics calculations
    torque = -DIPOLE_MOMENT * FIELD_STRENGTH * math.sin(angle)
    angular_acceleration = torque / INERTIA
    
    # Update angular velocity and angle (with damping)
    angular_velocity += angular_acceleration * TIME_STEP
    angular_velocity *= DAMPING  # Simulate friction/air resistance
    angle += angular_velocity * TIME_STEP
    
    # Wrap angle between 0 and 2π
    angle %= 2 * math.pi

    # Clear screen
    screen.fill((255, 255, 255))

    # Draw electric field (horizontal line)
    pygame.draw.line(screen, (255, 0, 0), (100, HEIGHT//2), (WIDTH-100, HEIGHT//2), 2)

    # Calculate charge positions
    center_x, center_y = WIDTH//2, HEIGHT//2
    pos_x = center_x + DIPOLE_LENGTH * math.cos(angle)
    pos_y = center_y - DIPOLE_LENGTH * math.sin(angle)  # Pygame Y increases downward
    neg_x = center_x - DIPOLE_LENGTH * math.cos(angle)
    neg_y = center_y + DIPOLE_LENGTH * math.sin(angle)

    # Draw dipole line
    pygame.draw.line(screen, (0, 0, 0), (neg_x, neg_y), (pos_x, pos_y), 3)

    # Draw charges
    pygame.draw.circle(screen, (0, 0, 255), (int(pos_x), int(pos_y)), 15)
    pygame.draw.circle(screen, (255, 0, 0), (int(neg_x), int(neg_y)), 15)

    # Update display
    pygame.display.flip()
    clock.tick(60)  # 60 FPS

pygame.quit()