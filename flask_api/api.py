from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse
from utils import makeprediction

from flask import render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField,  SubmitField

# App config.
DEBUG = True

app = Flask(__name__)

app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

#api = Api(app)



class ReusableForm(Form):
    slength = TextField('slength:', validators=[validators.required()])
    swidth = TextField('swidth:', validators=[validators.required()])
    plength = TextField('plength:', validators=[validators.required()])
    pwidth = TextField('pwidth:', validators=[validators.required()])

    
# class Prediction(Resource):
#     def get(self):

#         parser = reqparse.RequestParser()
#         parser.add_argument('slength', type=float, help='slength cannot be converted')
#         parser.add_argument('swidth', type=float, help='swidth cannot be converted')
#         parser.add_argument('plength', type=float, help='plength cannot be converted')
#         parser.add_argument('pwidth', type=float, help='pwidth cannot be converted')
#         args = parser.parse_args()

#         prediction = makeprediction.predict([
#                 args['slength'], 
#                 args['swidth'], 
#                 args['plength'], 
#                 args['pwidth']
#             ])

#         print "THE PREDICTION IS: " + str(prediction)

#         return {
#                 'slength': args['slength'],
#                 'swidth': args['swidth'],
#                 'plength': args['plength'],
#                 'pwidth': args['pwidth'],
#                 'species': prediction
#                }

@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)
        
    print form.errors
    if request.method == 'POST':
        slength=request.form['slength']
        swidth=request.form['swidth']
        plength=request.form['plength']
        pwidth=request.form['pwidth']
 
        if form.validate():
            prediction = makeprediction.predict([
                slength, 
                swidth, 
                plength, 
                pwidth
            ])
              
            # Save the comment here.
            flash('Prediction =  ' + prediction )
        else:
            flash('All the form fields are required. ')
 
    return render_template('hello.html', form=form)

    
#api.add_resource(Prediction, '/prediction')

if __name__ == '__main__':
    app.run(debug=True)
