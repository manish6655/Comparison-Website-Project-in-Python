
from flask import Flask, render_template, request, flash, session, redirect, Response
from flask_sqlalchemy import SQLAlchemy
import math
import json
import pandas as pd
import io
import xlwt

with open('configue.json', 'r') as data:
    params = json.load(data)["params"]


app = Flask(__name__)

app.secret_key = params['secret_key']

app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']

db = SQLAlchemy(app)


class Actual(db.Model):
    Sno = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(80), nullable=False)
    Component = db.Column(db.String(12), nullable=False)
    Company = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)


class Generic(db.Model):
    Sno = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(80), nullable=False)
    Component = db.Column(db.String(12), nullable=False)
    Company = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)


class Login(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(80), nullable=False)
    Password = db.Column(db.String(12), nullable=False)


class Ecommerce(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    link = db.Column(db.String(12), nullable=False)
    req = db.Column(db.String(12), nullable=False)
    by_which = db.Column(db.String(12), nullable=False)


class Itemsearch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    itemname = db.Column(db.String(80), nullable=False)
    path = db.Column(db.String(12), nullable=False)

class Contact(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(12), nullable=False)
    descc = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    email = db.Column(db.String(20), nullable=False)



def Sel_python(link, id, val, by_which):
    # try:
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.chrome.options import Options
    # chrome_options = Options()
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options=options, executable_path="C:\\ChromeDriver\\chromedriver.exe")
    
    # driver = webdriver.Chrome(
    #     executable_path="C:\\ChromeDriver\\chromedriver.exe")
    # driver.execute_script("document.body.style.zoom='zoom %'")
    driver.get(link)

    # browser = webdriver.Chrome()
    driver.set_window_size(2000, 2000)
    # chrome_options.add_experimental_option("detach", True)
    if(by_which == 'name'):
        search_bar = driver.find_element_by_name(id)
    elif(by_which == 'id'):
        search_bar = driver.find_element_by_id(id)
    elif(by_which == 'xpath'):
        search_bar = driver.find_element_by_xpath(id)
    elif(by_which == 'tagname'):
        search_bar = driver.find_element_by_tag_name(id)
    elif(by_which == 'linktext'):
        search_bar = driver.find_element_by_link_text(id)
    elif(by_which == 'classname'):
        search_bar = driver.find_elements_by_class_name(id)
    elif(by_which == 'cssselector'):
        search_bar = driver.find_elements_by_css_selector(id)
    else:
        pass

    # try:
    #     dis_button = driver.find_element_by_xpath("//button[text()='✕']")
    #     dis_button.click()
    # except:
    #     pass
    search_bar.clear()
    search_bar.send_keys(val)
    search_bar.send_keys(Keys.RETURN)
    
    # except:
    #     pass


@app.route("/")
def home():
    session.pop("itemname", None)
    session.pop("name", None)
    return render_template('index.html')


@app.route("/search", methods=['GET', 'POST'])
def search():
    session.pop("itemname", None)
    session.pop("name", None)
    if(request.method == 'POST'):
        search_val = str(request.form.get('search'))
        search_val = search_val.lower()
        item_result = Itemsearch.query.filter(
            Itemsearch.itemname.like(f'%%{search_val}%%')).first()
        print(item_result)
        if(not (str(item_result) == 'None')):
            return redirect(item_result.path)

    return render_template('index.html')


@app.route("/help")
def help():
    session.pop("itemname", None)
    session.pop("name", None)
    return render_template('help.html')


@app.route("/about")
def about():
    session.pop("itemname", None)
    session.pop("name", None)
    return render_template('about.html')


@app.route("/feedback",methods=['GET','POST'])
def feedback():
    if request.method == 'POST':
        firstname=request.form['firstname']
        lastname=request.form['lastname']
        return f"success {firstname} {lastname}"
    # session.pop("itemname", None)
    # session.pop("name", None)

    return render_template('feedback.html')



@app.route("/contact",methods = ['GET', 'POST'])
def contact():
    if(request.method=='POST'):
        import datetime
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        descc = request.form.get('message')
        entry = Contact(name=name, phone = phone, descc = descc, date= datetime.datetime.now(),email = email )
        db.session.add(entry)
        db.session.commit()
        # mail.send_message('New message from ' + name,
        #                   sender=email,
        #                   recipients = [params['gmail-user']],
        #                   body = descc + "\n" + phone
        #                   )
        flash('Thanks for giving your feedback')
    return render_template('contact.html', params="params",name="namee",name1="name1")


@app.route("/md_logout")
def md_logout():
    session.pop("md_login", None)
    return render_template('index.html')


