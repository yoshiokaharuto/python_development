from flask import Blueprint,render_template,url_for,request,redirect
import db,string,random


user_bp = Blueprint('user',__name__,url_prefix='/user')

@user_bp.route('/user_register')
def user_register():
    return render_template('user/user_register.html')

@user_bp.route('/user_register_result',methods = ['POST'])
def user_register_result():
    name = request.form.get('name')
    mail = request.form.get('mail')
    pw   = request.form.get('pw')
    
    if name == '':
        error = 'ユーザ名が未入力です'
        return render_template('user/user_register.html',error=error,mail=mail,pw=pw)
    if mail == '':
        error = 'メールアドレスが未入力です'
        return render_template('user/user_register.html',error=error,name=name,pw=pw)    
    if pw == '':
        error = 'パスワードが未入力です'
        return render_template('user/user_register.html',error=error,name=name,mail=mail)
    
    
    count = db.register(name,mail,pw)
    print(count)
    
    if count == 1:
        msg = '登録が完了しました。'
        return redirect(url_for('user.user_register_redirect',msg = msg))
    else:
        error = '登録に失敗しました。'
        return render_template('user/user_register.html',error = error)

@user_bp.route('/user_regsiter_redirect' ,methods=['GET'])
def user_register_redirect():
    
    msg = request.args.get('msg')
    
    print(msg)
    
    if msg == None:
        return render_template('user/user_register.html' , msg=msg)        
    else:
        return render_template('user/user_register_result.html', msg = msg)

    
@user_bp.route('/user_list')
def user_list():
    
    user = db.user_list()
    
    return render_template('user/user_list.html', user_list = user)