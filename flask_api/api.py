from flask import Flask
from utils import makeprediction

from flask import render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField,  SubmitField

app = Flask(__name__)
app.debug = True
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class ReusableForm(Form):
    # All suits 
    suits1 = ['Hearts', 'Spades', 'Diamonds', 'Clubs']
    suits2 = ['Hearts', 'Spades', 'Diamonds', 'Clubs']
    suits3 = ['Hearts', 'Spades', 'Diamonds', 'Clubs']
    suits4 = ['Hearts', 'Spades', 'Diamonds', 'Clubs']
    suits5 = ['Hearts', 'Spades', 'Diamonds', 'Clubs']
    
    # Rank of card
    rank1 = ['Ace', '2','3','4','5','6','7','8','9','10','Jack','Queen','King']
    rank2 = ['Ace', '2','3','4','5','6','7','8','9','10','Jack','Queen','King']
    rank3 = ['Ace', '2','3','4','5','6','7','8','9','10','Jack','Queen','King']
    rank4 = ['Ace', '2','3','4','5','6','7','8','9','10','Jack','Queen','King']
    rank5 = ['Ace', '2','3','4','5','6','7','8','9','10','Jack','Queen','King']
def change_suit_to_number(option):
    if option =='Clubs':
        return 4
    elif option =='Hearts':
        return 1
    elif option == 'Spades':
        return 2
    else:
        return 3

def change_rank_to_number(option):
    if option =='Ace':
        return 1
    elif option =='Jack':
        return 11
    elif option =='Queen':
        return 12
    elif option =='King':
        return 13
    else:
        return int(option)


@app.route('/', methods=['GET','POST'])    
def dropdown():
    # All suits and ranks structure
    form = ReusableForm(request.form)
    # Define the default values
    if request.method == 'GET':
        save =  { 'suits1':'Clubs',
                  'rank1':'Ace',
                  'suits2':'Spades',
                  'rank2':'Ace',
                  'suits3':'Hearts',
                  'rank3':'Jack',
                  'suits4':'Diamonds',
                  'rank4':'Jack',
                  'suits5':'Spades',
                  'rank5':'Jack'}
    
    # Define what to do while sending with the button
    if request.method == 'POST':
        # Get the first card values
        s1=request.form.get('suits1')
        r1=request.form.get('rank1')
        # Get the other card values
        s2=request.form.get('suits2')
        r2=request.form.get('rank2')
        
        s3=request.form.get('suits3')
        r3=request.form.get('rank3')
        
        s4=request.form.get('suits4')
        r4=request.form.get('rank4')
        
        s5=request.form.get('suits5')
        r5=request.form.get('rank5')

        # Save the card states
        save =  { 'suits1':s1,
                  'rank1':r1,
                  'suits2':s2,
                  'rank2':r2,
                  'suits3':s3,
                  'rank3':r3,
                  'suits4':s4,
                  'rank4':r4,
                  'suits5':s5,
                  'rank5':r5}

        # Validate the entries
        if form.validate():
            # Perform the prediction
            prediction = makeprediction.predict([
                change_suit_to_number(s1), change_rank_to_number(r1), 
                change_suit_to_number(s2), change_rank_to_number(r2), 
                change_suit_to_number(s3), change_rank_to_number(r3),
                change_suit_to_number(s4), change_rank_to_number(r4),
                change_suit_to_number(s5), change_rank_to_number(r5)
            ])

            # Show the prediction
            flash('Prediction =  ' + prediction )
            
        else:
            flash('All the form fields are required. ')

    return render_template('test.html', form=form, save=save)

# Run the app add port=# if you want to run on a different port than 5000
if __name__ == "__main__":
    app.run()
