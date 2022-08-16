import datetime
import colorama
import time
import logging


class Wizard:
    def __init__(self):
        """init"""
        self.players_num = None
        self.player_name = None
        self.player_points = {}
        self.current_datetime = datetime.datetime.now().strftime("%Y%m%d_%Hh%Mm")
        self.logger = self.create_logger()
        colorama.init(autoreset=True)

    def create_logger(self):
        logger = logging.getLogger(f"Wizzard_{self.current_datetime}")
        logger.setLevel(logging.DEBUG)
        for handler in reversed(logger.handlers):
            logger.removeHandler(handler)
        # File
        file_handler = logging.FileHandler(f"Log_Wizzard_{self.current_datetime}.txt")
        file_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter("%(asctime)s - %(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        # Console
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter("%(message)s")
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        return logger

    def player_number(self) -> int:
        """number of player

        Returns:
            int: number of player
        """
        self.logger.info(colorama.Fore.CYAN + "Als Erstes wird die Anzahl der Spieler bestimmt.")
        self.logger.info(colorama.Fore.RED + "=> min = 3, max = 6 <=")
        while True:
            try:
                self.players_num = int(input(colorama.Fore.GREEN + "Bitte wähle die Anzahl der Spieler: "))
            except Exception:
                self.logger.info(colorama.Fore.RED + "Die Eingabe ist nicht korrekt, bitte wähle eine Zahl zwischen 3 und 6")
            else:
                if self.players_num < 3 or self.players_num > 6:
                    self.logger.info(colorama.Fore.RED + "Anzahl der Spieler muss zwischen 3 und 6 sein!")
                    continue
                else:
                    self.logger.info(colorama.Fore.GREEN + f"Anzahl der Spieler = {self.players_num }")
                    break
        return self.players_num

    def players_name(self) -> list:
        """name of the players

        Returns:
            list: name of the players
        """
        self.logger.info(colorama.Fore.CYAN + "\nNun werden die Namen der Spieler bestimmt.")
        self.logger.info(colorama.Fore.CYAN + "Starte mit dem Spieler welcher beginnen soll und gehe dann im Uhrzeigersinn weiter!\n")
        if not self.players_num:
            self.players_num = self.player_number()
        self.player_name = [input(colorama.Fore.GREEN + f"Name von Spieler {num+1}: ") for num in range(self.players_num)]
        return self.player_name

    def round_number(self) -> int:
        """number of rounds

        Returns:
            int: number of rounds
        """
        if not self.players_num:
            self.players_num = self.player_number()
        if not self.player_name:
            self.player_name = self.players_name()
        if self.players_num == 3:
            round_num = 20
        elif self.players_num == 4:
            round_num = 15
        elif self.players_num == 5:
            round_num = 12
        else:
            round_num = 10

        self.logger.info(colorama.Fore.RED + "\nWichtiger Hinweiß! Durch eintragen eines Buchstabens kann die Schätzung korrigiert werden.")
        self.logger.info(colorama.Fore.CYAN + f"\nHallo {', '.join(self.player_name)} es werden {round_num} gespielt. Viel Spaß.\n")
        return round_num

    def run(self) -> None:
        """start the game"""
        self.logger.info("\n")
        self.logger.info(colorama.Fore.RED + f"=============================================== Wizard by Kevin Thalmann ===============================================")
        self.logger.info("\n")
        num_rounds = self.round_number()
        player_wins = []
        for idx_round in range(num_rounds):
            wins = 0
            runde = idx_round + 1
            self.logger.info(f"################################################## Runde {runde} von {num_rounds} ##################################################")
            idx_player = 0
            while not idx_player == len(self.player_name):
                if idx_player + 1 == self.players_num:
                    if wins > runde:
                        player_win = input(colorama.Fore.GREEN + f"{self.player_name[idx_player]} bitte schätze deine Siege: ")
                        if player_win.isalpha():
                            if not player_wins:
                                continue
                            self.logger.info(colorama.Fore.RED + f"         --> {self.player_name[idx_player-1]}s Eintrag wird gelöscht.")
                            wins -= player_wins[-1]["Points"]
                            player_wins.pop(-1)
                            idx_player -= 1
                            continue
                        player_wins.append({"Gamer": self.player_name[idx_player], "Points": int(player_win)})
                        wins += int(player_win)
                    else:
                        player_win = input(colorama.Fore.RED + f"Achtung {self.player_name[idx_player]}! Du darfst NICHT {(forbidden_num := runde-wins)} auswählen, bitte schätze: ")
                        if player_win.isalpha():
                            if not player_wins:
                                continue
                            self.logger.info(colorama.Fore.RED + f"         --> {self.player_name[idx_player-1]}s Eintrag wird gelöscht.")
                            wins -= player_wins[-1]["Points"]
                            player_wins.pop(-1)
                            idx_player -= 1
                            continue
                        while forbidden_num == int(player_win):
                            player_win = input(colorama.Fore.RED + f"Achtung {self.player_name[idx_player]}! Du darfst NICHT {(forbidden_num := runde-wins)} auswählen, bitte schätze: ")
                        player_wins.append({"Gamer": self.player_name[idx_player], "Points": int(player_win)})
                        wins += int(player_win)
                    break
                player_win = input(colorama.Fore.GREEN + f"{self.player_name[idx_player]} bitte schätze deine Siege: ")
                if player_win.isalpha():
                    if not player_wins:
                        continue
                    self.logger.info(colorama.Fore.RED + f"               -----> {self.player_name[idx_player-1]}s Eintrag wird gelöscht.")
                    wins -= player_wins[-1]["Points"]
                    player_wins.pop(-1)
                    idx_player -= 1
                    continue
                player_wins.append({"Gamer": self.player_name[idx_player], "Points": int(player_win)})
                wins += int(player_win)
                idx_player += 1
            self.logger.info(colorama.Fore.CYAN + "-" * 40)
            self.logger.info(colorama.Fore.CYAN + f"Gesamtanzahl der Siege = {wins}")
            self.logger.info(colorama.Fore.CYAN + "-" * 40)
            self.logger.info(colorama.Fore.CYAN + "Viel Erfolg bei der Runde ...")
            if runde in [1, 2, 3]:
                time.sleep(5)
            else:
                time.sleep(15)
            for gamer in player_wins:
                real_win = int(input(colorama.Fore.GREEN + f"{gamer['Gamer']} wie oft hast du gewonnen?: "))
                if real_win == gamer["Points"]:
                    winning_points = 20 + 10 * real_win
                    try:
                        self.player_points[gamer["Gamer"]] = self.player_points[gamer["Gamer"]] + winning_points
                    except Exception:
                        self.player_points[gamer["Gamer"]] = winning_points
                    self.logger.info(colorama.Fore.LIGHTGREEN_EX + f"--> Glückwunsch {gamer['Gamer']} du erhälst {winning_points} Punkte")
                else:
                    loosing_points = abs(gamer["Points"] - real_win) * 10
                    try:
                        self.player_points[gamer["Gamer"]] = self.player_points[gamer["Gamer"]] - loosing_points
                    except Exception:
                        self.player_points[gamer["Gamer"]] = -loosing_points
                    self.logger.info(colorama.Fore.LIGHTRED_EX + f"--> Schade {gamer['Gamer']} du verlierst {loosing_points} Punkte")
            # Der erste Spieler kommt zum Schluss
            self.player_name.append(self.player_name.pop(self.player_name.index(player_wins[0]["Gamer"])))
            player_wins = []
            self.logger.info(colorama.Fore.CYAN + "                   <<< Zwischenstand >>>")
            interim = " | ".join([f"{i+1}. {a[0]}: {a[1]} Punkten" for i, a in enumerate(sorted(self.player_points.items(), key=lambda x: x[1], reverse=True))])
            self.logger.info(colorama.Fore.CYAN + interim)
        self.logger.info(colorama.Fore.GREEN + "=============== Das Spiel ist Zuende ===============")
        interim = " | ".join([f"{i+1}. {a[0]}: {a[1]} Punkten" for i, a in enumerate(sorted(self.player_points.items(), key=lambda x: x[1], reverse=True))])
        self.logger.info(colorama.Fore.LIGHTGREEN_EX + interim)
        end_game = input(colorama.Fore.RED + "Wollte ihr das Spiel Wiederholen?  [Y/N]  :")
        if end_game == "N":
            self.logger.info(colorama.Fore.LIGHTGREEN_EX + "Das Spiel wird beendet.")
            quit
        else:
            self.logger.info(colorama.Fore.LIGHTGREEN_EX + "Das Spiel neu gestartet.")
            self.players_num.__del__()
            self.player_name.__del__()
            self.player_points.__del__()
            wizard = Wizard()
            wizard.run()


if __name__ == "__main__":
    wizard = Wizard()
    wizard.run()
# pyinstaller --onefile -c Wizard.py
