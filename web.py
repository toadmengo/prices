from flask import Flask, render_template, redirect, request, url_for, session
import ebay
import amazon
import newegg

app = Flask(__name__)
app.secret_key = "christmastree"

@app.route('/', methods=["POST", 'GET'])
def home():
    if request.method == 'POST':
        username = request.form["username"]
        session["user"] = username
        return redirect(url_for("main"))
    else:
        return render_template('index.html')

@app.route('/search', methods=["POST", 'GET'])
def main():
    if request.method == 'POST':
        product = request.form["item"]
        return redirect(url_for("search", item=product))
    else:
        user = session['user']
        return render_template('main.html', user=user)

@app.route('/search/<item>', methods=["POST", 'GET'])
def search(item):
    if request.method == 'POST':
        product = request.form["item"]
        return redirect(url_for("search", item=product))
    else:    
        keyword = str(item)
        ebaylist = ebay.main(keyword, 5)
        amazonlist = amazon.main(keyword, 5)
        newegglist = newegg.main(keyword, 5)

        return render_template('search.html', item = item, amazon = amazonlist, ebay = ebaylist, newegg = newegglist)

if __name__ == '__main__':
    app.run(debug=True)