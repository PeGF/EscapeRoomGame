import socket
from threading import Thread
from fase_controle import GameManager

import socket
import threading
import os

class EscapeRoomServer:
    def __init__(self, host='localhost', port=5558):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen(2)
        self.players = []
        self.player_id = 1
        self.game_manager = GameManager()  # Instância de GameManager
        print("Servidor iniciado. Esperando por conexões...\n")

    def handle_player(self, conn, addr, player_id):
        print(f"Jogador {player_id} conectado: {addr}")
        conn.sendall(f"Bem-vindo ao Escape Room, Jogador {player_id}!\nPara utilizar o Walkie Talkie para se comunicar com o seu aliado, digite o comando /msg e escreva a mensagem.\nPara receber uma dica, digite apenas /hint. \nPara inserir uma tentativa de resposta, digite /key e escreva a sua resposta ao lado.\nBoa sorte em sua fuga!\n\n".encode())

        # Enviar a descrição da sala atual imediatamente após a conexão
        current_room = self.game_manager.get_current_room(player_id)
        current_room.send_description(conn, player_id)

        while True:
            try:
                data = conn.recv(1024).decode()
                if not data:
                    break

                # Comando de mensagem entre jogadores
                if data.startswith("/msg"):
                    message = f"Jogador {player_id} diz: " + data[5:] + "\n"
                    self.broadcast(message, conn)

                elif data.startswith("/hint"):
                    current_room.send_hint(conn, player_id)    

                elif data.startswith("/key"):
                    current_room.handle_player(conn, player_id, self, data.strip())
                    
                    # Se o jogador resolveu o enigma, marca como resolvido
                    if current_room.solution_found:
                        self.game_manager.player_solved_enigma(player_id)
                        
                        # Verifica se todos os jogadores resolveram o enigma e move para a próxima sala
                        if self.game_manager.move_to_next_room():
                            self.clear_terminal()
                            self.broadcast("Todos avançaram para a próxima sala!\n")
                            
                            # Envia a descrição da nova sala para todos os jogadores
                            for player_conn, player_id in zip(self.players, [1, 2]):
                                room = self.game_manager.get_current_room(player_id)
                                room.send_description(player_conn, player_id)
                        else:
                            conn.sendall("Aguardando o outro jogador resolver o enigma...\n".encode())
                
            except ConnectionResetError:
                break

        conn.close()

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def broadcast(self, message, current_conn=None):
        """
        Envia uma mensagem para todos os jogadores, exceto o remetente, se especificado.
        """
        for player in self.players:
            if player != current_conn:
                player.sendall(message.encode())

    def start(self):
        while self.player_id <= 2:
            conn, addr = self.server.accept()
            self.players.append(conn)
            threading.Thread(target=self.handle_player, args=(conn, addr, self.player_id)).start()
            self.player_id += 1
        print("Dois jogadores conectados. Jogo iniciado!\n")
