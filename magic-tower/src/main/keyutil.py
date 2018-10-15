#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pygame


def is_up(event_key):
    return event_key == pygame.K_w or event_key == pygame.K_UP


def is_down(event_key):
    return event_key == pygame.K_s or event_key == pygame.K_DOWN


def is_left(event_key):
    return event_key == pygame.K_a or event_key == pygame.K_LEFT


def is_right(event_key):
    return event_key == pygame.K_d or event_key == pygame.K_RIGHT

