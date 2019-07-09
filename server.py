from flask import Flask, render_template, request, redirect, session

from mysqlconnection import connectToMySQL    # import the function that will return an instance of a connection
app = Flask(__name__)


@app.route("/")
def index():
    mysql = connectToMySQL('c_r_pets')	        # call the function, passing in the name of our db
    pets = mysql.query_db('SELECT * FROM pets;')  # call the query_db function, pass in the query as a string
    return render_template("index.html", all_pets = pets)



@app.route("/create_pet", methods=["POST"])
def add_pet_to_db():
    # QUERY: INSERT INTO first_flask (first_name, last_name, occupation, created_at, updated_at) 
    #                         VALUES (fname from form, lname from form, occupation from form, NOW(), NOW());
    mysql = connectToMySQL('c_r_pets')

    query = "INSERT INTO pets (name, type, created_at, updated_at) VALUES (%(nm)s, %(typ)s, NOW(), NOW());"

    data = {
        "nm": request.form["name"],
        "typ": request.form["typ"]
    }
    
    new_friend_id = mysql.query_db(query, data)
    return redirect("/")

            
if __name__ == "__main__":
    app.run(debug=True)