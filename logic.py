class Destroyer_logic(object):

    def __init__(self, destroyer, enemies, bullets, fades, window_size):
        self.__destroyer = destroyer
        self.__bullets = bullets
        self.__enemies = enemies
        self.__fades = fades
        self.__window_size = window_size

    def __check_bullets(self):
        bullet_remove_list = []
        bullet_list = self.__bullets.get_bullets()

        for i in range(len(bullet_list)):
            if not (self.__window_size[0] >= bullet_list[i].get_position()[0] >= 0) or not (self.__window_size[1] >= bullet_list[i].get_position()[1] >= 0):
                bullet_remove_list.append(i)
        return bullet_remove_list

    def __check_bullets_enemies(self):
        enemy_remove_list = []
        bullet_remove_list = []
        enemy_list = self.__enemies.get_enemies()
        bullet_list = self.__bullets.get_bullets()

        for b in range(len(bullet_list)):
            for e in range(len(enemy_list)):
                if bullet_list[b].get_image()[1].colliderect(enemy_list[e].get_image()[1]):
                    bullet_remove_list.append(b)
                    enemy_remove_list.append(e)
                    self.__fades.add_fade(enemy_list[e].get_image()[0], enemy_list[e].get_image()[1], 0.5)
        return bullet_remove_list, enemy_remove_list

    def __check_enemies(self):
        enemies_remove_list = []
        enemies = self.__enemies.get_enemies()
        for i in range(len(self.__enemies.get_enemies())):
            rect = enemies[i].get_rect()
            if enemies[i].get_direction() == 3:
                if rect[2] <= 0:
                    enemies_remove_list.append(i)
            if enemies[i].get_direction() == 1:
                if rect[2] >= self.__window_size[0] + (rect[2]-rect[0]):
                    enemies_remove_list.append(i)
        return enemies_remove_list

    def check(self):

        bullet_remove_list_1 = self.__check_bullets()
        bullet_remove_list_2, enemy_remove_list_1 = self.__check_bullets_enemies()
        enemy_remove_list_2 = self.__check_enemies()

        bullet_remove_list = list(set(bullet_remove_list_1 + bullet_remove_list_2))
        enemy_remove_list = list(set(enemy_remove_list_1 + enemy_remove_list_2))

        self.__bullets.remove_bullets(bullet_remove_list)
        self.__enemies.remove_enemies(enemy_remove_list)

        if len(self.__enemies.get_enemies()) == 0:
            self.__enemies.add_enemy()
