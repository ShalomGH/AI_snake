import pygame


def event_loop(change_to):
    """Функция для отслеживания нажатий клавиш игроком"""
    # запускаем цикл по ивентам
    for event in pygame.event.get():
        # если нажали клавишу
        if event.type == pygame.KEYDOWN:
            __pushed__ = True
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_to = "RIGHT"
            elif event.key == pygame.K_LEFT or event.key == ord('a'):
                change_to = "LEFT"
            elif event.key == pygame.K_UP or event.key == ord('w'):
                change_to = "UP"
            elif event.key == pygame.K_DOWN or event.key == ord('s'):
                change_to = "DOWN"
            # нажали escape
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    return change_to


def init_and_check_for_errors():
    """Начальная функция для инициализации и
       проверки как запустится pygame"""
    check_errors = pygame.init()
    if check_errors[1] > 0:
        sys.exit()
