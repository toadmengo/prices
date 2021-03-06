from flask import Flask, render_template, redirect, request, url_for, session
import ebay
import amazon
import walmart

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
        ebaylist = ebay.main(keyword, 9)
        amazonlist = amazon.main(keyword, 9)
        walmartlist = walmart.main(keyword, 9)
        return render_template('search.html', item = item, amazon = amazonlist, ebay = ebaylist, walmart = walmartlist)

if __name__ == '__main__':
   app.run()