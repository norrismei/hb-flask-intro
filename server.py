"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

INSULTS = ['flabby', 'obnoxious', 'vile', 'annoying', 'boring',
    'a waste of space']


@app.route('/')
def start_here():
    """Home page."""

    return """<!doctype html><html>Hi! This is the home page. 
    <a href="/hello">Say hello</a></html>


    """


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There! Get a compliment</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">

          <div>Select a compliment: </div>
          <select name="compliment">
            <option value="{AWESOMENESS[0]}">{AWESOMENESS[0]}</option>
            <option value="{AWESOMENESS[1]}">{AWESOMENESS[1]}</option>
            <option value="{AWESOMENESS[2]}">{AWESOMENESS[2]}</option>
            <option value="{AWESOMENESS[3]}">{AWESOMENESS[3]}</option>
            <option value="{AWESOMENESS[4]}">{AWESOMENESS[4]}</option>
            <option value="{AWESOMENESS[5]}">{AWESOMENESS[5]}</option>
            <option value="{AWESOMENESS[6]}">{AWESOMENESS[6]}</option>
            <option value="{AWESOMENESS[7]}">{AWESOMENESS[7]}</option>
            <option value="{AWESOMENESS[8]}">{AWESOMENESS[8]}</option>
            <option value="{AWESOMENESS[9]}">{AWESOMENESS[9]}</option>
            <option value="{AWESOMENESS[10]}">{AWESOMENESS[10]}</option>
            <option value="{AWESOMENESS[11]}">{AWESOMENESS[11]}</option>
            <option value="{AWESOMENESS[12]}">{AWESOMENESS[12]}</option>
            <option value="{AWESOMENESS[13]}">{AWESOMENESS[13]}</option>
          </select>
          <input type="submit" value="Submit">
        </form>

        <h1>Or get a diss</h1>
        <form action="/diss">
          What's your name? <input type="text" name="name">

          <div>Select a diss: </div>
            <select name="diss">
              <option value="{INSULTS[0]}">{INSULTS[0]}</option>
              <option value="{INSULTS[1]}">{INSULTS[1]}</option>
              <option value="{INSULTS[2]}">{INSULTS[2]}</option>
              <option value="{INSULTS[3]}">{INSULTS[3]}</option>
              <option value="{INSULTS[4]}">{INSULTS[4]}</option>
              <option value="{INSULTS[5]}">{INSULTS[5]}</option>
            </select>
            <input type="submit" value="Submit">
          </form>

      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)


@app.route('/diss')
def diss_person():
    """Get user by name."""

    player = request.args.get("name")

    diss = request.args.get("diss")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A DISS</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, diss)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
