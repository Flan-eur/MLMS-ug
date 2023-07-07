import datetime
import random
import smtplib
from email.mime.text import MIMEText

import os
from email.mime import image
import smtplib
from email.mime.text import MIMEText
from flask_mail import Mail   #pip install flask-mail --user

from flask import Flask,render_template,request,redirect,session
from DBConnection import Db
app = Flask(__name__)
app.secret_key="key"

@app.route('/')
def home():
    return render_template('loginindex.html')

@app.route('/login')
def login():
    return render_template('loginindex.html')
@app.route('/logout')
def logout():
    session.clear
    session['lg']=""
    return render_template('loginindex.html')
@app.route('/login_value',methods=['post'])
def login_value():
    db=Db()
    username=request.form['uname']
    password=request.form['upwd']
    qry=db.selectOne("select * from login where username='"+username+"' and password='"+password+"'")
    if qry is not None:
        session['lg']='lin'
        if qry['Type']=="admin":
            return redirect('/mhome')
        elif qry['Type']=="agent":
            session['lid']=qry['Login_ID']
            return redirect('/ahome')
        elif qry['Type'] == "labour":
            session['lbid'] = qry['Login_ID']
            return redirect('/lhome')
        elif qry['Type'] == "customer":
            session['cid'] = qry['Login_ID']
            return redirect('/chome')
        elif qry['Type'] == "company":
            session['coid'] = qry['Login_ID']
            return redirect('/ichome')

        else:
            return '''<script>alert("invalid user");window.location="/"</script>'''
    else:
        return '''<script>alert("invalid user");window.location="/"</script>'''

@app.route('/magent')
def magent():
    if session['lg'] == 'lin':
        db=Db()
        qry=db.select("SELECT * FROM login,agentreg WHERE login.`Login_ID`=agentreg.`Login_id` AND `login`.`Type`='pending' ")
        return render_template('admin/mapproveagent.html',data=qry)
    else:
        return render_template('loginindex.html')
@app.route('/approve/<id>')
def approve(id):
    if session['lg'] == 'lin':
        db=Db()
        qry=db.update("update login set type='agent' where  Login_ID='"+id+"' ")
        return redirect('/magent')
    else:
        return render_template('loginindex.html')
@app.route('/reject/<id>')
def reject(id):
    if session['lg'] == 'lin':
      db=Db()
      qry=db.update("update login set type='reject' where  Login_ID='"+id+"' ")
      return redirect('/magent')
    else:
        return render_template('loginindex.html')

@app.route('/mapprovedagent')
def mapprovedagent():
    if session['lg'] == 'lin':
      db=Db()
      qry=db.select("SELECT * FROM login,agentreg WHERE login.`Login_ID`=agentreg.`Login_id` AND `login`.`Type`='agent' ")
      return render_template('admin/mapprovedagent.html',data=qry)
    else:
        return render_template('loginindex.html')

@app.route('/mstatus')
def mstatus():
    if session['lg'] == 'lin':
      db=Db()
      qry=db.select("SELECT * FROM agentreg,status WHERE agentreg.`Login_id`=status.Agent_Id")
      return render_template('admin/mstatus.html',data=qry)
    else:
        return render_template('loginindex.html')



@app.route('/mlabour')
def mlabour():
    if session['lg'] == 'lin':
       db = Db()
       qry = db.select("SELECT * FROM login,laboursreg WHERE login.`Login_ID`=laboursreg.`Login_Id` AND `login`.`Type`='pending' ")
       return render_template('admin/mapprovelabours.html', data=qry)
    else:
        return render_template('loginindex.html')


@app.route('/lapprove/<id>')
def lapprove(id):
    if session['lg'] == 'lin':
       db = Db()
       qry = db.update("update login set type='labour' where  Login_ID='" + id + "' ")
       return redirect('/mlabour')
    else:
        return render_template('loginindex.html')



@app.route('/lreject/<id>')
def lreject(id):
    if session['lg'] == 'lin':
      db = Db()
      qry = db.update("update login set type='reject' where  Login_ID='" + id + "' ")
      return redirect('/mlabour')
    else:
        return render_template('loginindex.html')


@app.route('/mapprovedlabour')
def mapprovedlabour():
    if session['lg'] == 'lin':
      db = Db()
      qry = db.select("SELECT * FROM login,laboursreg WHERE login.`Login_ID`=laboursreg.`Login_Id` AND `login`.`Type`='labour' ")
      return render_template('admin/mapprovedlabour.html', data=qry)
    else:
        return render_template('loginindex.html')


@app.route('/mcustomer',methods=['get'])
def mcustomer():
    if session['lg'] == 'lin':
      db = Db()
      qry = db.select( "SELECT * FROM login,customerreg WHERE login.`Login_ID`=customerreg.`Login_Id` AND `login`.`Type`='pending' ")
      return render_template('admin/mapprovecustomer.html',data=qry)
    else:
        return render_template('loginindex.html')

@app.route('/capprove/<id>')
def capprove(id):
    if session['lg'] == 'lin':
      db = Db()
      qry = db.update("update login set type='customer' where  Login_ID='" + id + "' ")
      return redirect('/mcustomer')
    else:
        return render_template('loginindex.html')


@app.route('/creject/<id>')
def creject(id):
    if session['lg'] == 'lin':
      db = Db()
      qry = db.update("update login set type='reject' where  Login_ID='" + id + "' ")
      return redirect('/mcustomer')
    else:
        return render_template('loginindex.html')

