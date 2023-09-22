from flask import Flask, render_template, jsonify

app = Flask(__name__)

Robots = [{
    'id': 1,
    'title': 'Fire Extingusher',
    'price': '₹1000'
}, {
    'id': 2,
    'title': 'Room Cleaner',
    'price': '₹2000'
}, {
    'id': 3,
    'title': 'Weed Plucker',
    'price': '₹500'
}]


@app.route("/")
def mara():
  return render_template('home.html', robots=Robots)


@app.route("/api/robots")
def list_robots():
  return jsonify(Robots)


# print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
