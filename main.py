import time
from turtle import Screen

from player import Player
from score import Score
from traffic import Traffic
from display import Display

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
game_is_on = True

player = Player()
score = Score()
traffic = Traffic()
display = Display()

is_game_paused = False


def pause_game():
    global is_game_paused
    is_game_paused = not is_game_paused


screen.listen()
screen.onkey(key="Up", fun=player.up)
screen.onkey(key="Down", fun=player.down)
screen.onkey(key="Left", fun=player.left_turn)
screen.onkey(key="Right", fun=player.right_turn)
screen.onkey(key="space", fun=pause_game)


while game_is_on:

    if not is_game_paused:
        display.display_status(is_game_paused)
        time.sleep(0.1)
        screen.update()

        traffic.create_car()
        traffic.move_cars()

        # Detect Collision with Car
        for car in traffic.traffic_list:
            if car.distance(player) < 20:
                game_is_on = False
                score.show_game_over()

        # Detect Level Completion
        if player.ycor() > 250:
            score.increase_score()
            if score.level > score.highest_level:
                score.update_score()
            player.return_to_start()
            traffic.level_up()
    else:
        display.display_status(is_game_paused)

screen.exitonclick()
