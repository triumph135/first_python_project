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

@app.route("/")
def hello_world():
    return render_template('home.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)