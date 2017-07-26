from flask import Flask, render_template, flash, request, send_file
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import os
import thread
 
# App config.
DEBUG = True
app = Flask(__name__,template_folder='./')
# app.config.from_object(__name__,template_folder='./')
# app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
 
class ReusableForm(Form):
    from_edge = TextField('From edge id:\t', validators=[validators.required()])
    to_edge = TextField('To edge id:\t', validators=[validators.required()])
 
@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)
    print form.errors
    if request.method == 'POST':
        if request.form['btn'] == 'Randomise traffic':
            os.system("python /home/ubuntu/Desktop/trajectory_clone/Vis/net_to_json.py")
            flash("Done !")
            return render_template('front.html', form=form)

        from_edge=request.form['from_edge'].strip()
        to_edge=request.form['to_edge'].strip()
        print from_edge
        if from_edge=="" or to_edge=="":
            flash("Edge ids cannot be blank !")
            return render_template('front.html', form=form)

        table_gen=open("Vis/table_input","w")
        table_gen.write("0")
        table_gen.close()

        path_gen=open("Vis/path_input","w")
        path_gen.write(from_edge+"\n")
        path_gen.write(to_edge+"\n")
        path_gen.close()
        flash("Please wait...")
 
        os.system("python /home/ubuntu/Desktop/trajectory_clone/Vis/table_gen.py < /home/ubuntu/Desktop/trajectory_clone/Vis/table_input")
        try:
            os.system("python /home/ubuntu/Desktop/trajectory_clone/Vis/path_predict.py < /home/ubuntu/Desktop/trajectory_clone/Vis/path_input")
            return send_file("/home/ubuntu/Desktop/trajectory_clone/Vis/out_path", attachment_filename='path.txt')
        except:
            flash("Path not found!")

        # if form.validate():
        #     # Save the comment here.
        #     flash('Hello ' + name)
        # else:
        #     flash('All the form fields are required. ')
 
    return render_template('front.html', form=form)

@app.route('/return-files/')
def return_files_tut():
    try:
        return send_file('/home/ubuntu/Desktop/trajectory_clone/Vis/out.json', attachment_filename='JSON_output.json')
    except Exception as e:
        return str(e)

@app.route('/traffic_gen/')
def traffic_new():
    flash("Please wait...")
    os.system("python /home/ubuntu/Desktop/trajectory_clone/Vis/net_to_json.py")
    flash("Done!")
 
if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.debug = True
    app.run(host= '0.0.0.0', port=80)