@app.route('/mapprovedcustomer')
def mapprovedcustomer():
    if session['lg'] == 'lin':
     db = Db()
     qry = db.select( "SELECT * FROM login,customerreg WHERE login.`Login_ID`=customerreg.`Login_Id` AND `login`.`Type`='customer' ")
     return render_template('admin/mapprovedcustomer.html',data=qry)
    else:
        return render_template('loginindex.html')


@app.route('/mcompany',methods=['get'])
def mcompany():
    if session['lg'] == 'lin':
      db = Db()
      qry = db.select("SELECT * FROM login,companyreg WHERE login.`Login_ID`=companyreg.`Login_Id` AND `login`.`Type`='pending' ")
      return render_template('admin/mapprovecompany.html',data=qry)
    else:
        return render_template('loginindex.html')


@app.route('/coapprove/<id>')
def coapprove(id):
    if session['lg'] == 'lin':
      db = Db()
      qry = db.update("update login set type='company' where  Login_ID='" + id + "' ")
      return redirect('/mcompany')
    else:
        return render_template('loginindex.html')


@app.route('/coreject/<id>')
def coreject(id):
    if session['lg'] == 'lin':
     db = Db()
     qry = db.update("update login set type='reject' where  Login_ID='" + id + "' ")
     return redirect('/mcompany')
    else:
        return render_template('loginindex.html')


@app.route('/mapprovedcompany')
def mapprovedcompany():
    if session['lg'] == 'lin':
     db = Db()
     qry = db.select("SELECT * FROM login,companyreg WHERE login.`Login_ID`=companyreg.`Login_Id` AND `login`.`Type`='company' ")
     return render_template('admin/mapprovedcompany.html',data=qry)
    else:
        return render_template('loginindex.html')


@app.route('/mnoti')
def mnoti():
    if session['lg'] == 'lin':
     return render_template('admin/madminnotif.html')
    else:
        return render_template('loginindex.html')


@app.route('/mnoti1',methods=['post'])
def mnoti1():
    if session['lg'] == 'lin':
     db=Db()
     n=request.form['textarea']
     qry=db.insert("insert into notification values('','"+n+"',curdate()) ")
     return '''<script>alert("Send successfully");window.location='/mnoti'</script>'''
    else:
        return render_template('loginindex.html')


@app.route('/mlfeed')
def mlfeed():
    if session['lg'] == 'lin':
      db=Db()
      qry=db.select("SELECT * FROM lfeedback,laboursreg WHERE `lfeedback`.`Labour_id`=`laboursreg`.`Login_Id`")
      return render_template('admin/madminlabourfeed.html',data=qry)
    else:
        return render_template('loginindex.html')


@app.route('/mcfeed')
def mcfeed():
    if session['lg'] == 'lin':
     db=Db()
     qry=db.select("SELECT * FROM cfeedback,customerreg WHERE `cfeedback`.`Customer_id`=`customerreg`.`Login_Id`")
     return render_template('admin/madmincustomerfeed.html',data=qry)
    else:
        return render_template('loginindex.html')


@app.route('/mhome')
def mhome():
    if session['lg']=='lin':
        return render_template('admin/MadminHome.html')
    else:
        return render_template('loginindex.html')
















# agent

@app.route('/signup')
def signup():
    return render_template('agent/agent_register.html')



@app.route('/agentreg',methods=['post'])
def agentreg():
    db=Db()
    name=request.form['textfield']
    place=request.form['textfield2']
    post=request.form['textfield3']
    pin=request.form['textfield4']
    Age = request.form['textfield5']
    DOB = request.form['textfield6']

    gender = request.form['radio']
    district=request.form['select']
    phn_no=request.form['textfield7']
    mailid = request.form['textfield8']
    agentlicence=request.form['textfield9']
    licenceimage=request.files['fileField']
    governmentid=request.form['textfield10']
    idno = request.form['textfield11']
    idimage = request.files['fileField2']
    psw=request.form['textfield12']
    password=request.form['password']
    ac=request.form['ac']
    ifsc=request.form['ifsc']
    import random
    blnc=random.randint(00000,99999)
    date=datetime.datetime.now().strftime("%d%m%y-%H%M%S")
    licenceimage.save("C:\\Users\\aswin\\PycharmProjects\\MIGRANT\\static\\mphoto\\"+date+".jpg")
    path="/static/mphoto/"+date+".jpg"
    idimage.save("C:\\Users\\aswin\\PycharmProjects\\MIGRANT\\static\\mphoto1\\" + date + ".jpg")
    path1 = "/static/mphoto1/" + date + ".jpg"
    if psw == password:
        qry=db.insert("insert into login values('','"+mailid+"','"+password+"','pending') ")
        qr=db.insert("insert into account values('','"+ac+"','"+ifsc+"','"+str(blnc)+"','"+str(qry)+"') ")
        qry1=db.insert("insert into agentreg values('"+str(qry)+"','"+name+"','"+place+"','"+post+"','"+pin+"','"+Age+"','"+DOB+"','"+gender+"','"+district+"','"+phn_no+"','"+mailid+"','"+agentlicence+"','"+str(path)+"','"+governmentid+"','"+idno+"','"+str(path1)+"')")
        return '''<script>alert("registered successfully");window.location="/"</script>'''
    else:
        return '''<script>alert("Password Mismatch");window.location="/signup"</script>'''
@app.route('/mapplication')
def mapplication():
    if session['lg'] == 'lin':
     db=Db()
     qry=db.select("SELECT * FROM `laboursreg`,`login`,`jobrequest` WHERE `laboursreg`.`Login_Id`=`login`.`Login_ID` AND `login`.`Type`='labour' AND `jobrequest`.`Status`='pending' AND `jobrequest`.`Labour_Id`=`laboursreg`.`Login_Id` and jobrequest.Agent_Id='"+str(session['lid'])+"' ")
     return render_template('agent/magentapprove.html',data=qry)
    else:
        return render_template('loginindex.html')
