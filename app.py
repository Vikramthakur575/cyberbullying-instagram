from flask import Flask, render_template, request

app = Flask(__name__)

bullying_words = ["stupid", "idiot", "useless", "hate", "kill"]

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    warning = ""
    show_image = False

    if request.method == "POST":
        comment = request.form["comment"].lower()

        if any(word in comment for word in bullying_words):
            warning = "⚠️ Cyberbullying detected! Please delete the comment or action will be taken."
            show_image = True
        else:
            message = "✅ Comment posted successfully."

    return render_template(
        "index.html",
        message=message,
        warning=warning,
        show_image=show_image
    )

if __name__ == "__main__":
    app.run(debug=True)