@app.route("/md_dashboard", methods=['GET', 'POST'])
def md_dashboard():
    session.pop("itemname", None)
    session.pop("name", None)
    if (request.method == 'POST'):
        username = request.form.get('uname')
        password = request.form.get('pass')
        login_un = Login.query.filter(
            Login.Username.like(f'{username}%')).first()

        if(str(login_un) == 'None'):
            return render_template('md_login.html', msg="Invalid username or password")
        if(login_un.Password != password):
            return render_template('md_login.html', msg="Invalid username or password")

        session["md_login"] = request.form.get('uname')
        return redirect('/md_dashboard')
    if("md_login" in session):
        actual_medicines = Actual.query.filter_by().all()
        last = math.ceil(len(actual_medicines) / params['no_of_items'])
        page = request.args.get('page')
        if (not str(page).isnumeric()):
            page = 1
        page = int(page)
        nxtstatus = ''
        prvstatus = ''
        actual_medicines1 = actual_medicines[(page - 1) * params['no_of_items']: (
            page - 1) * params['no_of_items'] + params['no_of_items']]
        if (page == 1):
            prvstatus = 'disabled'
            prev = "#"
            if(page == last or last == 0):
                next = "#"
                nxtstatus = 'disabled'
            else:
                next = "/md_dashboard?page=" + str(page + 1)
        elif (page == last):
            prev = "/md_dashboard?page=" + str(page - 1)
            next = "#"
            nxtstatus = 'disabled'
        else:
            prev = "/md_dashboard?page=" + str(page - 1)
            next = "/md_dashboard?page=" + str(page + 1)
        return render_template('md_dashboard.html', no_of_medicine=len(actual_medicines), actual_medicines=actual_medicines1, username=session["md_login"], next=next, prev=prev, nxtstatus=nxtstatus, prvstatus=prvstatus)

    return render_template('md_login.html')


@app.route("/delete_medicine/<string:md_name>", methods=['GET', 'POST'])
def delete_medicine(md_name):
    session.pop("itemname", None)
    session.pop("name", None)
    if ('md_login' in session):
        medicine_dt = Generic.query.filter_by(Name=md_name).first()
        # Delete data from generic table corresponding to the actual
        db.session.delete(medicine_dt)
        db.session.commit()
        name = md_name.split("-")[0]
        return redirect(f'/view_generic/{name}')
    return render_template('md_login.html')


@app.route("/search_medicine", methods=['GET', 'POST'])
def search_medicine():
    session.pop("itemname", None)
    session.pop("name", None)
    if (request.method == 'POST'):
        session["search"] = request.form.get('search_md')
        return redirect('/search_medicine')
    if("search" in session):
        md_name = session["search"]
        actual_medicines = Actual.query.filter(
            Actual.Name.like(f'{md_name}%')).all()
        last = math.ceil(len(actual_medicines) / params['no_of_items'])
        page = request.args.get('page')
        if (not str(page).isnumeric()):
            page = 1
        page = int(page)
        prvstatus = ''
        nxtstatus = ''
        actual_medicines1 = actual_medicines[(page - 1) * params['no_of_items']: (
            page - 1) * params['no_of_items'] + params['no_of_items']]
        if (page == 1):
            prvstatus = 'disabled'
            prev = "#"
            if(page == last or last == 0):
                next = "#"
                nxtstatus = 'disabled'
            else:
                next = "/search_medicine?page=" + str(page + 1)
        elif (page == last):
            prev = "/search_medicine?page=" + str(page - 1)
            next = "#"
            nxtstatus = 'disabled'
        else:
            prev = "/search_medicine?page=" + str(page - 1)
            next = "/search_medicine?page=" + str(page + 1)
        if(len(actual_medicines) == 0):
            flash(f"There is No Medicine Available for {md_name}", 'danger')
        else:
            flash(
                f"We have {len(actual_medicines)} Medicines Available for {md_name} Medicine", 'success')
        return render_template('md_dashboard.html', actual_medicines=actual_medicines1, username=session["md_login"], next=next, prev=prev, nxtstatus=nxtstatus, prvstatus=prvstatus)

    return render_template('md_login.html')


