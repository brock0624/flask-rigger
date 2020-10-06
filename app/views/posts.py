# -*- coding:utf-8 -*-
import os

from PIL import Image
from flask_security import login_required
from flask import Blueprint, render_template, current_app, redirect, url_for, flash, request, render_template_string, \
    abort, g
from flask_security import current_user
# 创建蓝本对象
from app.extensions import photos, db
from app.forms.posts import PostsForm
from app.models import Post

posts = Blueprint('posts', __name__)


# 生成随机的字符串
def random_string(length=32):
    import random
    import string
    base_str = string.ascii_letters + string.digits
    return ''.join(random.choice(base_str) for _ in range(length))


@posts.route("/", methods=['GET', 'POST'])
def index():
    """Show all the posts, most recent first."""
    # form = PostsForm()
    # page = request.args.get('page', 1, type=int)
    pagination = Post.query.filter_by(rid=0). \
        order_by(Post.timestamp.desc()).paginate(1, per_page=3, error_out=False)
    posts = pagination.items
    return render_template('posts/index.html', posts=posts)


def get_post(id, check_author=True):
    """Get a post and its author by id.

    Checks that the id exists and optionally that the current user is
    the author.

    :param id: id of post to get
    :param check_author: require the current user to be the author
    :return: the post with author information
    :raise 404: if a post with the given id doesn't exist
    :raise 403: if the current user isn't the author
    """
    post = Post.query.filter_by(id=id).first()

    if post is None:
        abort(404, f"Post id {id} doesn't exist.")

    if check_author and post["author_id"] != g.user["id"]:
        abort(403)

    return post


@posts.route("/create", methods=("GET", "POST"))
@login_required
def create():
    """Create a new post for the current user."""
    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]
        error = None

        if not title:
            error = "Title is required."

        if error is not None:
            flash(error)
        else:

            return redirect(url_for("posts.index"))

    return render_template("posts/create.html")


@posts.route("/<int:id>/update", methods=("GET", "POST"))
@login_required
def update(id):
    """Update a post if the current user is the author."""
    post = get_post(id)

    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]
        error = None

        if not title:
            error = "Title is required."

        if error is not None:
            flash(error)
        else:

            return redirect(url_for("posts.index"))

    return render_template("posts/update.html", post=post)


@posts.route("/<int:id>/delete", methods=("POST",))
@login_required
def delete(id):
    """Delete a post.

    Ensures that the post exists and that the logged in user is the
    author of the post.
    """
    get_post(id)

    return redirect(url_for("posts.index"))
