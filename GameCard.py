class Players:
    def __init__(self, names=None, count=5, max_score=100):
        self.max_score = max_score
        
        # Collect names if not passed directly
        if names is None:
            self.players = {
                input(f"Enter name for Player {i + 1}: ").strip(): []
                for i in range(count)
            }
        else:
            self.players = {name.strip(): [] for name in names}

    def add_score(self, scores: dict):
        """
        Pass scores as a dictionary: {player_name: score_this_round}
        Omit a player or pass None/0 if eliminated or not scoring.
        """
        round_summary = {}

        for name, history in self.players.items():
            current_total = sum(history)

            # Check if player is already eliminated
            if current_total >= self.max_score:
                round_summary[name] = "Thrown out"
                continue

            # Add new score if provided
            points = scores.get(name)
            if points is not None:
                history.append(points)
                new_total = sum(history)

                if new_total >= self.max_score:
                    print(f"{name} reached {new_total} and is Thrown Out!")
                    round_summary[name] = "Thrown out"
                else:
                    print(f"{name}: {history} | Total = {new_total}")
                    round_summary[name] = points
            else:
                round_summary[name] = 0

        print(f"\nRound Summary: {round_summary}\n")

    def active_players(self):
        """Returns players still in the game."""
        return [
            name for name, history in self.players.items() 
            if sum(history) < self.max_score
        ]
