from flask import Flask, request, render_template
import os
import random_food

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/test')
def test():
    return "Test"

@app.route('/restart')
def restart():
    #os.system("shutdown -r now")
    os.system("reboot -n")
    return "Done"

@app.route('/reboot')
def reboot():
    os.system("echo b > /sysrq")
    return "Reboot"

@app.route('/allfood')
def allfood():
    foodreturn = random_food.returnFood()
    return render_template("allfood.html", output=foodreturn)

@app.route('/alldrinks')
def alldrinks():
    drinkreturn = random_food.returnDrinks()
    return render_template("alldrinks.html", output=drinkreturn)

@app.route("/randomiser", methods=['GET', 'POST'])
def randomiser():
    if request.method == 'POST':
        if request.form.get('Choose') == 'Choose':
            foodreturn = random_food.foodRandomiser()
            return render_template('randomiser.html', output=foodreturn)
        elif request.form.get('Reset') == 'Reset':
            print("Clear")
        if request.form.get('History') == 'History':
            historyreturn = random_food.returnTen()
            return render_template('randomiser.html', history=historyreturn)
        else:
            # pass # unknown
            return render_template("randomiser.html")
    elif request.method == 'GET':
        # return render_template("index.html")
        print("No Post Back Call")
    return render_template("randomiser.html")

@app.route("/drinksrandomiser", methods=['GET', 'POST'])
def drinksrandomiser():
    if request.method == 'POST':
        if request.form.get('BubbleTea') == 'BubbleTea':
            teareturn = random_food.teaRandomiser()
            return render_template('drinksrandomiser.html', output=teareturn)
        if request.form.get('Coffee') == 'Coffee':
            coffeereturn = random_food.coffeeRandomiser()
            return render_template('drinksrandomiser.html', output=coffeereturn)
        elif request.form.get('Reset') == 'Reset':
            print("Clear")
        if request.form.get('History') == 'History':
            historyreturn = random_food.returnDrinksTen()
            return render_template('drinksrandomiser.html', history=historyreturn)
        else:
            # pass # unknown
            return render_template("drinksrandomiser.html")
    elif request.method == 'GET':
        # return render_template("index.html")
        print("No Post Back Call")
    return render_template("drinksrandomiser.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
