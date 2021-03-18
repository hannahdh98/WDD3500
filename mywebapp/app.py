from flask import Flask, url_for, redirect
app = Flask(__name__)

#directs you to the home page
@app.route('/')
def hello_world():
 return "Hello World"

#directs you to the hello admin page
@app.route('/admin')
def admin_page():
 return "welcome to the admin page"

#directs you to the hello guest page
@app.route('/guest/<guest>')
def hello_guest(guest):
 return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
    #if name equals admin then it will redirect to the hello admin page.
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
       # if another name is put in that is not admin, then it will redirect them to the guest page.
       return redirect(url_for('hello_guest',guest = name))


if __name__ == '__main__':
 app.run()