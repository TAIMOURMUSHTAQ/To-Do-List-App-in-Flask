#Login Logout routes

from flask import Blueprint,render_template,request,redirect,url_for,flash,session
auth_bp=Blueprint('auth',__name__)

#Creating dummy users for testing/ we have to provide user feature to register himself and store it for login
USER_CREDENTIALS={
    'admin':'123',
    'Taimour':'1234',
    'Abdul':'0000'
}

@auth_bp.route('/')
def home():
    return render_template('home.html')

#Route for Login
@auth_bp.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        username=request.form.get('username')
        password=request.form.get('password')
        if USER_CREDENTIALS.get(username)==password:
            session['user']=username
            flash('Login Sucessful','success')
            return redirect(url_for('tasks.view_tasks'))
        flash('Invalid credentials','danger')
    return render_template('login.html')

@auth_bp.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        username=request.form.get('username','').strip()
        password=request.form.get('password','')
        confirm=request.form.get('confirm','')
        if not username or not password:
            flash('Username and password are required','danger')
            return render_template('register.html')
        if username in USER_CREDENTIALS:
            flash('Username already exists','danger')
            return render_template('register.html')
        if password != confirm:
            flash('Passwords do not match','danger')
            return render_template('register.html')
        USER_CREDENTIALS[username]=password
        session['user']=username
        flash('Account created successfully','success')
        return redirect(url_for('tasks.view_tasks'))
    return render_template('register.html')

#Route for Login
@auth_bp.route('/logout')
def logout():
    session.pop('user',None)
    flash('Logout','info')
    return redirect(url_for('auth.login'))

