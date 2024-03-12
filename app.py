import random

from flask import Flask, render_template, request, redirect, url_for
import pymysql
import sys
import importlib
import math
import datetime

importlib.reload(sys)

app = Flask(__name__)
mysql_pwd = '123456'
db_name = "canteen_management"
# 全局变量
username = ""
userRole = ""
notFinishedNum = 0
# 上传文件要储存的目录
UPLOAD_FOLDER = '/static/images/'
# 允许上传的文件扩展名的集合
ALLOWED_EXTENSIONS = set([ 'png', 'jpg', 'jpeg'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/consumer_index',methods=['GET', 'POST'])
def consumer_index():
    print("2325")
    return render_template('consumer_index.html')


# 用户注册
@app.route('/consumer_register', methods=['GET', 'POST'])
def registerPage():
    global username
    global userRole
    msg = ""
    if request.method == 'GET':
        return render_template('consumer_Register.html')
    if request.method == 'POST':
        id = request.form.get('id')
        username = request.form.get('username')
        password = request.form.get('password')
        title = request.form.get('title')
        phone = request.form.get('phone')
        addr = request.form.get('addr')
        # 连接数据库
        db = pymysql.connect(host="127.0.0.1", user='root', password=mysql_pwd, database=db_name,charset='utf8')

        cursor = db.cursor()
        try:
            cursor.execute("use canteen_management")
        except:
            print("Error: unable to use database!")
        sql1 = "SELECT * from consumer where id_consumer = '{}' ".format(id)
        cursor.execute(sql1)
        db.commit()
        res1 = cursor.fetchall()
        num = 0
        for row in res1:
            num = num + 1
        # 如果已经存在
        if num == 1:
            print("失败！用户已注册！")
            msg = "fail1"
        else:
            sql2 = "insert into consumer (id_consumer, name_consumer, key_consumer, title, tele_consumer,address_consumer) values ('{}', '{}', '{}', '{}', '{}', '{}') ".format(id, username, password, title, addr, phone)

            try:
                cursor.execute(sql2)
                db.commit()
                print("用户注册成功")
                msg = "done1"
            except ValueError as e:
                print("--->", e)
                print("注册出错，失败")
                msg = "fail1"
        return render_template('consumer_Register.html', messages=msg, username=username, userRole=userRole)

# 用户登录
@app.route('/consumer_login', methods=['GET', 'POST'])
def logInPage():
    global username
    global userRole
    msg = ""
    if request.method == 'GET':
        return render_template('consumer_Login.html')
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # 连接数据库
        db =  pymysql.connect(
            host='127.0.0.1',
            user='root',
            password=mysql_pwd,
            database=db_name,
            charset='utf8')

        cursor = db.cursor()
        try:
            cursor.execute("use canteen_management")
        except:
            print("Error: unable to use database!")
        sql = "SELECT * from consumer where name_consumer = '{}' and key_consumer='{}'".format(username, password)
        cursor.execute(sql)
        db.commit()
        res = cursor.fetchall()
        num = 0
        for row in res:
            num = num + 1
        # 如果存在且密码正确
        if num == 1:
            print("登录成功！欢迎用户！")
            msg = "done2"
        else:
            print("您没有用户权限或登录信息出错。")
            msg = "fail2"
        return render_template('consumer_Login.html', messages=msg, username=username, userRole=userRole)

# 用户主界面
@app.route('/MerchantIndex')
def Merchantindexpage():
    return render_template('MerchantIndex.html')

# 404跳转
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404

# 用户个人中心页面
@app.route('/MerchantPersonal')
def MpersonalPage():
    return render_template('MerchantPersonal.html')

# 修改用户个人信息页面
@app.route('/MerchantModifyPerInfo', methods=['GET', 'POST'])
def MerchantModifyPerInfo():
    msg = ""
    if request.method == 'GET':
        return render_template('MerchantModifyPerInfo.html', username=username)
    if request.method == 'POST':
        # username = request.form['username']
        address = request.form['address']
        phonenum = request.form['phonenum']


        # 连接数据库
        db = pymysql.connect(host='127.0.0.1', user='root', password=mysql_pwd, db=db_name, charset='utf8')
        cursor = db.cursor()
        try:
            cursor.execute("use canteen_management")
        except:
            print("Error: unable to use database!")

        sql = "Update consumer SET address_consumer = '{}', tele_consumer = '{}' where name_consumer = '{}'".format(address, phonenum,
                                                                                            username)
        try:
            cursor.execute(sql)
            db.commit()
            # print("修改个人信息成功")
            msg = "done"
        except ValueError as e:
            print("--->", e)
            print("修改个人信息失败")
            msg = "fail"
        return render_template('MerchantModifyPerInfo.html', messages=msg, username=username)


# 修改用户密码页面
@app.route('/MerchantModifyPwd', methods=['GET', 'POST'])
def MerModifyPassword():
    msg = ""
    if request.method == 'GET':
        return render_template('MerchantModifyPwd.html', username=username)
    if request.method == 'POST':
        psw1 = request.form['psw1']
        psw2 = request.form['psw2']
        # 两次输入密码是否相同
        if psw1 == psw2:
            # 连接数据库
            db = pymysql.connect(host='127.0.0.1', user='root', password=mysql_pwd, db=db_name, charset='utf8')
            cursor = db.cursor()
            try:
                cursor.execute("use canteen_management")
            except:
                print("Error: unable to use database!")
            sql = "Update consumer SET key_consumer = '{}' where name_consumer = '{}'".format(psw1, username)
            try:
                cursor.execute(sql)
                db.commit()
                # print("修改密码成功")
                msg = "done"
            except ValueError as e:
                print("--->", e)
                print("修改密码失败")
                msg = "fail"
            return render_template('MerchantModifyPwd.html', messages=msg, username=username)
        else:
            msg = "not equal"
            return render_template('MerchantModifyPwd.html', messages=msg, username=username)

# 用户点餐情况
@app.route('/MerchantMenu', methods=['GET', 'POST'])
def MerchantMenu():
    msg = ""
    if request.method == 'GET':
        msg = ""
        # 连接数据库
        db = pymysql.connect(host='127.0.0.1', user='root', password=mysql_pwd, db=db_name, charset='utf8')
        cursor = db.cursor()
        try:
            cursor.execute("use canteen_management")
        except:
            print("Error: unable to use database!")
        # 查询
        sql = "SELECT * FROM order_list"
        cursor.execute(sql)
        res = cursor.fetchall()
        if len(res) != 0:
            msg = "done"
            return render_template('MerchantMenu.html', username=username, result=res, messages=msg)
        else:
            print("NULL")
            msg = "none"
            return render_template('MerchantMenu.html', username=username, messages=msg)

# 用户点餐
@app.route('/MenuAdd', methods=['GET', 'POST'])
def MenuAdd():
    msg = ""
    print(request.method)
    if request.form["action"] == "立即点餐":
        return render_template('MenuAdd.html')
    if request.form["action"] == "订单状态查看":
        return redirect(url_for('MerMenuLook'))
    elif request.form["action"] == "确认下单":
        con_id = request.form.get('con_id')
        con_id = int(con_id)
        id_order = int((random.random()*9+1))*100000
        dishinfo = request.form.get('dishinfo')
        order_time =datetime.datetime.now()
        pickup_time = request.form.get('pickup_time')
        order_condition = 0 # 订单状态
        address = request.form.get('address')
        db = pymysql.connect(host='127.0.0.1', user='root', password=mysql_pwd, db=db_name, charset='utf8')

        cursor = db.cursor()
        try:
            cursor.execute("use canteen_management")
        except:
            print("Error: unable to use database!")

        sql = "SELECT * FROM order_list"
        cursor.execute(sql)
        u = cursor.fetchall()

        sql2 = "insert into order_list (id_business, id_order, id_consumer, type, order_time, pickup_time,order_condition,address_consumer) values ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}') ".format(
            con_id, id_order, 10001, dishinfo, order_time, pickup_time,order_condition,address)
        try:
            cursor.execute(sql2)
            db.commit()
            print("下单成功")
            msg = "done"
        except ValueError as e:
            print("--->", e)
            print("下单失败")
            msg = "fail"
        return render_template('MenuAdd.html', messages=msg, username=username, u=u)

# 用户查看订单信息
@app.route('/MerMenuLook', methods=['GET', 'POST'])
def MerMenuLook():
    msg = ""
    # 连接数据库
    db =  pymysql.connect(host='127.0.0.1', user='root', password=mysql_pwd, database=db_name,charset='utf8')
    cursor = db.cursor()
    try:
        cursor.execute("use canteen_management")
    except:
        print("Error: unable to use database!")
    sql = "SELECT * FROM order_list"
    print("sqlllll",sql)
    cursor.execute(sql)
    u = cursor.fetchall()
    db.close()
    return render_template('MerMenuLook.html', u=u)


# 用户查看菜品信息
@app.route('/ResCommentList', methods=['GET', 'POST'])
def ResCommentList():
    msg = ""
    # 连接数据库
    db =  pymysql.connect(host='127.0.0.1', user='root', password=mysql_pwd, database=db_name,charset='utf8')
    cursor = db.cursor()
    try:
        cursor.execute("use canteen_management")
    except:
        print("Error: unable to use database!")
    sql = "SELECT * FROM commodity"
    cursor.execute(sql)
    u = cursor.fetchall()
    db.close()
    return render_template('ResCommentList.html', u=u)


#用户查看座位信息
@app.route('/MerchantOrderPage', methods=['GET', 'POST'])
def MerchantOrderPage():
    msg = ""
    global notFinishedNum
    if request.method == 'GET':
        msg = ""
        # 连接数据库
        db = pymysql.connect(host='127.0.0.1', user='root', password=mysql_pwd, db=db_name, charset='utf8')
        cursor = db.cursor()
        try:
            cursor.execute("use canteen_management")
        except:
            print("Error: unable to use database!")
        sql = "SELECT * FROM ttable"
        cursor.execute(sql)
        u = cursor.fetchall()
        db.close()
        return render_template('MerchantOrderPage.html', u=u)

# 首页
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        submit5 = request.form.get('submit1')
        submit6 = request.form.get('submit2')
        submit7 = request.form.get('submit3')
        print('submit1: {}'.format(submit5))
        print('submit2: {}'.format(submit6))
        print('submit3: {}'.format(submit7))
        if submit5 is not None:
            return redirect(url_for('consumer_index'))
        if submit6 is not None:
            return redirect(url_for('business'))
        if submit7 is not None:
            return redirect(url_for('deliver'))
    return render_template('front_index.html')

if __name__ == '__main__':
    app.run(debug=True)
