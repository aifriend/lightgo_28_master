import random

import interface


class RandBot(interface.Bot):
    """Bot que juega aleatoriamente."""
    NAME = "RandBot"

    def play(self, state):
        """

        Jugar: llamado cada turno.
        Debe devolver una accion (jugada).
        """
        cx, cy = state["position"]
        lighthouses = dict((tuple(lh["position"]), lh)
                           for lh in state["lighthouses"])

        # Si estamos en un faro...
        if (cx, cy) in lighthouses:
            # Probability 60%: connect with a valid remote lighthouse
            if lighthouses[(cx, cy)]["owner"] == self.player_num:
                if random.randrange(100) < 60:
                    possible_connections = []
                    for dest in self.lighthouses:
                        # No conectar con sigo mismo
                        # No conectar si no tenemos la clave
                        # No conectar si ya existe la conexion
                        # No conectar si no controlamos el destino
                        # Nota: no comprobamos si la conexion se cruza.
                        if (dest != (cx, cy) and
                                lighthouses[dest]["have_key"] and
                                [cx, cy] not in lighthouses[dest]["connections"] and
                                lighthouses[dest]["owner"] == self.player_num):
                            possible_connections.append(dest)

                    if possible_connections:
                        return self.connect(random.choice(possible_connections))

            # Probabilidad 60%: recargar el faro
            if random.randrange(100) < 60:
                energy = random.randrange(state["energy"] + 1)
                return self.attack(energy)

        # Mover aleatoriamente
        moves = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
        # Valid moves
        moves = [(x, y) for x, y in moves if self.map[cy + y][cx + x]]
        move = random.choice(moves)
        self.log("MOVE TO: %s", str(move))
        return self.move(*move)


if __name__ == "__main__":
    iface = interface.Interface(RandBot)
    iface.run()
