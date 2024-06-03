from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.properties import StringProperty

class TicTacToeApp(App):
    current_player = StringProperty("X")
    winning_combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                            (0, 3, 6), (1, 4, 7), (2, 5, 8),
                            (0, 4, 8), (2, 4, 6))
    click_count = 0
    game_over = False

    def build(self):
        self.root = Builder.load_file("tictactoe.kv")
        return self.root

    def on_button_press(self, button):
        if button.text == "" and not self.game_over:
            button.text = self.current_player
            self.click_count += 1
            if self.check_winner():
                self.display_winner()
                self.game_over = True
                return
            elif self.click_count == 9:
                self.root.ids.winner_label.text = "It's a Tie!"
                self.game_over = True
                return
            self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        for combination in self.winning_combinations:
            button1, button2, button3 = self.root.ids.game_board.children[-(combination[0] + 1)], \
                                         self.root.ids.game_board.children[-(combination[1] + 1)], \
                                         self.root.ids.game_board.children[-(combination[2] + 1)]
            if button1.text == button2.text == button3.text != "":
                return True
        return False

    def display_winner(self):
        self.root.ids.winner_label.text = f"{self.current_player} Wins!"

    def reset_game(self):
        for button in self.root.ids.game_board.children:
            button.text = ""
        self.click_count = 0
        self.current_player = "X"
        self.root.ids.winner_label.text = ""
        self.game_over = False

if __name__ == "__main__":
    TicTacToeApp().run()
