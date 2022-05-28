class Wizard:
    def __init__(self):
        self.players_num = None
        self.player_name = None
        self.player_points = {}

    def player_number(self):
        print("Als Erstes wird die Anzahl der Spieler bestimmt.")
        print("=> min = 3, max = 6 <=")
        while True:
            try:
                self.players_num = int(input("Bitte wähle die Anzahl der Spieler: "))
            except Exception:
                print("Die Eingabe ist nicht korrekt, bitte wähle eine Zahl zwischen 3 und 6")
            else:
                if self.players_num < 3 or self.players_num > 6:
                    print("Anzahl der Spieler muss zwischen 3 und 6 sein!")
                    continue
                else:
                    print(f"Anzahl der Spieler = {self.players_num }")
                    break
        return self.players_num

    def players_name(self):
        print("\nNun werden die Namen der Spieler bestimmt.")
        print("Starte mit dem Spieler welcher beginnen soll und gehe dann im Uhrzeigersinn weiter!")
        if not self.players_num:
            self.players_num = self.player_number()
        self.player_name = [input(f"Name von Spieler {num+1}: ") for num in range(self.players_num)]
        return self.player_name

    def round_number(self):
        if not self.players_num:
            self.players_num = self.player_number()
        if not self.player_name:
            self.player_name = self.players_name()
        if self.players_num == 3:
            rounds = 20
        elif self.players_num == 4:
            rounds = 15
        elif self.players_num == 5:
            rounds = 12
        else:
            rounds = 10
        print(f"\nHallo {', '.join(self.player_name)} es werden {rounds} gespielt. Viel Spaß\n")

        return rounds

    def run(self):
        print(f"=============================================== Wizard by Kevin Thalmann ===============================================\n")
        num_rounds = self.round_number()
        player_wins = []
        for idx_round in range(num_rounds):
            wins = 0
            runde = idx_round + 1
            print(f"################################################## Runde {runde} ##################################################")
            for idx_player, player in enumerate(self.player_name):
                if idx_player + 1 == self.players_num:
                    if wins > runde:
                        player_win = int(input(f"{player} bitte schätze deine Siege: "))
                        player_wins.append({"Gamer": player, "Points": player_win})
                        wins += player_win
                    else:
                        player_win = int(input(f"Achtung {player}! Du darfst NICHT {runde-wins} auswählen, bitte schätze: "))
                        player_wins.append({"Gamer": player, "Points": player_win})
                        wins += player_win
                    break
                player_win = int(input(f"{player} bitte schätze deine Siege: "))
                player_wins.append({"Gamer": player, "Points": player_win})
                wins += player_win

            print("-" * 40)
            print(f"Gesamtanzahl der Siege = {wins}")
            print("-" * 40)

            for gamer in player_wins:
                real_win = int(input(f"{gamer['Gamer']} wie oft hast du gewonnen?: "))
                if real_win == gamer["Points"]:
                    winning_points = 20 + 10 * real_win
                    try:
                        self.player_points[gamer["Gamer"]] = self.player_points[gamer["Gamer"]] + winning_points
                    except Exception:
                        self.player_points[gamer["Gamer"]] = winning_points
                    print(f"--> Glückwunsch {gamer['Gamer']} du erhälst {winning_points} Punkte")
                else:
                    loosing_points = abs(gamer["Points"] - real_win) * 10
                    try:
                        self.player_points[gamer["Gamer"]] = self.player_points[gamer["Gamer"]] - loosing_points
                    except Exception:
                        self.player_points[gamer["Gamer"]] = -loosing_points
                    print(f"--> Schade {gamer['Gamer']} du verlierst {loosing_points} Punkte")
            # Der erste Spieler kommt zum Schluss
            self.player_name.append(self.player_name.pop(self.player_name.index(player_wins[0]["Gamer"])))
            player_wins = []
            print("<---------------------------------- Zwischenstand ---------------------------------->")
            print(sorted(self.player_points.items(), key=lambda x: x[1], reverse=True))
            print("\n")
        print("=============== Das Spiel ist Zuende ===============")
        print(sorted(self.player_points.items(), key=lambda x: x[1], reverse=True))


if __name__ == "__main__":
    wizard = Wizard()
    wizard.run()
