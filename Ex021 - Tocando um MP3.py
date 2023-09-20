# Ex021 - Faça um programa em Python que abra e reprosuza o áudio de um arquivo MP3
# Autor - Samuel Santos

import pygame

pygame.init()
pygame.mixer_music.load('ex.mp3')
pygame.mixer_music.play()
pygame.mixer_music.wait()