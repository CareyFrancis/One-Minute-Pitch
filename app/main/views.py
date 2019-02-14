from flask import render_template, request, redirect, url_for, abort
from . import main
from .forms import CommentsForm, UpdateProfile, PitchForm, UpvoteForm
from ..models import Comment, Pitch, User, Category
from flask_login import login_required, current_user
from .. import db
# import markdown2


@main.route('/')
@login_required
def index():
    title = 'PITCH-IT--HOME'

    search_pitch = request.args.get('pitch_query')
    pitches = Pitch.get_all_pitches()
    categories = Category.get_categories()
    return render_template('index.html', title=title, pitches=pitches, categories=categories)

# this section consist of the category root functions


@main.route('/product/pitches/')
def Business():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Business Ideas'
    pitches = Pitch.get_all_pitches()
    return render_template('business.html', title=title, pitches=pitches)


@main.route('/motivational/pitches/')
def Motivational():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Motivational Ideas'
    pitches = Pitch.get_all_pitches()
    return render_template('motivational.html', title=title, pitches=pitches)


@main.route('/technology/pitches/')
def Technology():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Technology Ideas'
    pitches = Pitch.get_all_pitches()
    return render_template('technology.html', title=title, pitches=pitches)


@main.route('/pitch/new/', methods=['GET', 'POST'])
@login_required
def new_pitch():

    form = PitchForm()
    if category is None:
        abort(404)

    if form.validate_on_submit():
        pitch = form.content.data
        category_id = form.category_id.data
        new_pitch = Pitch(pitch=pitch, category_id=category_id)

        new_pitch.save_pitch()
        return redirect(url_for('main.index'))

    return render_template('new_pitch.html', new_pitch_form=form, category=category)


@main.route('/category/<int:id>')
def category(id):

    category = PitchCategory.query.get(id)

    if category is None:
        abort(404)

    pitches_in_category = Pitches.get_pitch(id)
    return render_template('category.html', category=category, pitches=pitches_in_category)


@main.route('/pitch/comments/new/<int:id>', methods=['GET', 'POST'])
@login_required
def new_comment(id):
    form = CommentsForm()
    vote_form = UpvoteForm()
    if form.validate_on_submit():
        new_comment = Comment(pitch_id=id, comment=form.comment.data,
                              username=current_user.username, votes=form.vote.data)
        new_comment.save_comment()
        return redirect(url_for('main.index'))
    #title = f'{pitch_result.id} review'
    return render_template('comments.html', comment_form=form, vote_form=vote_form)


@main.route('/user/<uname>/update/pic', methods=['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username=uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = 'photos/{}'.format(filename)
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile', uname=uname))


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username=uname).first()

    if user is None:
        return render_template('fourOwFour.html')

    return render_template("profile/profile.html", user=user)


@main.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.username))

    return render_template('profile/update.html', form=form)


@main.route('/view/comment/<int:id>')
def view_comments(id):
    '''
    Function that returs  the comments belonging to a particular pitch
    '''
    comments = Comment.get_comments(id)
    return render_template('view_comments.html', comments=comments, id=id)


@main.route('/test/<int:id>')
def test(id):
    '''
    this is route for basic testing
    '''
    pitch = Pitch.query.filter_by(id=1).first()
    return render_template('test.html', pitch=pitch)
