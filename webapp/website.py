from flask import Flask, render_template, redirect, url_for
from forms import GradeForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "dev"

#app.config['SQLALCHEMY_DATABASE_URI']

grades_list = [{
    'class_name': 'Python 101',
    'current_grade': 0,
    'desired_grade': 34,
    'final_weight': 10,
    'needed_grade': 95,
}]

@app.route('/', methods=("GET", "POST"))
def home():
    form = GradeForm()
    if form.validate_on_submit():
        grades_list.append({'class_name': form.class_name.data,
                            'current_grade': form.current_grade.data,
                            'desired_grade': form.desired_grade.data,
                            'final_weight': form.final_weight.data,
                            'needed_grade': form.current_grade.data * (form.final_weight) / form.desired_grade.data
                            })
        return redirect(url_for('grades'))
                        
    return render_template('home.html', form = form)

@app.route('/grades/')
def grades():
    return render_template('grade.html', grades_list=grades_list)

if __name__ == '__main__':
    app.run(debug=True)