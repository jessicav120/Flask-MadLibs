from flask import Flask, render_template, request
from stories import story_list

app = Flask(__name__)

@app.route("/")
def pick_story():
    '''Choose a story template from a drop down menu'''
    stories = story_list.values()
    return render_template("choose_story.html", stories=stories)


@app.route("/form")
def prompt_form():
    '''Generate a form to receive answers for the story prompts.'''
    chosen_story = request.args["chosen_story"]
    story = story_list[chosen_story]
    title = story.title
    prompts = story.prompts
    return render_template("ans_form.html", prompts=prompts, chosen_story=chosen_story, title=title)

@app.route("/story")
def show_story():
    '''Create story using input words'''
    chosen_story = request.args["chosen_story"]
    story = story_list[chosen_story]
    ans = request.args
    title = story.title
    story_text = story.generate(ans)

    return render_template("story.html", story_text=story_text, title=title)