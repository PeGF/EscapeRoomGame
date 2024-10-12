import re

class SalaBase:
    def __init__(self):
        self.solution_found = False

    def handle_player(self, conn, player_id, server, input_solution):
        """
        Método para lidar com a interação do jogador. 
        Implementado nas classes derivadas.
        """
        pass

    def send_description(self, conn, player_id):
        """
        Método para enviar a descrição inicial da sala.
        Implementado nas classes derivadas.
        """
        pass

class Sala1(SalaBase):
    def send_description(self, conn, player_id):
        description1 = "[SALA 1]\n\nDescrição: Você se encontra em uma sala quadrada de pedra com uma iluminação suave proveniente de tochas presas nas paredes.\nÀ sua frente, há três formas geométricas esculpidas na parede: um círculo, um triângulo e um quadrado, dispostas nessa ordem.\nAbaixo de cada uma das formas, há números gravados: 8, 5, 3, respectivamente.\nContudo, há espaços vazios ao lado de cada forma, onde parece faltar uma letra.\nA frase gravada abaixo das formas diz: \"O que falta deve ser completado, mas tome cuidado, pois a ordem importa.\"\nVocê sente uma leve corrente de ar vinda de uma fenda na parede, e o som de um relógio distante faz o tempo parecer correr mais rápido.\n"
        description2 = "[SALA 1]\n\nDescrição: Você se encontra em uma sala de pedra com ar frio e paredes úmidas.\nÀ sua frente, três formas geométricas estão esculpidas na parede: um quadrado, um círculo e um triângulo, dispostas nessa ordem.\nAbaixo de cada uma das formas, há letras gravadas: A, C, B, respectivamente.\nNo entanto, ao lado de cada forma, há espaços vazios onde parece faltar um número.\nA frase gravada na parede diz: \"O que falta deve ser completado, mas a ordem importa.\"\nUm leve som de gotejamento ecoa pela sala, reforçando a sensação de estar em um lugar isolado e frio.\n"
        
        if player_id == 1:
            conn.sendall(description1.encode())
        elif player_id == 2:
            conn.sendall(description2.encode())

    def handle_player(self, conn, player_id, server, input_solution):
        text = re.sub(r'[^a-zA-Z0-9]', '', input_solution)
        answer = text.upper()
        if player_id == 1 and (answer[3:].strip() == "CBA"):
            self.solution_found = True
            conn.sendall("Uma porta se abriu e você pode avançar para a próxima sala.\n".encode())
        if player_id == 2 and (answer[3:].strip() == "385"):
            self.solution_found = True
            conn.sendall("Uma porta se abriu e você pode avançar para a próxima sala.\n".encode())
        else:
            if not self.solution_found:
                conn.sendall("Nada aconteceu...\n".encode())

    def send_hint(self, conn, player_id):
        hint1 = "Você sabe que os números 8, 5 e 3 correspondem ao círculo, triângulo e quadrado, mas as letras que faltam devem vir de outra fonte — provavelmente algo que o outro jogador vê.\nSeu objetivo é descobrir quais letras se associam a essas formas e preencher as lacunas.\n\n"
        hint2 = "As letras A, C e B correspondem ao quadrado, círculo e triângulo, mas você precisa descobrir quais números associar a essas formas, o que provavelmente será fornecido pelo outro jogador.\n Seu objetivo é completar os números corretamente, assim como o outro jogador deve completar suas letras.\n\n"

        if player_id == 1:
            conn.sendall(hint1.encode())
        elif player_id == 2:
            conn.sendall(hint2.encode())

