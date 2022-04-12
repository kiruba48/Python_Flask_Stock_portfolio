from flask import render_template, flash, abort
from . import users_blueprint

@users_blueprint.route('/about')
def about():
        # return render_template('about.html')
    flash('Thanks Visiting the site!', 'info')
    return render_template('users/about.html', company_name='kiruba.dev')

@users_blueprint.route('/admin')
def admin():
    abort(403)

# Registering errorhandle in blueprint
@users_blueprint.errorhandler(403)
def page_forbidden(e):
    return render_template('users/403.html'), 403


