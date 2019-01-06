import pygame


class Animation:
    def rotate(self, image, rect, angle):
        new_image = pygame.transform.rotate(image, angle)
        rect = new_image.get_rect(
            center = rect.center
        )
        return new_image, rect