class Sala2(SalaBase):
    def send_description(self, conn, player_id):
        description1 = "[SALA 2]\n\nDescrição: Você se encontra em uma sala com uma pequena ilha cercada por água, com o som das ondas calmas batendo ao seu redor.\nAo seu lado, há uma estátua imponente, erguida sobre um pedestal maciço.\nEla retrata uma figura feminina, vestida com uma longa túnica, segurando uma tocha elevada em uma das mãos.\nEm sua outra mão, ela segura uma tábua com uma inscrição antiga. No alto de sua cabeça, uma coroa com pontas se destaca.\nUma placa próxima a você diz:\"Este monumento, presente de um país amigo, simboliza a liberdade e a esperança, saudando aqueles que buscam um novo lar.\"\nCumprimente seu amigo na língua do lugar onde ele está.\n"
        description2 = "[SALA 2]\n\nDescrição: Você se encontra em uma sala com uma praça aberta, cercada por jardins cuidadosamente organizados.\nNa sua frente, ergue-se uma estrutura metálica colossal, composta por arcos intricados e linhas de ferro que se entrelaçam, criando uma forma triangular que afina conforme sobe ao céu.\nA estrutura, enfeitada por pequenas luzes, parece dominar a paisagem.\nAo seu lado, uma pequena placa no chão diz: \"Essa torre foi concluída no final do século XIX, representando um marco de engenharia que se eleva mais de 300 metros acima da cidade.\"\nCumprimente seu amigo na língua do lugar onde ele está.\n"
        
        if player_id == 1:
            conn.sendall(description1.encode())
        elif player_id == 2:
            conn.sendall(description2.encode())

    def handle_player(self, conn, player_id, server, input_solution):
        text = re.sub(r'[^a-zA-Z0-9]', '', input_solution)
        answer = text.upper()
        if player_id == 1 and (answer[3:].strip() == "BONJOUR"):
            self.solution_found = True
            conn.sendall("Très bien! Vous pouvez passer à la pièce suivante\n".encode())
        if player_id == 2 and (answer[3:].strip() == "HELLO" or input_solution[5:].strip() == "HI"):
            self.solution_found = True
            conn.sendall("Nice! You can now go to the next room\n".encode())
        else:
            if not self.solution_found:
                conn.sendall("Nada aconteceu...\n".encode())
    
    def send_hint(self, conn, player_id):
        hint1 = "Seu amigo está em uma cidade famosa por sua ligação com liberdade, onde uma enorme estátua segura uma tocha como um farol de esperança.\nTalvez seja uma cidade que nunca dorme\n\n"
        hint2 = "Seu amigo está em uma cidade famosa por seu charme romântico, onde uma torre de ferro foi erguida para uma grande exposição há mais de cem anos.\nO monumento é hoje um dos mais visitados e símbolo da cidade.\n\n"

        if player_id == 1:
            conn.sendall(hint1.encode())
        elif player_id == 2:
            conn.sendall(hint2.encode())

class Sala3(SalaBase):
    def send_description(self, conn, player_id):
        description1 = "[SALA 3]\n\nDescrição: Você se encontra no que parece ser a sala de navegação de um antigo navio.\nA madeira rangente e o som distante das ondas revelam que você está em uma embarcação antiga, o HMS Beagle, como indica a placa envelhecida sobre a mesa.\nDiante de você, um grande mapa está preso à mesa com tachas douradas, mostrando rotas antigas e uma linha pontilhada que sai do Cabo da Boa Esperança, no Sul da África e segue rumo à América do Sul.\nAo lado do mapa, uma bússola tremula com o balanço das ondas, apontando para o norte.\nObjetos estranhos estão espalhados pela sala, incluindo velhos instrumentos náuticos, lunetas e uma ampulheta quase cheia.\nAlgo na disposição das rotas e da bússola parece essencial. Quem te guiará nessa viagem?\n"
        description2 = "[SALA 3]\n\nDescrição: Você está em um pequeno compartimento do HMS Beagle, com paredes de madeira escura, iluminado apenas por uma vela.\nAo centro, um púlpito sustenta um antigo livro. Ao abri-lo, você vê descrições de quatro estrelas da constelação Ursa Maior: Dubhe, Merak, Phecda e Megrez.\nO livro explica que essas estrelas são frequentemente usadas para guiar viajantes, especialmente marinheiros.\nDubhe: \'A estrela mais brilhante, usada para orientar rumo ao norte.\'\nMerak: \'Conhecida por guiar viajantes para o oeste, junto com Dubhe, aponta para a direção do Polo Norte Celestial.\'\nPhecda: \'Uma estrela de brilho moderado, situada mais ao sul, usada ocasionalmente para viagens meridionais.\'\nMegrez: \'A menor e menos brilhante das quatro, raramente usada para navegação.\'\nQual delas você irá seguir?\n"

        if player_id == 1:
            conn.sendall(description1.encode())
        elif player_id == 2:
            conn.sendall(description2.encode())

    def handle_player(self, conn, player_id, server, input_solution):
        text = re.sub(r'[^a-zA-Z0-9]', '', input_solution)
        answer = text.upper()
        if answer[3:].strip() == "MERAK":
            self.solution_found = True
            conn.sendall("As estrelas te guiam rumo à direção correta.\n".encode())
        else:
            if not self.solution_found:
                conn.sendall("Nada aconteceu...\n".encode())

    def send_hint(self, conn, player_id):
        hint1 = "Você percebe que o mapa e a bússola indicam que a maior parte da rota segue para o oeste. Talvez uma estrela que ajude a guiar essa direção seja a chave.\n\n"
        hint2 = "Para qual direção este navio precisa ir? Talvez o seu companheiro na sala ao lado tenha a resposta.\n\n"

        if player_id == 1:
            conn.sendall(hint1.encode())
        elif player_id == 2:
            conn.sendall(hint2.encode())
