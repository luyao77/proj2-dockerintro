from flask import Flask,render_template
import os

app = Flask(__name__)

@app.route("/<path:path>") #

def show_name(path):
    #print(path)
    valid = ".html", ".css"
    invalid = ["~","..","//"]
    if(any(s in path for s in invalid)):
         return render_template("403.html"), 403
    elif not path.endswith(valid):
         return render_template("403.html"), 403
    else:
        # try:
        #     source_path = "./pages/" + path
        #     return render_template(source_path)
        #
        # except Os as error:
        #     return render_template("404.html"), 404
        try:
                #print(os.getcwd())
                source_path = "./pages/" + path
                with open(source_path, 'r') as source:
                    return source.read()
        except OSError as error:
                return render_template("404.html"), 404
    #return path
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
