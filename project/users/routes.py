from flask import render_template, flash
from . import users_blueprint

@users_blueprint.route('/about')
def about():
        # return render_template('about.html')
    flash('Thanks Visiting the site!', 'info')
    return render_template('users/about.html', company_name='kiruba.dev')