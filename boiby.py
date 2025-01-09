import pygame
import os
import psutil
import platform
import random

pygame.init()

version = "2.0"
img_folder = "img"
sound_folder = "sounds"

window_icon = pygame.image.load(os.path.join(img_folder, "boiby2.png"))
pygame.display.set_icon(window_icon)
window_size = (350, 350)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("boiby")

boiby = pygame.image.load(os.path.join(img_folder, "boiby.png"))
boiby = pygame.transform.scale(boiby, window_size)

boiby2 = pygame.image.load(os.path.join(img_folder, "boiby2.png"))
boiby2 = pygame.transform.scale(boiby2, window_size)

mp3_files = [file for file in os.listdir(sound_folder) if file.endswith(".mp3")]
if not mp3_files:
    print("No MP3 files found in the sounds folder.")
else:
    print(f"Found {len(mp3_files)} MP3 files.")

cpu_threads = psutil.cpu_count()
memory_info = psutil.virtual_memory().total / (1024 * 1024)
os_build = platform.version()
cpu_name = platform.processor()

print(f"CPU: {cpu_name}")
print(f"Threads: {cpu_threads}")
print(f"Memory: {memory_info:.2f} MB")
print(f"OS Build: {os_build}")

log_events = [
    "Welcome to the boiby app",

    f"App Version: {version}",
    "-" * 40,
    f"CPU: {cpu_name}",
    f"Threads: {cpu_threads}",
    f"Memory: {memory_info:.2f} MB",
    f"OS Build: {os_build}",
    "-" * 40,
]

clock = pygame.time.Clock()
current_image = boiby
is_boiby2 = False
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    window.fill((255, 255, 255))
    window.blit(current_image, (0, 0))
    pygame.display.flip()
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            log_events.append("Application quit.")
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                current_image = boiby if is_boiby2 else boiby2
                log_events.append(f"K_e pressed.")
                log_message = "Image changed to boiby.png." if is_boiby2 else "Image changed to boiby2.png."
                log_events.append(log_message)
                print(log_message)
                is_boiby2 = not is_boiby2
            elif event.key == pygame.K_SPACE and mp3_files:
                sound_file = os.path.join(sound_folder, random.choice(mp3_files))
                log_events.append(f"K_SPACE pressed.")
                pygame.mixer.music.load(sound_file)
                pygame.mixer.music.play()
                log_events.append(f"Boiby meowed (playing sound: {sound_file}).")
                print(f"Playing sound: {sound_file}")
            elif event.key == pygame.K_q:
                log_events.append(f"K_q pressed.")
                with open("log.txt", "w") as log_file:
                    log_file.write("\n".join(log_events))
                print("Logged all events.")
                log_events.append("Logged all events.")
                
    window.fill((255, 255, 255))
    window.blit(current_image, (0, 0))
    pygame.display.flip()

pygame.quit()
