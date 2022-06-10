from flask import Flask,render_template,request,session,redirect,url_for
app=Flask(__name__)
app.config['SECRET_KEY']='1234'

#building the route
@app.route('/')
def home():
    return '''<h1 style="color:red;"> 
    Hello Everyone</h1>
    <p>This is a paragraph</p>
    '''

emails=['user1@gmail.com','user2@gmail.com','user3@gmail.com']
passwords=[123,456,789]

@app.route('/register',methods=["GET",'POST'])
def register():
    if request.method=='GET':
        name=session.get('my_name','user')
        message='Hello ' + name + ' Welcome to Registration Page'
        return render_template('register.html',message=message)
    elif request.method=='POST':
        name=request.form.get('name')
        email=request.form.get('email')
        password=request.form.get('password')
        age=int(request.form.get('age'))
        # Check whether email is already present in the list
        if email in emails:
            message='Email Id already exist'
        elif email not in emails:
            if age>=12:
                message='Hi '+name+' registration successful'
                emails.append(email)
                passwords.append(password)
                session['my_email']=email
                session['my_password']=password
            else:
                message='Age should be more than or equal to 12'
        return render_template('register.html',message=message)

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    elif request.method=='POST':
        email=request.form.get('email')
        password=request.form.get('password')
        email_session=session.get('my_email')
        password_session=session.get('my_password')
        message=''
        # if email==email_session and password==password_session:
        if True:
            message='Login Successful'
            session['authenticated']=True#session={'authenticated':True}
            return render_template('quizinstructions.html',message=message)
        else:
            message='Either email or password is incorrect'
            return render_template('login.html',messsage=message)



# QUIZ APPLICATION

@app.route('/quiz')
def quiz():
    return render_template('quizinstructions.html')

#Question1
@app.route('/q1', methods=['GET', 'POST'])
def q1():
    score=session.get('score',0)#0
    #User is not logged in
    # if session.get('authenticated') !=True:
    #     return redirect('/login')
    if request.method=='GET':
        return render_template('question1.html')
    elif request.method=='POST':
        correct_answer='1'
        user_option=request.form.get('option')
        print(user_option)
        message=''
        if user_option==correct_answer:
            message='Your answer is correct'
            score=score+10
            #replacing new score in session
            session['score']=score
        else:
            message='Your answer is wrong' 
    return render_template('question1.html',message=message)


#Question2
@app.route('/q2', methods=['GET', 'POST'])
def q2():
    score=session.get('score',0)
    if request.method=='GET':
        return render_template('question2.html')
    elif request.method=='POST':
        correct_answer='3'
        user_option=request.form.get('option')
        message=''
        if user_option==correct_answer:
            message='Your answer is correct'
            score=score+10
            session['score']=score
        else:
            message='Your answer is wrong'
    return render_template('question2.html',message=message)


#Question3
@app.route('/q3', methods=['GET', 'POST'])
def q3():
    score=session.get('score',0)
    if request.method=='GET':
        return render_template('question3.html')
    elif request.method=='POST':
        correct_answer='5'
        user_option=request.form.get('option')
        message=''
        if user_option==correct_answer:
            message='Your answer is correct'
            score=score+10
            session['score']=score
        else:
            message='Your answer is wrong'
    return render_template('question3.html',message=message)

#Question4
@app.route('/q4', methods=['GET', 'POST'])
def q4():
    score=session.get('score',0)
    if request.method=='GET':
        return render_template('question4.html')
    elif request.method=='POST':
        correct_answer='4'
        user_option=request.form.get('option')
        message=''
        if user_option==correct_answer:
            message='Your answer is correct'
            score=score+10
            session['score']=score
        else:
            message='Your answer is wrong'
    return render_template('question4.html',message=message)


#Question5
@app.route('/q5', methods=['GET', 'POST'])
def q5():
    score=session.get('score',0)
    if request.method=='GET':
        return render_template('question5.html')
    elif request.method=='POST':
        correct_answer='1'
        user_option=request.form.get('option')
        message=''
        if user_option==correct_answer:
            message='Your answer is correct'
            score=score+10
            session['score']=score
        else:
            message='Your answer is wrong'
    return render_template('question5.html',message=message)

#Question6
@app.route('/q6', methods=['GET', 'POST'])
def q6():
    score=session.get('score',0)
    if request.method=='GET':
        return render_template('question6.html')
    elif request.method=='POST':
        correct_answer='2'
        user_option=request.form.get('option')
        message=''
        if user_option==correct_answer:
            message='Your answer is correct'
            score=score+10
            session['score']=score
        else:
            message='Your answer is wrong'
    return render_template('question6.html',message=message)

leaderboard=[[1,'test1','test1@gmail.com',50],
            [2,'test1','test1@gmail.com',50],
            [3,'test1','test1@gmail.com',50],
            [4,'test1','test1@gmail.com',50],
            [5,'test1','test1@gmail.com',50],
            [6,'anand','anand@gmail.com',40]]

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404
        
@app.route('/leaderboard')
def leaderboard_data():
    return render_template('leaderboard.html',leaderboard=leaderboard)


    
if __name__=='__main__':
    app.run(debug=True)