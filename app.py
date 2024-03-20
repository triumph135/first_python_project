# print("Hello, world. This is Python!")

# name = input ("What is your name?") 
# print ("Hello, " + name)


# name = input ("What is your name?")
# age = input ("How old are you?")
# gender = input.upper ("Are you a male or female?")
# marital_status = input ("Are you married?")  

# if gender == "MALE":
#   print ("Hello, Mr. " + name)  
# elif gender == "FEMALE":
#   if marital_status == "yes":
#     print ("Hello, Mrs. " + name)
#   else : 
#     print ("Hello, Ms. " + name)
    



from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Product Manager',
    'company': 'Cargas Systems Inc.',
    'location': 'Lancaster, PA',
    'date': 'Feb 2022 - Present'
  },
  {
    'id': 2,
    'title': 'Systems Consultant',
    'company': 'Cargas Systems Inc.',
    'location': 'Lancaster, PA',
    'date': 'Jun 2019 - Feb 2022'
  },
  {
    'id': 3,
    'title': 'Enterprise Support Consultant',
    'company': 'Cargas Systems Inc.',
    'location': 'Lancaster, PA',
    'date': 'Jan 2018 - Jun 2019'
  },
  {
    'id': 4,
    'title': 'Senior Financial Management Analyst',
    'company': 'US Army Reserve and PA National Guard',
    'location': 'Owings Mills, MD',
    'date': 'May 2009 - Present'
  },
]

@app.route("/")
def hello_world():
    return render_template('home.html',
                          jobs=JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)