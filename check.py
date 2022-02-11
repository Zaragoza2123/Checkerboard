from flask import Flask, render_template
app = Flask(__name__)

@app.route('/<int:x>/<int:y>/<color1>/<color2>')

def board(x,y,color1,color2):
    return render_template('board.html', x=x, y=y, color1 = color1, color2 = color2 )


if __name__=="__main__":
    app.run(debug=True)