@app.route('/labapprove/<id>')
def labapprove(id):
    if session['lg'] == 'lin':
     db=Db()
     qry=db.update("update jobrequest set status='approved' where Labour_Id='"+id+"'")
     return redirect('/mapplication')
    else:
        return render_template('loginindex.html')
@app.route('/labreject/<id>')
def labreject(id):
    if session['lg'] == 'lin':
     db=Db()
     qry=db.update("update jobrequest set status='reject' where Labour_Id='"+id+"'")
     return redirect('/mapplication')
    else:
        return render_template('loginindex.html')
@app.route('/mapplication1')
def mapplication1():
    if session['lg'] == 'lin':
      db=Db()
      qry=db.select("SELECT * FROM `laboursreg`,`login`,`jobrequest` WHERE `laboursreg`.`Login_Id`=`login`.`Login_ID` AND `login`.`Type`='labour' AND `jobrequest`.`Status`='approved' AND `jobrequest`.`Labour_Id`=`laboursreg`.`Login_Id` and jobrequest.Agent_Id='"+str(session['lid'])+"' ")
      return render_template('agent/magentlabourapproved.html',data=qry)
    else:
        return render_template('loginindex.html')
@app.route('/custrqst')
def custrqst():
    if session['lg'] == 'lin':
     db=Db()
     qry=db.select("SELECT * FROM `customerreg`,`login`,`request` WHERE `customerreg`.`Login_Id`=`login`.`Login_ID` and `request`.`Customer_Id`=`customerreg`.`Login_Id`")
     return render_template('agent/magentrqst.html',data=qry)
    else:
        return render_template('loginindex.html')


@app.route('/custapprove/<id>')
def custapprove(id):
    if session['lg'] == 'lin':
     db=Db()
     qry=db.update("update request set status='approved' where Request_Id='"+id+"'")
     return redirect('/custrqst')
    else:
        return render_template('loginindex.html')


@app.route('/custreject/<id>')
def custreject(id):
    if session['lg'] == 'lin':
     db=Db()
     qry=db.update("update request set status='reject' where Request_Id='"+id+"'")
     return redirect('/custrqst')
    else:
        return render_template('loginindex.html')


@app.route('/workassign')
def workassign():
    if session['lg'] == 'lin':
      db=Db()
      qry=db.select("select * from laboursreg,jobrequest where `jobrequest`.`Labour_Id`=`laboursreg`.`Login_Id` AND jobrequest.Status='approved' and `jobrequest`.`Agent_Id`='"+str(session['lid'])+"'")
      return render_template("agent/massigns.html",data=qry)
    else:
        return render_template('loginindex.html')


@app.route('/workassign1/<id>')
def workassign1(id):
    if session['lg'] == 'lin':
      return render_template("agent/massignjob.html",lbid=id)
    else:
        return render_template('loginindex.html')


@app.route('/workassign2/<id>',methods=['post'])
def workassign2(id):
    if session['lg'] == 'lin':
     db=Db()
     wrk=request.form['textfield']
     wrkdays=request.form['textfield7']
     place=request.form['textfield2']
     wdate=request.form['textfield3']
     wtime=request.form['textfield4']
     lati=request.form['textfield5']
     longi=request.form['textfield6']
     qry=db.insert("insert into assignjob values (null,'"+str(session['lid'])+"','"+id+"','"+wrk+"','"+wrkdays+"','"+place+"','"+wdate+"','"+wtime+"','"+lati+"','"+longi+"')")
     return  '''<script>alert("assigned successfully");window.location="/workassign"</script>'''
    else:
        return render_template('loginindex.html')

@app.route('/aaccomadate')
def aaccomadate():
    if session['lg'] == 'lin':
     db=Db()
     qry=db.select("select * from laboursreg,jobrequest where `jobrequest`.`Labour_Id`=`laboursreg`.`Login_Id` and jobrequest.Status='approved' and `jobrequest`.`Agent_Id`='"+str(session['lid'])+"'")
     return render_template("agent/labouracco.html",data=qry)
    else:
        return render_template('loginindex.html')

@app.route('/aaccomadate1/<id>')
def aaccomadate1(id):
    if session['lg'] == 'lin':
      return render_template("agent/maccomodate.html",laid=id)
    else:
        return render_template('loginindex.html')


@app.route('/k/<id>',methods=['post'])
def k(id):
    if session['lg'] == 'lin':
     db=Db()
     place=request.form['textfield2']
     post = request.form['textfield3']
     pin = request.form['textfield4']
     latitude= request.form['textfield5']
     longitude = request.form['textfield6']
     qry=db.insert("insert into accommodation values (null,'"+str(session['lid'])+"','"+id+"','"+place+"','"+post+"','"+pin+"','"+latitude+"','"+longitude+"') ")
     return  '''<script>alert("assigned successfully");window.location="/aaccomadate"</script>'''
    else:
        return render_template('loginindex.html')

@app.route('/addsts1',methods=['post'])
def addsts1():
    db=Db()
    return render_template("agent/maddstasts.html")

@app.route('/addsts',methods=['post'])
def addsts():
    db=Db()
    sts=request.form['textfield']
    des=request.form['textarea']
    qry=db.insert("insert into Status values('','"+str(session['lid'])+"','"+sts+"','"+des+"',curdate())")
    return redirect('/vsts')
@app.route('/vsts')
def vsts():
    if session['lg'] == 'lin':
     db=Db()
     qry=db.select(" select * from status where Agent_Id='"+str(session['lid'])+"'")
     return render_template('agent/viewstatus.html',data=qry)
    else:
        return render_template('loginindex.html')


