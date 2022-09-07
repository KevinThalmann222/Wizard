import datetime
import time
import logging
import ColorCodes
import os


class Wizard:
    def __init__(self):
        """init"""
        self.players_num = None
        self.player_name = None
        self.player_points = {}
        self.current_datetime = datetime.datetime.now().strftime("%Y%m%d_%Hh%Mm")
        self.logger = self.create_logger()
        os.system("color")

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
        self.logger.info(f"{ColorCodes.fg.lightblue}{ColorCodes.colors.underline}Als Erstes wird die Anzahl der Spieler bestimmt.{ColorCodes.colors.reset}")
        self.logger.info(f"{ColorCodes.fg.red}{ColorCodes.colors.bold}=> min = 3, max = 6 <=")
        while True:
            try:
                self.players_num = int(input(f"{ColorCodes.fg.cyan}Bitte wähle die Anzahl der Spieler: {ColorCodes.colors.reset}"))
            except Exception:
                self.logger.info(f"{ColorCodes.fg.red}Die Eingabe ist nicht korrekt, bitte wähle eine Zahl zwischen 3 und 6{ColorCodes.colors.reset}")
            else:
                if self.players_num < 3 or self.players_num > 6:
                    self.logger.info(f"{ColorCodes.fg.red}Anzahl der Spieler muss zwischen 3 und 6 sein!{ColorCodes.colors.reset}")
                    continue
                else:
                    self.logger.info(f"{ColorCodes.fg.lightblue}Anzahl der Spieler = {self.players_num}{ColorCodes.colors.reset}")
                    break
        return self.players_num

    def players_name(self) -> list:
        """name of the players

        Returns:
            list: name of the players
        """
        self.logger.info(f"{ColorCodes.fg.blue}\nNun werden die Namen der Spieler bestimmt.{ColorCodes.colors.reset}")
        self.logger.info(f"{ColorCodes.fg.blue}Starte mit dem Spieler welcher beginnen soll und gehe dann im Uhrzeigersinn weiter!\n{ColorCodes.colors.reset}")
        if not self.players_num:
            self.players_num = self.player_number()
        self.player_name = [input(f"{ColorCodes.fg.cyan}Name von Spieler {num+1}: {ColorCodes.colors.reset}") for num in range(self.players_num)]
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

        self.logger.info(f"{ColorCodes.fg.blue}{ColorCodes.colors.bold}\nWichtiger Hinweiß! Durch eintragen eines Buchstabens kann die Schätzung korrigiert werden.{ColorCodes.colors.reset}")
        self.logger.info(f"{ColorCodes.fg.lightblue}\nHallo {', '.join(self.player_name)} es werden {round_num} gespielt. Viel Spaß.\n{ColorCodes.colors.reset}")
        return round_num

    def run(self) -> None:
        """start the game"""
        self.logger.info("\n")
        self.logger.info(f"{ColorCodes.fg.lightblue}{ColorCodes.colors.bold}Wizard by Kevin Thalmann{ColorCodes.colors.reset}")
        self.logger.info("\n")
        num_rounds = self.round_number()
        player_wins = []
        for idx_round in range(num_rounds):
            wins = 0
            runde = idx_round + 1
            self.logger.info(f"{ColorCodes.fg.blue}{ColorCodes.colors.bold}{ColorCodes.colors.underline}<                              Runde {runde} von {num_rounds}                             >{ColorCodes.colors.reset}\n")
            idx_player = 0
            while not idx_player == len(self.player_name):
                if idx_player + 1 == self.players_num:
                    if wins > runde:
                        player_win = input(f"{ColorCodes.fg.cyan}{self.player_name[idx_player]} bitte schätze deine Siege: {ColorCodes.colors.reset}")
                        if player_win.isalpha():
                            if not player_wins:
                                continue
                            self.logger.info(f"{ColorCodes.fg.orange}{ColorCodes.colors.bold}         --> {self.player_name[idx_player-1]}s Eintrag wird gelöscht.{ColorCodes.colors.reset}")
                            wins -= player_wins[-1]["Points"]
                            player_wins.pop(-1)
                            idx_player -= 1
                            continue
                        player_wins.append({"Gamer": self.player_name[idx_player], "Points": int(player_win)})
                        wins += int(player_win)
                    else:
                        player_win = input(f"{ColorCodes.fg.red}{ColorCodes.colors.bold}Achtung {self.player_name[idx_player]}! Du darfst NICHT {(forbidden_num := runde-wins)} auswählen, bitte schätze: {ColorCodes.colors.reset}")
                        if player_win.isalpha():
                            if not player_wins:
                                continue
                            self.logger.info(f"{ColorCodes.fg.orange}{ColorCodes.colors.bold}         --> {self.player_name[idx_player-1]}s Eintrag wird gelöscht.{ColorCodes.colors.reset}")
                            wins -= player_wins[-1]["Points"]
                            player_wins.pop(-1)
                            idx_player -= 1
                            continue
                        while forbidden_num == int(player_win):
                            player_win = input(f"{ColorCodes.fg.red}Achtung {self.player_name[idx_player]}! Du darfst NICHT {(forbidden_num := runde-wins)} auswählen, bitte schätze: {ColorCodes.colors.reset}")
                        player_wins.append({"Gamer": self.player_name[idx_player], "Points": int(player_win)})
                        wins += int(player_win)
                    break
                player_win = input(f"{ColorCodes.fg.cyan}{self.player_name[idx_player]} bitte schätze deine Siege: {ColorCodes.colors.reset}")
                if player_win.isalpha():
                    if not player_wins:
                        continue
                    self.logger.info(f"{ColorCodes.fg.orange}{ColorCodes.colors.bold}               -----> {self.player_name[idx_player-1]}s Eintrag wird gelöscht.{ColorCodes.colors.reset}")
                    wins -= player_wins[-1]["Points"]
                    player_wins.pop(-1)
                    idx_player -= 1
                    continue
                player_wins.append({"Gamer": self.player_name[idx_player], "Points": int(player_win)})
                wins += int(player_win)
                idx_player += 1
            self.logger.info(f"{ColorCodes.fg.cyan}-" * 40)
            self.logger.info(f"{ColorCodes.fg.cyan}{ColorCodes.colors.bold}Gesamtanzahl der Siege = {wins}{ColorCodes.colors.reset}")
            self.logger.info(f"{ColorCodes.fg.cyan}-" * 40)
            self.logger.info(f"{ColorCodes.fg.cyan}Viel Erfolg bei der Runde ...{ColorCodes.colors.reset}")
            if runde in [1, 2, 3]:
                time.sleep(5)
            else:
                time.sleep(15)
            for gamer in player_wins:
                real_win = int(input(f"{ColorCodes.fg.cyan}{gamer['Gamer']} wie oft hast du gewonnen?: {ColorCodes.colors.reset}"))
                if real_win == gamer["Points"]:
                    winning_points = 20 + 10 * real_win
                    try:
                        self.player_points[gamer["Gamer"]] = self.player_points[gamer["Gamer"]] + winning_points
                    except Exception:
                        self.player_points[gamer["Gamer"]] = winning_points
                    self.logger.info(f"{ColorCodes.fg.green}{ColorCodes.colors.bold}--> Glückwunsch {gamer['Gamer']} du erhälst {winning_points} Punkte{ColorCodes.colors.reset}")
                else:
                    loosing_points = abs(gamer["Points"] - real_win) * 10
                    try:
                        self.player_points[gamer["Gamer"]] = self.player_points[gamer["Gamer"]] - loosing_points
                    except Exception:
                        self.player_points[gamer["Gamer"]] = -loosing_points
                    self.logger.info(f"{ColorCodes.fg.red}{ColorCodes.colors.bold}--> Schade {gamer['Gamer']} du verlierst {loosing_points} Punkte{ColorCodes.colors.reset}")
            # Der erste Spieler kommt zum Schluss
            self.player_name.append(self.player_name.pop(self.player_name.index(player_wins[0]["Gamer"])))
            player_wins = []
            self.logger.info("\n")
            self.logger.info(f"{ColorCodes.fg.cyan}{ColorCodes.colors.bold}{ColorCodes.colors.underline}<                              Zwischenstand                              >{ColorCodes.colors.reset}")
            interim = f" | ".join([f"{i+1}. {a[0]}: {a[1]} Punkten" for i, a in enumerate(sorted(self.player_points.items(), key=lambda x: x[1], reverse=True))])
            self.logger.info(f"{ColorCodes.fg.lightgrey}{ColorCodes.colors.bold}{interim}{ColorCodes.colors.reset}")
            self.logger.info("\n")
        self.logger.info("\n")
        self.logger.info(f"{ColorCodes.fg.blue}{ColorCodes.colors.bold}{ColorCodes.colors.underline}<                              Das Spiel ist Zuende                               >{ColorCodes.colors.reset}")
        interim = f" | ".join([f"{i+1}. {a[0]}: {a[1]} Punkten" for i, a in enumerate(sorted(self.player_points.items(), key=lambda x: x[1], reverse=True))])
        self.logger.info(f"{ColorCodes.fg.green}{ColorCodes.colors.bold}{interim}{ColorCodes.colors.reset}")
        self.logger.info("\n")
        end_game = input(f"{ColorCodes.fg.cyan}Wollte ihr das Spiel Wiederholen?  [Y/N]  :{ColorCodes.colors.reset}")
        if end_game == "N":
            self.logger.info(f"{ColorCodes.fg.cyan}Das Spiel wird beendet.{ColorCodes.colors.reset}")
            quit
        else:
            self.logger.info(f"{ColorCodes.fg.cyan}Das Spiel neu gestartet.{ColorCodes.colors.reset}")
            self.players_num.__del__()
            self.player_name.__del__()
            self.player_points.__del__()
            wizard = Wizard()
            wizard.run()


if __name__ == "__main__":
    wizard = Wizard()
    wizard.run()
# pip install pip==18.1
# py -m PyInstaller --onefile -c Wizard.py
# python -m pip install --upgrade pip