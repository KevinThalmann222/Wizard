class Wizard:
    def __init__(self):
        self.rounds = None
        self.player_name = None
        self.valid_player = None
        self.players_num = None

        self.current_round = 1
        self.current_player = -1
        self.victorys_num = 0

        self.player_points = {}
        self.player_wins = []
        self.current_victorys = []

    def check(self, *args):
        player_names = [
            Element("name1").element.value,
            Element("name2").element.value,
            Element("name3").element.value,
            Element("name4").element.value,
            Element("name5").element.value,
            Element("name6").element.value,
        ]
        self.valid_player = [player for player in player_names if player]
        self.players_num = len(self.valid_player)
        if self.players_num >= 3:
            Element("text_input_player").element.innerText = f"Es spielen {self.players_num} Leute mit: {', '.join(self.valid_player)}"
            if self.players_num == 3:
                self.rounds = 20
            elif self.players_num == 4:
                self.rounds = 15
            elif self.players_num == 5:
                self.rounds = 12
            elif self.players_num == 6:
                self.rounds = 10
            Element("player_num").element.innerText = f"Es werden {self.rounds} gespielt, viel Spaß."
            Element("round").element.innerText = self.rounds
            Element("player").element.innerText = self.players_num
            Element("aktuell").element.innerText = self.current_round

        else:
            Element("text_input_player").element.innerText = "Es müssen mindestens 3 Spieler mitspielen"

    def play(self, *args):

        if not all([self.rounds, self.players_num, self.valid_player]):
            return

        if self.current_player + 2 == self.players_num:
            self.current_player += 1
            dif = self.current_round - self.victorys_num
            if self.current_round > self.victorys_num:
                Element("wins_text").element.innerText = f"Achtung {self.valid_player[self.current_player]}! Du darfst NICHT {dif} auswählen, bitte schätze: "
            else:
                Element("wins_text").element.innerText = f"{self.valid_player[self.current_player]} bitte schätze deine Siege: "
        else:
            self.current_player += 1
            Element("wins_text").element.innerText = f"{self.valid_player[self.current_player]} bitte schätze deine Siege: "

    def select_wins(self, *args):
        if not all([self.rounds, self.players_num, self.valid_player]):
            return
        if len(self.current_victorys) == self.players_num:
            return

        victory = int(Element("wins_num").element.value)
        self.victorys_num += victory

        self.current_victorys.append(f"{self.valid_player[self.current_player]} geschätzte Siege: {victory}")

        Element("wins_text_goal").element.innerText = ", ".join(self.current_victorys)
        Element("wins_num").element.value = 0
        self.player_wins.append({"Gamer": self.current_player, "Points": victory})
        if self.current_victorys:
            Element("startrunde").element.innerText = "Nächster Spieler"

    def del_wins(self, *args):
        if not all([self.rounds, self.players_num, self.valid_player]):
            return
        Element("wins_text_goal").element.innerText = ""
        self.current_victorys = []
        self.current_round = 0
        self.current_player = -1
        self.victorys_num = 0

    def next_round(self, *args):
        if not all([self.rounds, self.players_num, self.valid_player]):
            return
        self.current_round += 1
        self.current_victorys = []
        Element("aktuell").element.innerText = self.current_round
        Element("wins_text_goal").element.innerText = ""

        self.valid_player.append(self.valid_player.pop(self.valid_player.index(self.valid_player[0])))
        self.current_player = 0
        Element("wins_text").element.innerText = f"{self.valid_player[self.current_player]} bitte schätze deine Siege: "


if __name__ == "__main__":
    wizard = Wizard()
    wizard.check()
    wizard.play()
    wizard.select_wins()
    wizard.del_wins()
    wizard.next_round()