@app.route('/upsts/<id>')
def upsts(id):
    if session['lg'] == 'lin':
     db=Db()
     qry=db.selectOne("select * from status where Status_Id='"+id+"'")
     return render_template('agent/mupdatestatus.html',data=qry)
    else:
        return render_template('loginindex.html')


@app.route('/updsts/<id>',methods=['post'])
def updsts(id):
    if session['lg'] == 'lin':
      db=Db()
      sts=request.form['textfield']
      des=request.form['textarea']
      res=db.update("update status set Status='"+sts+"',Description='"+des+"',Date=curdate() where Status_Id='"+id+"'")
      return '''<script>alert("status updated successfully");window.location="/vsts"</script>'''
    else:
        return render_template('loginindex.html')


@app.route('/labsalary',methods=['post','get'])
def labsalary():
    if session['lg'] == 'lin':
      db=Db()
      res=db.select("select laboursreg.* from assignjob,agentreg,laboursreg where assignjob.Agent_Id=agentreg.Login_id and assignjob.Labour_Id=laboursreg.Login_Id and assignjob.Agent_Id='"+str(session['lid'])+"'")
      return render_template('agent/msalary.html',data=res)
    else:
        return render_template('loginindex.html')

@app.route('/labsalary_ajax/<lid>',methods=['post','get'])
def labsalary_ajax(lid):
    if session['lg'] == 'lin':
      db=Db()

      res=db.select("select * from assignjob where Labour_Id='"+lid+"' and year(Work_date)=year(CURRENT_DATE - INTERVAL 1 MONTH) and month(Work_date)=month(CURRENT_DATE - INTERVAL 1 MONTH)")
      return render_template('agent/ajax_works.html',data=res)
    else:
        return render_template('loginindex.html')


@app.route('/salarym',methods=['post'])
def salarym():
    if session['lg'] == 'lin':
     db=Db()
     amnt=request.form['textfield']
     lbid=request.form['select']
     qry=db.insert("insert into salary values(null,'"+str(session['lid'])+"','"+str(lbid)+"','"+str(amnt)+"',now())")
     return '''<script>alert("added successfully");window.location='/ahome'</script>'''
    else:
        return render_template('loginindex.html')


@app.route('/vlfeed')
def vlfeed():
    if session['lg'] == 'lin':
     db = Db()
     qry = db.select("SELECT * FROM lfeedback,laboursreg WHERE `lfeedback`.`Labour_id`=`laboursreg`.`Login_Id`")
     return render_template('agent/magentlabourfeed.html', data=qry)
    else:
        return render_template('loginindex.html')


@app.route('/vcfeed')
def vcfeed():
    if session['lg'] == 'lin':
     db = Db()
     qry = db.select("SELECT * FROM cfeedback,customerreg WHERE `cfeedback`.`Customer_id`=`customerreg`.`Login_Id`")
     return render_template('agent/magentcustfeed.html', data=qry)
    else:
        return render_template('loginindex.html')


@app.route('/vnoti')
def vnoti():
    if session['lg'] == 'lin':
     db=Db()
     qry=db.select("SELECT * FROM notification")
     return render_template('agent/magentviewnoti.html',data=qry)
    else:
        return render_template('loginindex.html')


@app.route('/vsp')
def vsp():
    if session['lg'] == 'lin':
      db=Db()
      qry=db.select("SELECT * FROM `companyreg`,login where companyreg.Login_Id=login.Login_ID and login.Type='company'")
      return render_template('agent/magentviewsp.html',dat=qry)
    else:
        return render_template('loginindex.html')


@app.route('/vsp1',methods=['post'])
def vsp1():
    if session['lg'] == 'lin':
     db=Db()
     cmp=request.form['s']
     qry=db.select("SELECT * FROM `companyreg`,`policy` WHERE `policy`.`Company_Id`=`companyreg`.`Login_Id` and `companyreg`.`Login_Id`='"+cmp+"'")
     return render_template('agent/magentviewsp.html',data=qry)
    else:
        return render_template('loginindex.html')


@app.route('/agent_sendpolicyrequest/<id>',methods=['post','get'])
def agent_sendpolicyrequest(id):
    if session['lg'] == 'lin':
      db=Db()
      res=db.select("SELECT * FROM `jobrequest`,`laboursreg` WHERE `jobrequest`.`Labour_Id`=`laboursreg`.`Login_Id` AND `jobrequest`.`Agent_Id`='"+str(session['lid'])+"' AND `jobrequest`.`Status`='approved'")
      return render_template('agent/agent_sendrequest.html',data=res,pid=id)
    else:
        return render_template('loginindex.html')


@app.route('/agentsend/<i>',methods=['post'])
def agentsend(i):
    if session['lg'] == 'lin':
      db=Db()
      lbid=request.form['select']
      lid=session['lid']
      qry=db.insert("insert into policy_request values(null,'"+str(i)+"','"+str(lbid)+"','"+str(lid)+"',curdate(), 'pending')")
      return '''<script>alert("send successfully");window.location="/ahome"</script>'''
    else:
        return render_template('loginindex.html')


@app.route('/ahome')
def ahome():
    if session['lg'] == 'lin':
      return render_template('agent/agenthome.html')
    else:
        return render_template('loginindex.html')

@app.route('/viewr')
def viewr():
    db=Db()
    qry=db.select("select *,DATE_ADD(`policy_request`.date,INTERVAL 365 DAY) AS tDateDiff,`policy`.*,`policy_request`.*,`laboursreg`.* from laboursreg,policy_request,policy where policy_request.labourid=laboursreg.Login_Id and policy_request.policyid=policy.policyid")
    return render_template('agent/viewrenewal.html',data=qry)