# Logic For showing the selected Items of generic type for actual one
@app.route("/view_generic/<string:md_name>", methods=['GET', 'POST'])
def view_generic(md_name):
    session.pop("itemname", None)
    session.pop("name", None)
    if("md_login" in session):
        generic_medicines = Generic.query.filter(
            Generic.Name.like(f'{md_name}%')).all()
        last = math.ceil(len(generic_medicines) / params['no_of_items'])
        page = request.args.get('page')
        if (not str(page).isnumeric()):
            page = 1
        page = int(page)
        nxtstatus = ''
        prvstatus = ''
        generic_medicines1 = generic_medicines[(page - 1) * params['no_of_items']: (
            page - 1) * params['no_of_items'] + params['no_of_items']]
        if (page == 1):
            prvstatus = 'disabled'
            prev = "#"
            if(page == last or last == 0):
                next = "#"
                nxtstatus = 'disabled'
            else:
                next = f"/view_generic/{md_name}?page=" + str(page + 1)
        elif (page == last):
            prev = f"/view_generic/{md_name}?page=" + str(page - 1)
            next = "#"
            nxtstatus = 'disabled'
        else:
            prev = f"/view_generic/{md_name}?page=" + str(page - 1)
            next = f"/view_generic/{md_name}?page=" + str(page + 1)
        if(len(generic_medicines) == 0):
            flash(
                f"There is No Generic Medicine Available for {md_name}", 'danger')
        else:
            flash(
                f"We have {len(generic_medicines)} Medicines Available for {md_name} Medicine", 'success')
        return render_template('view_generic.html', generic_medicines=generic_medicines1, username=session["md_login"], next=next, prev=prev, nxtstatus=nxtstatus, prvstatus=prvstatus)

    return render_template('md_login.html')


# Will decide in future what to do
@app.route("/add_medicine/<string:name>", methods=['GET', 'POST'])
def add_medicine(name):
    session.pop("itemname", None)
    session.pop("name", None)
    pass
    # if ('md_login' in session):
    #     books = Book_data.query.filter_by(Name=sno).first()
    #

# import functionality for import / md dashboard- for admin only


@app.route("/import_generic/<string:name>", methods=['GET', 'POST'])
def import_generic(name):
    session.pop("itemname", None)
    session.pop("name", None)
    if("md_login" in session):
        if(request.method == 'POST'):
            # try:
            data1 = request.files['fileu']
            alldata = pd.read_excel(data1.read())
            Name1 = alldata['Medicine Name'].tolist()
            Component1 = alldata['Medicine Componant'].tolist()
            Company1 = alldata['Medicine Company'].tolist()
            for i in range(0, len(Name1)):
                add_m = Generic(Name=name+'-'+Name1[i], Component=Component1[i], Company=Company1[i])
                db.session.add(add_m)
            db.session.commit()
            return redirect('/md_dashboard')
            # except:
            #     return render_template('medicine_import.html', name=name)
        else:
            return render_template('medicine_import.html', name=name)
    else:
        return render_template('md_login.html')

 # export functionality for exporting / md dashboard- for Users


@app.route("/export_generic/<string:name>", methods=['GET', 'POST'])
def export_generic(name):
    session.pop("itemname", None)
    session.pop("name", None)
    generic_medicines = Generic.query.filter(
        Generic.Name.like(f'{name}%')).all()
    output = io.BytesIO()
    # create WorkBook object
    workbook = xlwt.Workbook()
    # bold = workbook.add_format({'bold': True})
    # add a sheet
    sh = workbook.add_sheet(f'{name} Medicines')
    # add headers
    sh.write(0, 0, 'Medicine Name')
    sh.write(0, 1, 'Medicine Componant')
    sh.write(0, 2, 'Medicine Company')
    i = 1
    for medicine in generic_medicines:
        sh.write(i, 0, str(medicine.Name).split('-')[1])
        sh.write(i, 1, medicine.Component)
        sh.write(i, 2, medicine.Company)
        i = i+1
    workbook.save(output)
    output.seek(0)
    return Response(output, mimetype="application/ms-excel", headers={"Content-Disposition": f"attachment;filename={name}_Generic_Medicines.xls"})


