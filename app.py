from flask import Flask, escape, render_template, request, session, redirect, url_for;

app = Flask(__name__)

# Secret key for cookie sessions.
# Secret value generated using python secrets module - secrets.token_bytes(32)
app.secret_key = b'\x80\t\xb3Y\x94Q\xb1\xab\\Q\x89\xd3\xd4\xddAV\xbf\x02\xe30\x0c\xa2)\x01\xac\x0b\x1b\xc6\xc0H\xb0*'

@app.route('/')
def index():   
    return render_template('index.html')


@app.route('/about')
def about():
        # return render_template('about.html')
    return render_template('about.html', company_name='kiruba.dev')


@app.route('/add_stock', methods=['GET', 'POST'])
def add_stock():
    if request.method == 'POST':
        for k, v in request.form.items():
            print(f'{k}: {v}')

        # Save the form data to the session object
        session['stock_symbol'] = request.form['stock_symbol']
        session['number_of_shares'] = request.form['number_of_shares']
        session['purchase_price'] = request.form['purchase_price']
        return redirect(url_for('stocks'))

    return render_template('add_stock.html')



@app.route('/stocks/')
def stocks():
    return render_template('stocks.html')

@app.route('/blog_posts/<int:post_id>')
def display_blog_post(post_id):
    return f'<h1>Blog Post #{post_id}...</h1>'