@app.route('/apayment/<id>/<amt>')
def apayment(id,amt):
    if session['lg'] == 'lin':
     db=Db()
     res=db.selectOne("select account.* from account,policy where policyid='"+id+"' and Company_Id=account.user_id")
     if res is not None:
        return render_template('agent/send_payment.html',acc=res['account_no'],ifsc=res['ifsc_code'],amount=amt)
     else:

         return render_template('agent/send_payment.html', acc="", ifsc="", amount=amt)
    else:
        return render_template('loginindex.html')


@app.route('/apayment1',methods=['post'])
def apayment1():
    if session['lg'] == 'lin':
     ac=request.form['textfield7']
     ifsc=request.form['textfield8']
     amt=request.form['textfield9']
     lid = session['lid']
     db=Db()
     q=db.selectOne("select * from account where user_id='"+str(lid)+"'")
     blnc=q['balance']
     if float(blnc) > float(amt):
        q1=db.selectOne("select * from account where account_no='"+ac+"' and ifsc_code='"+ifsc+"'")
        cblnc=q1['balance']
        cid=q1['user_id']
        b=float(blnc)-float(amt)
        b1=float(cblnc)+float(amt)

        q2=db.update("update account set balance='"+str(b)+"' where user_id='"+str(lid)+"'")
        q3=db.update("update account set balance='"+str(b1)+"' where account_no='"+ac+"' ")
        q4=db.insert("insert into apayment values('','"+str(lid)+"','"+str(cid)+"','"+str(amt)+"',curdate())")
        return '''<script>alert("Payment completed");window.location="/ahome"</script>'''
     else:
        return '''<script>alert("insufficient balance");window.location="/ahome"</script>'''
    else:
        return render_template('loginindex.html')







#labours



@app.route('/lsignup')
def lsignup():
    return render_template('labours/labour_register.html')


@app.route('/labourreg',methods=['post'])
def labourreg():
    db = Db()
    name = request.form['textfield']
    place = request.form['textfield2']
    post = request.form['textfield3']
    pin = request.form['textfield4']
    Age = request.form['textfield5']
    DOB = request.form['textfield6']
    gender = request.form['radio']
    state = request.form['select']
    district = request.form['select2']
    phn_no = request.form['textfield7']
    mailid = request.form['textfield8']
    govid = request.form['select3']
    idno = request.form['textfield9']
    idimage = request.files['fileField']
    psw = request.form['textfield12']
    password = request.form['password']
    date = datetime.datetime.now().strftime("%d%m%y-%H%M%S")
    idimage.save("C:\\Users\\aswin\\PycharmProjects\\MIGRANT\\static\\mphoto\\" + date + ".jpg")
    path1 = "/static/mphoto/" + date + ".jpg"
    if psw == password:
        qry = db.insert("insert into login values('','" + mailid + "','" + password + "','pending') ")
        qry1 = db.insert("insert into laboursreg values('" + str( qry) + "','" + name + "','" + place + "','" + post + "','" + pin + "','" + Age + "','" + DOB + "','" + gender + "','"+state+"','" + district + "','" + phn_no + "','" + mailid + "','" + govid + "','" + idno + "','" + str(path1) + "')")
        return '''<script>alert("registered successfully");window.location="/"</script>'''
    else:
        return '''<script>alert("Password Mismatch");window.location="/signup"</script>'''


@app.route('/search')
def search():
    if session['lg'] == 'lin':
     db=Db()
     return render_template('labours/mlabourrqst.html')
    else:
        return render_template('loginindex.html')



@app.route('/vsend',methods=['post'])
def vsend():
    if session['lg'] == 'lin':
     db=Db()
     dist=request.form['s']
     qry=db.select("SELECT * FROM `agentreg`,`status`,login WHERE `status`.`Agent_Id`=`agentreg`.`Login_id` and agentreg.Login_id=login.Login_ID and login.Type='agent' and agentreg.District='"+dist+"'")
     return render_template('labours/mlabourrqst.html',data=qry)
    else:
        return render_template('loginindex.html')

@app.route('/sendrqst/<a>')
def sendrqst(a):
    if session['lg'] == 'lin':
     db=Db()
     qry=db.selectOne("SELECT * FROM `laboursreg` WHERE `Login_Id`='"+str(session['lbid'])+"' ")
     return render_template('labours/mlabourapplication.html',data=qry,q=a)
    else:
        return render_template('loginindex.html')

@app.route('/sendrqst1/<a>',methods=['post'])
def sendrqst1(a):
    if session['lg'] == 'lin':
     db=Db()
     cv=request.files['fileField']
     phto=request.files['fileField2']
     date = datetime.datetime.now().strftime("%d%m%y-%H%M%S")
     cv.save("C:\\Users\\aswin\\PycharmProjects\\MIGRANT\\static\\mphoto\\" + date + ".jpg")
     path= "/static/mphoto/" + date + ".jpg"
     date1 = datetime.datetime.now().strftime("%d%m%y-%H%M%S")
     phto.save("C:\\Users\\aswin\\PycharmProjects\\MIGRANT\\static\\mphoto1\\" + date1 + ".jpg")
     path1 = "/static/mphoto1/" + date1 + ".jpg"

     qry=db.insert("insert into jobrequest values(null,'"+str(a)+"','"+str(session['lbid'])+"','pending',curdate(),'"+str(path)+"','"+str(path1)+"')")
     return  '''<script>alert("send successfully");window.location="/search"</script>'''
    else:
        return render_template('loginindex.html')


