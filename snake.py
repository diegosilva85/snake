from turtle import Turtle

INITIAL_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # Indica as posições iniciais dos três primeiros segmentos
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        # A cobra começa com 3 segmentos
        for position in INITIAL_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_snake = Turtle("square")
        new_snake.up()
        new_snake.color("white")
        new_snake.goto(position)
        self.segments.append(new_snake)

    def reset_snake(self):
        # Ao dar game over, teleporta a cobra para uma posição fora da tela
        for seg in self.segments:
            seg.goto(1000, 1000)
        # Deleta todos os segmentos
        self.segments.clear()
        # Cria nova cobra na posição inicial
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        # O último segmento ocupa a posição do penúltimo segmento,
        # o penultimo ocupa a do antipenultimo e assim por diante.
        # Menos a çabeça (HEAD).
        for snake in range(len(self.segments) - 1, 0, -1):
            x_pos = self.segments[snake - 1].xcor()
            y_pos = self.segments[snake - 1].ycor()
            self.segments[snake].goto(x_pos, y_pos)
        # Move a cabeça pra frente
        self.head.forward(MOVE_DISTANCE)

# Funções de movimentação da cobra
    def up(self):
        # O if é para impedir que a cobra mude do head voltado para baixo ir direto para cima
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        # O if é para impedir que a cobra mude do head voltado para cima ir direto para baixo
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        # O if é para impedir que a cobra mude do head voltado para direita ir direto para esquerda
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        # O if é para impedir que a cobra mude do head voltado para esquerda ir direto para direita
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
