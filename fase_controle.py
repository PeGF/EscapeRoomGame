from salas import Sala1, Sala2, Sala3

class GameManager:
    def __init__(self):
        self.current_room_index = 0
        self.rooms = [Sala1(), Sala2(), Sala3()]
        self.players_in_room = {1: 0, 2: 0}  # controla em qual sala cada jogador está
        self.player_solved = {1: False, 2: False}  # controla se cada jogador resolveu o enigma

    def get_current_room(self, player_id):
        room_index = self.players_in_room[player_id]
        return self.rooms[room_index]

    def player_solved_enigma(self, player_id):
        self.player_solved[player_id] = True

    def check_progress(self):
        # Verifica se ambos os jogadores resolveram seus enigmas
        return all(self.player_solved.values())

    def move_to_next_room(self):
        if self.check_progress():
            # Reseta a condição de solução e avança os jogadores
            self.current_room_index += 1
            self.players_in_room[1] = self.current_room_index
            self.players_in_room[2] = self.current_room_index
            self.player_solved = {1: False, 2: False}  # Reseta para a próxima sala
            return True
        return False

    def advance_room(self):
        if self.current_room_index < len(self.rooms) - 1:
            self.current_room_index += 1
            return True
        return False
