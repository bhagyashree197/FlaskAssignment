from flask import Flask,render_template,url_for,flash,redirect
from forms import RegistrationForm,LoginForm
app=Flask(__name__)
app.config['SECRET_KEY']='bhagyashree197'

posts=[
{
	'author':'Bhagyashree Porwal',
	'title':'Blog Post 1',
	'content':'FIRST POST CONTENT',
	'date_posted':'April 20,2018'
},
{
	'author':'Jenny Porwal',
	'title':'Blog Post 2',
	'content':'SECOND POST CONTENT',
	'date_posted':'April 22,2010'
}

]

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html',posts=posts,title='abc')


@app.route("/about")
def about():
	return render_template('about.html',title="about")

@app.route("/register",methods=['GET','POST'])
def register():
	form=RegistrationForm()
	if form.validate_on_submit():
		flash('Account Successfully Created!','success')
		return redirect(url_for('home'))
	return render_template('register.html',title="Register",form=form)

@app.route("/login",methods=['POST','GET'])
def login():
	login=LoginForm()
	if login.validate_on_submit():
		if login.email.data =="admin@blog.com" and login.password.data=="root":
			flash("Successfully Logged in",'success')
			return redirect(url_for('home'))
		else:
			flash('Login Unsuccessful','danger')
	return render_template('login.html',title="Login",form=login)


if __name__=="__main__":
	app.run(debug=True)
