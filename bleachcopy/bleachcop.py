# bleach_pixel_demo.py
# 2D pixel-art prototype: Soul Society background + Ichigo-like pixel sprite
# Place assets in ./assets/
# - assets/ss_background.png    (background image or tiled panorama)
# - assets/samurai_sprites.png  (spritesheet: frames arranged in rows)
#
# Note: This is a small, robust loader/animation example. Replace files with the
# exact sprites you downloaded from Kenney / OpenGameArt (both CC0/public domain).

import pygame, sys, os
from pathlib import Path

# ---------- Config ----------
WIDTH, HEIGHT = 960, 540
FPS = 60

ASSETS_DIR = Path("assets")
BG_FILE = ASSETS_DIR / "ss_background.png"
SPRITE_FILE = ASSETS_DIR / "ichigo_sprites.png"

# Character sprite parameters (adjust to match the spritesheet you downloaded)
FRAME_W = 48     # width of a single frame
FRAME_H = 48     # height of a single frame
SCALE = 2        # integer scale for pixel-art
ANIM_SPEED = 120 # ms per frame

PLAYER_SPEED = 3

# Colors
BLACK = (0,0,0)
WHITE = (255,255,255)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bleach — Pixel Prototype")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 20)

# ---------- Utility: load image safely ----------
def load_image(path, colorkey=None):
    if not path.exists():
        raise FileNotFoundError(f"Missing asset: {path}")
    img = pygame.image.load(str(path)).convert_alpha()
    if colorkey is not None:
        img.set_colorkey(colorkey)
    return img

# ---------- Sprite sheet helper ----------
class SpriteSheet:
    def __init__(self, image, frame_w, frame_h):
        self.sheet = image
        self.frame_w = frame_w
        self.frame_h = frame_h
        self.cols = image.get_width() // frame_w
        self.rows = image.get_height() // frame_h

    def frame(self, col, row):
        rect = pygame.Rect(col*self.frame_w, row*self.frame_h, self.frame_w, self.frame_h)
        surf = pygame.Surface(rect.size, pygame.SRCALPHA)
        surf.blit(self.sheet, (0,0), rect)
        return surf

# ---------- Player (animated) ----------
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, spritesheet):
        super().__init__()
        self.spritesheet = spritesheet
        # We'll assume layout: row0 = idle frames (cols 0..n), row1 = walk frames, row2 = attack frames
        self.idle_frames = [self.spritesheet.frame(i,0) for i in range(self.spritesheet.cols)]
        self.walk_frames = [self.spritesheet.frame(i,1) for i in range(self.spritesheet.cols)]
        # if attack row missing, reuse first frame
        self.attack_frames = [self.spritesheet.frame(i,2) for i in range(self.spritesheet.cols)] \
                             if self.spritesheet.rows > 2 else [self.idle_frames[0]]

        # scale frames
        def scale_list(frames):
            return [pygame.transform.scale(f, (f.get_width()*SCALE, f.get_height()*SCALE)) for f in frames]
        self.idle_frames = scale_list(self.idle_frames)
        self.walk_frames = scale_list(self.walk_frames)
        self.attack_frames = scale_list(self.attack_frames)

        self.image = self.idle_frames[0]
        self.rect = self.image.get_rect(midbottom=(x,y))
        self.vx = 0
        self.facing = 1
        self.state = "idle"   # 'idle', 'walk', 'attack'
        self.anim_index = 0
        self.last_anim_time = pygame.time.get_ticks()

    def update(self, dt, keys):
        # Movement
        self.vx = 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.vx = -PLAYER_SPEED; self.facing = -1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.vx = PLAYER_SPEED; self.facing = 1

        self.rect.x += int(self.vx)

        # Determine state
        if keys[pygame.K_SPACE]:
            if self.state != "attack":
                self.state = "attack"
                self.anim_index = 0
                self.last_anim_time = pygame.time.get_ticks()
        elif self.vx != 0:
            if self.state != "walk":
                self.state = "walk"
                self.anim_index = 0
                self.last_anim_time = pygame.time.get_ticks()
        else:
            if self.state != "idle":
                self.state = "idle"
                self.anim_index = 0
                self.last_anim_time = pygame.time.get_ticks()

        # Animation tick
        now = pygame.time.get_ticks()
        if now - self.last_anim_time > ANIM_SPEED:
            self.last_anim_time = now
            self.anim_index += 1

            if self.state == "idle":
                frames = self.idle_frames
                self.anim_index %= max(1, len(frames))
                self.image = frames[self.anim_index]
            elif self.state == "walk":
                frames = self.walk_frames
                if len(frames) == 0: frames = self.idle_frames
                self.anim_index %= max(1, len(frames))
                self.image = frames[self.anim_index]
            elif self.state == "attack":
                frames = self.attack_frames
                # play attack animation once then return to idle
                if self.anim_index >= len(frames):
                    self.state = "idle"
                    self.anim_index = 0
                    self.image = self.idle_frames[0]
                else:
                    self.image = frames[self.anim_index]

        # flip to face direction
        if self.facing < 0:
            self.image = pygame.transform.flip(self.image, True, False)

# ---------- Main setup ----------
def main():
    # load assets
    try:
        bg = load_image(BG_FILE)
    except FileNotFoundError as e:
        print(e); sys.exit(1)
    try:
        sprite_img = load_image(SPRITE_FILE)
    except FileNotFoundError as e:
        print(e); sys.exit(1)

    spritesheet = SpriteSheet(sprite_img, FRAME_W, FRAME_H)
    player = Player(WIDTH//4, HEIGHT - 40, spritesheet)
    group = pygame.sprite.Group(player)

    # If background is smaller/larger, we'll tile or center it
    bg_w, bg_h = bg.get_size()

    running = True
    while running:
        dt = clock.tick(FPS)
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                running = False
            elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
                running = False

        keys = pygame.key.get_pressed()
        group.update(dt, keys)

        # Draw background: center or tile horizontally
        screen.fill((10,10,20))
        # center bg
        bg_x = (WIDTH - bg_w)//2
        bg_y = HEIGHT - bg_h
        screen.blit(bg, (bg_x, bg_y))

        # ground line (simple)
        pygame.draw.rect(screen, (40,40,40), (0, HEIGHT-32, WIDTH, 32))

        # draw player
        group.draw(screen)

        # HUD
        txt = font.render("Controls: A/D or ←/→ Move | Space Attack", True, (220,220,220))
        screen.blit(txt, (10,10))

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
