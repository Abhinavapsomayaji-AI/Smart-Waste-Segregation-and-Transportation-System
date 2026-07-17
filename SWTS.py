import pygame
import random

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Smart Waste Segregation & Transport System (SWTS)")


FONT = pygame.font.SysFont("Arial", 16)
TITLE_FONT = pygame.font.SysFont("Arial", 18, bold=True)

# Color Signatures for the 5 Waste Categories
YELLOW = (255, 235, 59)   # Solid Waste
BLUE = (33, 150, 243)     # Liquid Waste
GREEN = (76, 175, 80)     # Organic Waste
ORANGE = (255, 152, 0)    # Recyclable Waste
RED = (244, 67, 54)       # Hazardous Waste
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (180, 180, 180)
DARK_GRAY = (80, 80, 80)

# Global Bin Counters
bin_counts = {
    'solid': 0,
    'liquid': 0,
    'organic': 0,
    'recyclable': 0,
    'hazardous': 0
}

class Visitor:
    def __init__(self):
        self.direction = random.choice(["L2R", "R2L"])
        
        if self.direction == "L2R":
            self.x = -30
            self.speed = random.uniform(1.5, 2.5)
        else:
            self.x = WIDTH + 30
            self.speed = random.uniform(-2.5, -1.5)
            
        self.y = 188  
        self.radius = 12
        self.has_trash = True
        
        self.is_stopping = False
        self.stop_timer = 0
        self.stop_duration = random.randint(40, 70)

    def update(self, drop_zone_x):
        distance_to_bin = abs(self.x - drop_zone_x)
        
        if distance_to_bin < 10 and self.has_trash and not self.is_stopping:
            self.is_stopping = True

        if self.is_stopping:
            self.stop_timer += 1
            if self.stop_timer >= self.stop_duration:
                self.is_stopping = False
                self.has_trash = False
                return True 
        else:
            self.x += self.speed
            
        return False

    def draw(self, surface):
        pygame.draw.circle(surface, (103, 58, 183), (int(self.x), int(self.y)), self.radius)
        offset = -8 if self.speed > 0 else 8
        pygame.draw.circle(surface, (156, 39, 176), (int(self.x + offset), int(self.y)), 6)


class GarbageItem:
    def __init__(self, start_x):
        self.x = start_x
        self.y = 205 
        self.radius = 10
        self.state = "FALLING_TO_SCANNER"
        self.speed = 3
        self.scan_timer = 0
        
        categories = ['solid', 'liquid', 'organic', 'recyclable', 'hazardous']
        weights = [0.30, 0.25, 0.25, 0.1999999999999, 0.0000000000001]
        
        self.type = random.choices(categories, weights=weights, k=1)[0]
        self.color = self.get_color()
        self.target_x = self.get_target_x()

    def get_color(self):
        if self.type == 'solid': return YELLOW
        if self.type == 'liquid': return BLUE
        if self.type == 'organic': return GREEN
        if self.type == 'recyclable': return ORANGE
        if self.type == 'hazardous': return RED

    def get_target_x(self):
        if self.type == 'solid': return 100
        if self.type == 'liquid': return 250
        if self.type == 'organic': return 400
        if self.type == 'recyclable': return 550
        if self.type == 'hazardous': return 700

    def update(self):
        if self.state == "FALLING_TO_SCANNER":
            if self.y < 230:
                self.y += self.speed
            else:
                self.state = "SCANNING"
                
        elif self.state == "SCANNING":
            self.scan_timer += 1
            if self.scan_timer >= 45: 
                self.state = "SORTING"
                
        elif self.state == "SORTING":
            self.y += self.speed
            if self.x < self.target_x:
                self.x += min(4, self.target_x - self.x)
            elif self.x > self.target_x:
                self.x -= min(4, self.x - self.target_x)

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)



clock = pygame.time.Clock()
garbage_items = []
visitors = []
visitor_spawn_timer = 0
intake_x = WIDTH // 2

lid_open_pct = 0.0 

running = True
while running:
    screen.fill(WHITE)
    
    someone_nearby = False
    for person in visitors:
        if abs(person.x - intake_x) < 75:
            someone_nearby = True
            break
            
    if someone_nearby:
        lid_open_pct += min(0.1, 1.0 - lid_open_pct) 
    else:
        lid_open_pct -= min(0.05, lid_open_pct)       

    
    pygame.draw.line(screen, BLACK, (0, 200), (WIDTH, 200), 4)
    pygame.draw.rect(screen, GRAY, (intake_x - 30, 200, 60, 35))
    pygame.draw.rect(screen, DARK_GRAY, (intake_x - 30, 200, 60, 35), 2)
    
    lid_shift = int(25 * lid_open_pct)
    pygame.draw.rect(screen, BLACK, (intake_x - 28 - lid_shift, 196, 28, 6))
    pygame.draw.rect(screen, BLACK, (intake_x + lid_shift, 196, 28, 6))
    
  
    bin_types = [('solid', YELLOW, 100), ('liquid', BLUE, 250), 
                 ('organic', GREEN, 400), ('recyclable', ORANGE, 550), 
                 ('hazardous', RED, 700)]
                 
    for key, color, x_pos in bin_types:
        pygame.draw.rect(screen, color, (x_pos - 40, 480, 80, 80), 3)
        pygame.draw.rect(screen, (245, 245, 245), (x_pos - 37, 483, 74, 74))
        
        count_text = FONT.render(f"Qty: {bin_counts[key]}", True, BLACK)
        name_text = TITLE_FONT.render(key.capitalize(), True, color)
        screen.blit(name_text, (x_pos - 30, 430))
        screen.blit(count_text, (x_pos - 20, 455))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False


    visitor_spawn_timer += 1
   
    if visitor_spawn_timer >= random.randint(200, 350):
        visitors.append(Visitor())
        visitor_spawn_timer = 0

    for person in visitors[:]:
        should_drop = person.update(intake_x)
        person.draw(screen)
        
        if abs(person.x - intake_x) < 75:
            pygame.draw.circle(screen, (76, 175, 80), (intake_x, 185), 5)
            
        if should_drop:
            garbage_items.append(GarbageItem(intake_x))
            
        if person.x > WIDTH + 40 or person.x < -40:
            visitors.remove(person)

 
    for item in garbage_items[:]:
        item.update()
        item.draw(screen)
        
        if item.state == "SCANNING":
            pygame.draw.line(screen, (255, 0, 0), (intake_x - 26, 230), (intake_x + 26, 230), 3)
            
        if item.y >= 490 and (480 <= item.y <= 500):
            if abs(item.x - item.target_x) < 15:
                bin_counts[item.type] += 1
                garbage_items.remove(item)
        elif item.y > HEIGHT + 20:
            garbage_items.remove(item)

    pygame.display.flip()
    clock.tick(60)

pygame.display.quit()
pygame.quit()
print("Simulation closed cleanly.")
