from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.up()
        self.color("white")
        self.goto(0, 270)
        self.score = 0
        with open("data.txt", "r") as file:
            self.highscore = int(file.read())
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"SCORE: {self.score} HIGH SCORE: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset_game(self):
        # Ao término do jogo, atualiza a pontuação se necessário e chama a função para reiniciar o placar.
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", "w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def new_score(self):
        self.score += 1
        self.update_score()