@app.route('/vstatus')
def vstatus():
    if session['lg'] == 'lin':
     db=Db()
     qry=db.select("SELECT * from `agentreg`,`jobrequest` WHERE `agentreg`.`Login_id`=`jobrequest`.`Agent_Id` AND `jobrequest`.`Labour_Id`='"+str(session['lbid'])+"'")

     return render_template('labours/mviewstatus.html',data=qry)
    else:
        return render_template('loginindex.html')


@app.route('/vwork')
def vwork():
    if session['lg'] == 'lin':
     db=Db()
     qry=db.select("SELECT * FROM `assignjob` WHERE `Labour_Id`='"+str(session['lbid'])+"'")
     return render_template('labours/mlabourwork.html',data=qry)
    else:
        return render_template('loginindex.html')


@app.route('/vaccom')
def vaccom():
    if session['lg'] == 'lin':
     db=Db()
     qry=db.select("SELECT * FROM `accommodation` WHERE `Labour_Id`='"+str(session['lbid'])+"'")
     return render_template('labours/mlabouracco.html',data=qry)
    else:
        return render_template('loginindex.html')

@app.route('/vsalary')
def vsalary():
    if session['lg'] == 'lin':
     db=Db()
     qry=db.select("SELECT * FROM `salary` WHERE `Labours_Id`='"+str(session['lbid'])+"'")
     return render_template('labours/mlaboursalary.html',data=qry)
    else:
        return render_template('loginindex.html')


@app.route('/afeed')
def afeed():
    if session['lg'] == 'lin':
     return render_template('labours/mfeedback.html')
    else:
        return render_template('loginindex.html')

@app.route('/afeed1',methods=['post'])
def afeed1():
    if session['lg'] == 'lin':
     db=Db()
     feed=request.form['textarea']
     qry=db.insert("insert into `lfeedback` values ('','"+str(session['lbid'])+"','"+feed+"',curdate())")
     return  '''<script>alert("send successfully");window.location="/afeed"</script>'''
    else:
        return render_template('loginindex.html')


@app.route('/lhome')
def lhome():
    if session['lg'] == 'lin':
     return render_template('labours/labourhome.html')
    else:
        return render_template('loginindex.html')














#customer

@app.route('/chome')
def chome():
    if session['lg'] == 'lin':
     return render_template('customer/customerhome.html')
    else:
        return render_template('loginindex.html')


@app.route('/csignup')
def csignup():
    return render_template('customer/customer_register.html')

@app.route('/customerreg',methods=['post'])
def customerreg():
    db=Db()
    name = request.form['textfield']
    place = request.form['textfield2']
    post = request.form['textfield3']
    pin = request.form['textfield4']
    Age = request.form['textfield5']
    DOB = request.form['textfield6']
    gender = request.form['radio']
    # district = request.form['select']
    phn_no = request.form['textfield7']
    mailid = request.form['textfield8']
    idproof = request.form['select']
    idno = request.form['textfield10']
    idimage = request.files['fileField']
    psw = request.form['textfield11']
    password = request.form['password']
    date = datetime.datetime.now().strftime("%d%m%y-%H%M%S")
    idimage.save("C:\\Users\\aswin\\PycharmProjects\\MIGRANT\\static\\mphoto\\" + date + ".jpg")
    path1 = "/static/mphoto/" + date + ".jpg"
    if psw == password:
        qry = db.insert("insert into login values('','" + mailid + "','" + password + "','pending') ")
        qry1 = db.insert("insert into customerreg values('" + str(qry) + "','" + name + "','" + place + "','" + post + "','" + pin + "','" + Age + "','" + DOB + "','" + gender + "','" + phn_no + "','" + mailid + "','" + idproof + "','" + idno + "','" + str( path1) + "')")
        return '''<script>alert("registered successfully");window.location="/"</script>'''
    else:
        return '''<script>alert("Password Mismatch");window.location="/signup"</script>'''


@app.route('/clarqst')
def clarqst():
    if session['lg'] == 'lin':
     db=Db()
     return render_template("customer/mcalrqst.html")
    else:
        return render_template('loginindex.html')


@app.route('/search_agents',methods=['post'])
def search_agents():
    if session['lg'] == 'lin':
     db=Db()
     dis=request.form['k']
     qry=db.select("select * from agentreg,login where agentreg.Login_id=login.Login_ID and login.Type='agent'and agentreg.District='"+dis+"'")
     return render_template("customer/mcalrqst.html",data=qry)
    else:
        return render_template('loginindex.html')





@app.route('/clarqst2/<aid>')
def clarqst2(aid):
    if session['lg'] == 'lin':
     return render_template("customer/mcustomerapplication.html",aid=aid)
    else:
        return render_template('loginindex.html')


@app.route('/clarqst1/<aid>',methods=['post'])
def clarqst1(aid):
    if session['lg'] == 'lin':
     db=Db()
     wdetails=request.form['textarea']
     lno=request.form['textfield7']
     wdays=request.form['textfield8']
     phead=request.form['textfield9']
     qry=db.insert("insert into  `request` VALUES('','"+str(session['cid'])+"','"+str(aid)+"','"+wdetails+"','"+lno+"','pending',now(),'"+wdays+"','"+phead+"')")
     return '''<script>alert("Request sended Successfully");window.location="/clarqst"</script>'''
    else:
        return render_template('loginindex.html')






@app.route('/vsrqst')
def vsrqst():
    if session['lg'] == 'lin':
     db=Db()
     qry = db.select("SELECT * from `request` where `request`.`Customer_Id`='"+str(session['cid'])+"'")
     return render_template('customer/mcviewrqst.html',data=qry)
    else:
        return render_template('loginindex.html')



