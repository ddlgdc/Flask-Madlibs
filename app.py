from flask import Flask, render_template, request, redirect, url_for
from stories import Story

app = Flask(__name__, template_folder='templates')

story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        answers = {}
        for prompt in request.form.keys():
            answers[prompt] = request.form[prompt]

        generated_story = (
            f"Once upon a time in a long-ago {answers['place']}, there lived a "
            f"large {answers['adjective']} {answers['noun']}. It loved to "
            f"{answers['verb']} {answers['plural_noun']}."
        )

        return render_template('story.html', story=generated_story)
    else:
        prompts = ["place", "noun", "verb", "adjective", "plural_noun"]
        return render_template('form.html', prompts=prompts)
    
@app.route("/result", methods=["POST"])
def result():
    answers = {prompt: request.form[prompt] for prompt in story.prompts}
    madlibs_result = story.generate(answers)
    return render_template("result.html", madlibs_result=madlibs_result)
        
if __name__ == '__main__':
    app.run(debug=True)

