#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function

import sys


# ==============================================================================
# ROBOT
# Los robots definidos deben heredar de esta clase.
# ==============================================================================

class Bot(object):
    """Bot base. Este bot no hace nada (pasa todos los turnos)."""
    NAME = "NullBot"

    # ==========================================================================
    # Comportamiento del bot
    # Métodos a implementar / sobreescribir (opcionalmente)
    # ==========================================================================

    def __init__(self, init_state):
        if init_state is None:
            self.reset()
            return

        """Inicializar el bot: llamado al comienzo del juego."""
        self.player_num = init_state["player_num"]
        self.player_count = init_state["player_count"]
        self.init_pos = init_state["position"]
        self.map = init_state["map"]
        self.lighthouses = map(tuple, init_state["lighthouses"])

    def reset(self):
        self.player_num = -1
        self.player_count = 0
        self.init_pos = ()
        self.map = list()
        self.lighthouses = list()

    def play(self, state):
        """Jugar: llamado cada turno.
        Debe devolver una acción (jugada).
        
        state: estado actual del juego.
        """
        return self.nop()

    def success(self):
        """Éxito: llamado cuando la jugada previa es válida."""
        pass

    def error(self, message, last_move):
        """Error: llamado cuando la jugada previa no es válida."""
        self.log("Recibido error: %s", message)
        self.log("Jugada previa: %r", last_move)

    # ==========================================================================
    # Utilidades
    # No es necesario sobreescribir estos métodos.
    # ==========================================================================

    def log(self, message, *args):
        """Mostrar mensaje de registro por stderr"""
        print("[%s] %s" % (self.NAME, (message % args)), file=sys.stderr)

    # ==========================================================================
    # Jugadas posibles
    # No es necesario sobreescribir estos métodos.
    # ==========================================================================

    @staticmethod
    def nop():
        """Pasar el turno"""
        return {
            "command": "pass",
        }

    @staticmethod
    def move(x, y):
        """Mover a una casilla adyacente
        
        x: delta x (0, -1, 1)
        y: delta y (0, -1, 1)
        """
        return {
            "command": "move",
            "x": x,
            "y": y
        }

    @staticmethod
    def attack(energy):
        """Atacar a un faro
        
        energy: energía (entero positivo)
        """
        return {
            "command": "attack",
            "energy": energy
        }

    @staticmethod
    def connect(destination):
        """Conectar a un faro remoto
        
        destination: tupla o lista (x,y): coordenadas del faro remoto
        """
        return {
            "command": "connect",
            "destination": destination
        }
