from flask import Blueprint, render_template, redirect, url_for, request, flash, session
auth_bp = Blueprint('auth', __name__) # blueprint object ko create kiya hai, jise hum routes define karne ke liye use karenge
User_credentials = {
    'user': 'admin',  # hardcoded username and password for simplicity        
    'password': '123'
}
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == User_credentials['user'] and password == User_credentials['password']:
            
            session['logged_in'] = True
            session['user_id'] = username
            flash('Login successful!', 'success') 
            return redirect(url_for('tasks.view_tasks'))
        else:
            flash('Invalid credentials. Please try again.', 'danger')
    return render_template('login.html')


@auth_bp.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.login'))



# % extends "base.html" %}
# iska mtlb h isse bolre h base.html ka layout use kr