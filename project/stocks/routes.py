from flask import current_app, render_template, request, session, flash, redirect, url_for
from . import stocks_blueprint

################
#### routes ####
################

@stocks_blueprint.route('/')
def index():   
    current_app.logger.info('Calling the index function.')
    return render_template('stocks/index.html')

@stocks_blueprint.route('/add_stock', methods=['GET', 'POST'])
def add_stock():
    if request.method == 'POST':
        # Save the form data to the session object
        session['stock_symbol'] = request.form['stock_symbol']
        session['number_of_shares'] = request.form['number_of_shares']
        session['purchase_price'] = request.form['purchase_price']
        # Setting Flash message
        flash(f"Added new stock ({request.form['stock_symbol']})!", 'success')
        # Log new stock added
        current_app.logger.info(f"Added new stock ({request.form['stock_symbol']})!")
        
        return redirect(url_for('stocks.list_stocks'))
    
    return render_template('stocks/add_stock.html')

@stocks_blueprint.route('/stocks/')
def list_stocks():
    return render_template('stocks/list_stocks.html')
