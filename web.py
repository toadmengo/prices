from flask import Flask, render_template, redirect, request, url_for
import ebay
import amazon
import newegg

app = Flask(__name__)

@app.route('/', methods=["POST", 'GET'])
def home():
    if request.method == 'POST':
        username = request.form["username"]
        return redirect(url_for("main", user=username))
    else:
        return render_template('index.html')

@app.route('/<user>', methods=["POST", 'GET'])
def main(user):
    if request.method == 'POST':
        product = request.form["item"]
        return redirect(url_for("search", item=product))
    else:
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
        for egg in newegglist:
            print(egg[3])
        return render_template('search.html', item = item, amazon = amazonlist, ebay = ebaylist, newegg = newegglist)

if __name__ == '__main__':
    app.run(debug=True)