@app.route('/request_payment/<id>')
def request_payment(id):
    if session['lg'] == 'lin':
     db=Db()
     qry=db.selectOne("select * from request where request_id='"+str(id)+"'")
     q=db.selectOne("select * from account where user_id='"+str(qry['Agent_Id'])+"'")
     ac=q['account_no']
     ifsc=q['ifsc_code']
     amount=int(qry['Needed_labours'])*int(qry['work_days'])*int(qry['per_head'])
     return render_template("customer/send_payment.html",data=id,amount=amount,ac=ac,ifsc=ifsc)
    else:
        return render_template('loginindex.html')


@app.route('/request_payment_post/<id>',methods=['post'])
def request_payment_post(id):
    if session['lg'] == 'lin':
     db=Db()
     acno = request.form['textfield7']
     ifc = request.form['textfield8']
     amount = request.form['textfield9']
     qry1=db.selectOne("select * from account where account_no='"+acno+"' and ifsc_code='"+ifc+"'")
     qry2 = db.selectOne("select * from account where account_id='2'")
     if qry2 is not None:
        sbalance = qry2['balance']
        if qry1 is not None:
            balance=qry1['balance']

            if float(balance)>=float(amount):
                cbalance=float(balance)-float(amount)
                scbalance=float(sbalance)+float(amount)
                qry = db.insert("insert into  payment VALUES('','" + str(id) + "','','" + str(amount) + "',now())")
                db.update("update account set balance='"+str(cbalance)+"' where account_no='"+acno+"'")
                db.update("update account set balance='"+str(scbalance)+"' where account_id='2'")
                return '''<script>alert("Updated Successfully");window.location="/vsrqst"</script>'''
            else:
                return '''<script>alert("Insufficent balance");window.location="/vsrqst"</script>'''
        else:
            return '''<script>alert("Account Number or IFSC code is incorrect");window.location="/vsrqst"</script>'''

     else:
        return '''<script>alert("Invalid Account");window.location="/vsrqst"</script>'''
    else:
        return render_template('loginindex.html')






@app.route('/custfeed')
def custfeed():
    if session['lg'] == 'lin':

        return render_template('customer/custfeedback.html')
    else:
        return render_template('loginindex.html')

@app.route('/custfeed1', methods=['post'])
def custfeed1():
    if session['lg'] == 'lin':
        db = Db()
        feed = request.form['textarea']
        qry = db.insert("insert into `cfeedback` values ('','" + str(session['cid']) + "','" + feed + "',curdate())")
        return '''<script>alert("send successfully");window.location="/custfeed"</script>'''
    else:
        return render_template('loginindex.html')





#insurancecmpny



@app.route('/ichome')
def ichome():
    if session['lg'] == 'lin':
     return render_template('insurance/insurancehome.html')
    else:
        return render_template('loginindex.html')


@app.route('/icsignup')
def icsignup():
    return render_template('insurance/company_register.html')

@app.route('/companyreg',methods=['post'])
def companyreg():
    db=Db()
    name = request.form['textfield']
    place = request.form['textfield2']
    post = request.form['textfield3']
    pin = request.form['textfield4']
    district = request.form['select']
    phn_no = request.form['textfield5']
    mailid = request.form['textfield6']
    licno = request.form['textfield7']
    licimage = request.files['fileField']
    psw = request.form['textfield8']
    password = request.form['password']
    acc=request.form['ac']
    ifsc=request.form['ifsc']
    balance=random.randint(00000,99999)
    date = datetime.datetime.now().strftime("%d%m%y-%H%M%S")
    licimage.save("C:\\Users\\aswin\\PycharmProjects\\MIGRANT\\static\\mphoto\\" + date + ".jpg")
    path1 = "/static/mphoto/" + date + ".jpg"
    if psw == password:
        qry = db.insert("insert into login values('','" + mailid + "','" + password + "','pending') ")
        qry1 = db.insert("insert into companyreg values('" + str(qry) + "','" + name + "','" + place + "','" + post + "','" + pin + "','" + district + "','" + phn_no + "','" + mailid + "','"  + licno+ "','" + str( path1) + "')")
        qry2=db.insert("insert into account values ('','"+acc+"','"+ifsc+"','"+str(balance)+"','"+str(qry)+"')")
        return '''<script>alert("registered successfully");window.location="/"</script>'''
    else:
        return '''<script>alert("Password Mismatch");window.location="/signup"</script>'''
@app.route('/mpolicy')
def mpolicy():
    if session['lg'] == 'lin':
     return render_template('insurance/mcompanyscheme.html')
    else:
        return render_template('loginindex.html')

@app.route('/mpolicy1',methods=['post'])
def mpolicy1():
    if session['lg'] == 'lin':
     db=Db()
     pname=request.form['textfield4']
     pdetais=request.form['textarea2']
     amount=request.form['textfield5']
     dura=request.form['textfield6']
     qry=db.insert("insert into policy values('','"+str(session['coid'])+"','"+pname+"','"+pdetais+"','"+amount+"','"+dura+"')")
     return '''<script>alert("added successfully");window.location="/mpolicy"</script>'''
    else:
        return render_template('loginindex.html')


@app.route('/rview')
def rview():
    if session['lg'] == 'lin':
     db=Db()
     qry=db.select("SELECT * FROM `policy`,`policy_request`,`laboursreg`,`agentreg` WHERE policy_request.`Agent_Id`=`agentreg`.`Login_id` AND `policy_request`.`labourid`=`laboursreg`.`Login_Id` AND `policy_request`.`policyid`=`policy`.`policyid` AND `status`='pending' ")
     return render_template('insurance/viewpolicy.html',data=qry)
    else:
        return render_template('loginindex.html')


