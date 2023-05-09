#!/usr/bin/env python3
import ipdb

from classes.player import Player
from classes.game import Game
from classes.result import Result

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")


    prob = Player('prob22')
    ttags = Player('ttagtickles')
    emkay = Player('emkayshray')

    skiball = Game("Ski ball")
    pinball = Game("pinball")
    horseshoes = Game("horse shoes")

    r1 = Result(prob, skiball, 4050)
    r2 = Result(prob, skiball, 3000)
    r3 = Result(emkay, skiball, 300)
    r4 = Result(emkay, pinball, 5000)
    r5 = Result(ttags, horseshoes, 45)
    r6 = Result(prob, horseshoes, 100)
    r7 = Result(ttags, skiball, 2000)

    ipdb.set_trace()