@app.route("/medicine", methods=['GET', 'POST'])
def Medicine():
    session.pop("itemname", None)
    medicine_name1 = ""
    if (request.method == 'POST'): 
        session["name"] = request.form.get('med')
        return redirect('/medicine')
        # session["id"]=0
    if("name" in session):
        medicine_name = session["name"]
        medicine_name1 = str(medicine_name).capitalize()
        generic_medicines = Generic.query.filter(
            Generic.Name.like(f'{medicine_name}-%')).all()
        # generic_medicines = Generic.query.filter_by(Name=medicine_name).all()
        # str(generic_medicines[0].Name).split('-')[1]
        last = math.ceil(len(generic_medicines) / params['no_of_items'])
        page = request.args.get('page')
        if (not str(page).isnumeric()):
            page = 1
        page = int(page)
        generic_medicines1 = generic_medicines[(page - 1) * params['no_of_items']: (
            page - 1) * params['no_of_items'] + params['no_of_items']]
        # if("id" in session):
        #     if session["id"]==0:
        #         session["id"]=1
        #     else:
        #         session["id"]=len(generic_medicines1)
        prvstatus = ''
        nxtstatus = ''
        if (page == 1):
            prvstatus = 'disabled'
            prev = "#"
            if(page == last or last == 0):
                next = "#"
                nxtstatus = 'disabled'
            else:
                next = "/medicine?page=" + str(page + 1)

        elif (page == last):
            prev = "/medicine?page=" + str(page - 1)
            next = "#"
            nxtstatus = 'disabled'
        else:
            prev = "/medicine?page=" + str(page - 1)
            next = "/medicine?page=" + str(page + 1)
        if(len(generic_medicines) == 0):
            flash(
                f"There is No Medicine Available for {medicine_name}", 'danger')
            exportStatus = 'disabled'
        else:
            flash(
                f"We have {len(generic_medicines)} Medicines Available for {medicine_name} Medicine", 'success')
            exportStatus = 'enabled'
        return render_template('Medicine.html', generic_medicines=generic_medicines1, medicine_name1=medicine_name1, next=next, prev=prev, prvstatus=prvstatus, nxtstatus=nxtstatus, exportStatus=exportStatus)
    return render_template('Medicine.html', medicine_name1=medicine_name1, prvstatus='disabled', nxtstatus='disabled', exportStatus='disabled')


@app.route("/e_commerce", methods=['GET', 'POST'])
def e_commerce():
    session.pop("name", None)
    itemname = "Items"
    if (request.method == 'POST'):
        session["itemname"] = request.form.get('med')
        return redirect('/e_commerce')
        # session["id"]=0
    if("itemname" in session):
        itemname = session["itemname"]
        allsite = Ecommerce.query.filter_by().all()
        last = math.ceil(len(allsite) / params['no_of_items'])
        page = request.args.get('page')
        if (not str(page).isnumeric()):
            page = 1
        page = int(page)
        allsite1 = allsite[(page - 1) * params['no_of_items']: (page - 1)
                           * params['no_of_items'] + params['no_of_items']]
        prvstatus = ''
        nxtstatus = ''
        if (page == 1):
            prvstatus = 'disabled'
            prev = "#"
            if(page == last or last == 0):
                next = "#"
                nxtstatus = 'disabled'
            else:
                next = "/e_commerce?page=" + str(page + 1)

        elif (page == last):
            prev = "/e_commerce?page=" + str(page - 1)
            next = "#"
            nxtstatus = 'disabled'
        else:
            prev = "/e_commerce?page=" + str(page - 1)
            next = "/e_commerce?page=" + str(page + 1)
        flash(f"Please find the best site for searching your results", 'success')
        return render_template('e_commerce.html', allsite=allsite1, itemname=itemname, next=next, prev=prev, nxtstatus=nxtstatus, prvstatus=prvstatus)
    return render_template('e_commerce.html', itemname=itemname, nxtstatus='disabled', prvstatus='disabled')


@app.route("/e_commerce/<string:name>", methods=['GET', 'POST'])
def e_commerce_search(name):
    session.pop("name", None)
    if("itemname" in session):
        itemval = Ecommerce.query.filter(
            Ecommerce.name.like(f'{name}%')).first()
        Sel_python(itemval.link, itemval.req,
                   session["itemname"], str(itemval.by_which))
        itemname = session["itemname"]
        allsite = Ecommerce.query.filter_by().all()
        last = math.ceil(len(allsite) / params['no_of_items'])
        page = request.args.get('page')
        if (not str(page).isnumeric()):
            page = 1
        page = int(page)
        allsite1 = allsite[(page - 1) * params['no_of_items']: (page - 1)
                           * params['no_of_items'] + params['no_of_items']]
        prvstatus = ''
        nxtstatus = ''
        if (page == 1):
            prvstatus = 'disabled'
            prev = "#"
            if(page == last or last == 0):
                next = "#"
                nxtstatus = 'disabled'
            else:
                next = "/e_commerce?page=" + str(page + 1)
        elif (page == last):
            prev = "/e_commerce?page=" + str(page - 1)
            next = "#"
            nxtstatus = 'disabled'
        else:
            prev = "/e_commerce?page=" + str(page - 1)
            next = "/e_commerce?page=" + str(page + 1)
        flash(f"Please find the best site for searching your results", 'success')
        return render_template('e_commerce.html', allsite=allsite1, itemname=itemname, next=next, prev=prev, nxtstatus=nxtstatus, prvstatus=prvstatus)
    return render_template('e_commerce.html', itemname=session["itemname"], nxtstatus='disabled', prvstatus='disabled')


if __name__ == "__main__":
    app.run(debug=True)