@app.route('/papprove/<id>')
def papprove(id):
    if session['lg'] == 'lin':
     db=Db()
     qry=db.update("UPDATE `policy_request` SET  `status`='approved',date=curdate() WHERE `p_req_id`='"+id+"' and status='pending'")
     return '''<script>alert("approved ");window.location="/rview"</script>'''
    else:
        return render_template('loginindex.html')



@app.route('/preject/<id>')
def preject(id):
    if session['lg'] == 'lin':
     db=Db()
     qry=db.update("UPDATE `policy_request` SET  `status`='rejected' WHERE `p_req_id`='"+id+"' and status='pending'")
     return '''<script>alert("rejected");window.location="/rview"</script>'''
    else:
        return render_template('loginindex.html')



@app.route('/vpolicy')
def vpolicy():
    if session['lg'] == 'lin':
     db=Db()
     qry=db.select("SELECT *,DATE_ADD(`policy_request`.date,INTERVAL 365 DAY) AS tDateDiff,`policy`.*,`policy_request`.*,`laboursreg`.*,`agentreg`.*  FROM `policy`,`policy_request`,`laboursreg`,`agentreg` WHERE policy_request.`Agent_Id`=`agentreg`.`Login_id` AND `policy_request`.`labourid`=`laboursreg`.`Login_Id` AND `policy_request`.`policyid`=`policy`.`policyid` AND `policy`.`Company_Id`='"+str(session['coid'])+"'")
     print(qry)
     return render_template('insurance/viewandrenewal.html',data=qry)
    else:
        return render_template('loginindex.html')

@app.route('/vrenewal/<a>')
def vrenewal(a):
    db=Db()
    qry=db.selectOne("SELECT *,DATE_ADD(`policy_request`.date,INTERVAL 365 DAY) AS tDateDiff,`policy`.*,`policy_request`.*,`laboursreg`.*,`agentreg`.*,agentreg.Email as aemail  FROM `policy`,`policy_request`,`laboursreg`,`agentreg` WHERE policy_request.`Agent_Id`=`agentreg`.`Login_id` AND `policy_request`.`labourid`=`laboursreg`.`Login_Id` AND `policy_request`.`policyid`=`policy`.`policyid` AND `policy`.`Company_Id`='"+str(session['coid'])+"' AND policy_request.p_req_id='"+a+"' AND policy_request.status='approved' ")


    if qry is not None:
        email=qry['aemail']
        emname=qry['Labour_name']
        try:
            gmail = smtplib.SMTP('smtp.gmail.com', 587)

            gmail.ehlo()

            gmail.starttls()

            gmail.login('cksruthi@gmail.com', 'Cks45678')  # mail that send password

        except Exception as e:
             print("Couldn't setup email!!" + str(e))

        msg = MIMEText(  emname+ "Need to renew his/her policy")  # content

        msg['Subject'] = 'Policy Renewal'


        msg['To'] = email
        msg['From'] = 'cksruthi@gmail.com'

        try:

           gmail.send_message(msg)

        except Exception as e:

         print("COULDN'T SEND EMAIL", str(e))
        return  '''<script>alert("Email send");window.location="/vpolicy"</script>'''
    else:
        return '''<script>alert("Not Available");window.location="/vpolicy"</script>'''

# @app.route('/renewal')
# def renewal():
#     db=Db()
#     return render_template('insurance/')
#



@app.route('/ipayment')
def ipayment():
    if session['lg'] == 'lin':
     db=Db()
     qry=db.select("SELECT *,DATE_ADD(`policy_request`.date,INTERVAL 365 DAY) AS tDateDiff,`policy`.*,`policy_request`.*,`laboursreg`.*,`agentreg`.*,apayment.*  FROM `policy`,`policy_request`,`laboursreg`,`agentreg`,apayment WHERE policy_request.`Agent_Id`=`agentreg`.`Login_id` AND `policy_request`.`labourid`=`laboursreg`.`Login_Id` AND `policy_request`.`policyid`=`policy`.`policyid` AND `apayment`.agentid=`policy_request`.Agent_Id AND `policy`.`Company_Id`='"+str(session['coid'])+"'")
     return render_template('insurance/vpayment.html',data=qry)
    else:
        return render_template('loginindex.html')

@app.route('/common')
def common():
    return render_template('commonsignup.html')


# ///////////////////////////////////////////////////////////////////////

@app.route('/forgot_password')
def forgot_password():
    return render_template("forgot_password.html")

@app.route('/forgot_pwd_post', methods=['POST'])
def forgot_pwd_post():
    email = request.form["uname"]
    db = Db()
    q = db.selectOne("select * from login where username='" + email + "'")
    if q is not None:
        password =q['password']
        try:
            gmail = smtplib.SMTP('smtp.gmail.com', 587)

            gmail.ehlo()

            gmail.starttls()

            gmail.login('cksruthi123@gmail.com', 'Cks45678')  # mail that send password

        except Exception as e:
            print("Couldn't setup email!!" + str(e))

        msg = MIMEText("Your password is " + str(password))  # content

        msg['Subject'] = 'Verification'

        msg['To'] = email

        msg['From'] = 'cksruthi123@gmail.com'

        try:

            gmail.send_message(msg)

        except Exception as e:

            print("COULDN'T SEND EMAIL", str(e))
        return '<script>alert("Mail sended successfully ");window.location="/"</script>'

    else:
        return '<script>alert("invalid user");window.location="/"</script>'




if __name__ == '__main__':
    app.run()
