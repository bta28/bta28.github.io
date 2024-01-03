#!/usr/bin/python3

import random
import argparse
import sys
import json
from datetime import datetime


class FoodChooser:
    def __init__(self, foodsrc, choice):
        self.foodsrc = foodsrc
        self.choice = choice
        self.options = None

    def importFood(self):
        f = open(self.foodsrc)
        data = json.load(f)
        self.options = data['foodOptions']

    def importDrinks(self):
        f = open(self.foodsrc)
        data = json.load(f)
        self.options = data['drinkOptions']

    def randomChooser(self):
        foodChoice = self.choice
        if foodChoice == 'all':
            category = random.choice(list(self.options.keys()))
            foodChoice = category

        foodSel = random.choice(self.options[foodChoice])
        print("Category: {0}, Choice: {1}\n".format(foodChoice, foodSel))

        return(foodChoice, foodSel)

class FoodLogger:
    def __init__(self, fHistory):
        self.fHistory = fHistory

    def writeList(self, rest, food):
        dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        with open(self.fHistory, 'a') as f:
            wStr = "[{0}] {1}, {2}\n".format(dt_string, rest, food)
            f.write(wStr)

    def readList(self):
        with open(self.fHistory, 'r') as f:
            lista = f.readlines()
            lista.reverse()
            for i in lista:
                print(i.rstrip())
        f.close()

    def readListTen(self):
        listten = []
        print("Last 10 choices")
        with open(self.fHistory, 'r') as f:
            lista = f.readlines()
            lista = lista[-10:]
            lista.reverse()
            for i in lista:
                print(i.rstrip())
                listten.append(i)
        f.close()
        return listten


def arg_parser(args):
    if args.fOptions:
        print("Food options:")
        for i in foodOptions:
            print(i)
        sys.exit(0)

    if args.fPast:
        print("Past choices:")
        read_list(args)
        sys.exit(0)

def foodRandomiser():
    global foodOptions

    fc = FoodChooser("food.json", "all")
    fc.importFood()
    foodOptions = fc.options
    (fcat, fchoice) = fc.randomChooser()

    fl = FoodLogger("food.history")
    fl.writeList(fcat, fchoice)
    return("Category: {0}, Choice: {1}\n".format(fcat, fchoice))

def teaRandomiser():
    global drinkOptions

    fc = FoodChooser("food.json", "bubbletea")
    fc.importDrinks()
    drinkOptions = fc.options
    (fcat, fchoice) = fc.randomChooser()

    fl = FoodLogger("drinks.history")
    fl.writeList(fcat, fchoice)
    return("Category: {0}, Choice: {1}\n".format(fcat, fchoice))

def coffeeRandomiser():
    global drinkOptions

    fc = FoodChooser("food.json", "coffee")
    fc.importDrinks()
    drinkOptions = fc.options
    (fcat, fchoice) = fc.randomChooser()

    fl = FoodLogger("drinks.history")
    fl.writeList(fcat, fchoice)
    return("Category: {0}, Choice: {1}\n".format(fcat, fchoice))


def returnTen():
    fl = FoodLogger("food.history")
    listten = fl.readListTen()
    return(listten)

def returnDrinksTen():
    fl = FoodLogger("drinks.history")
    listten = fl.readListTen()
    return(listten)

def returnFood():
    global foodOptions

    fc = FoodChooser("food.json", "all")
    fc.importFood()
    return(fc.options)

def returnDrinks():
    global drinkOptions

    fc = FoodChooser("food.json", "all")
    fc.importDrinks()
    return(fc.options)
