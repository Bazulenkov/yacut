import random
import string

from flask import flash, render_template, redirect

from settings import LINK_LENGTH, DUPLICATE_MESSAGE, NEW_LINK_MESSAGE
from . import app, db
from .forms import UrlMapForm
from .models import URLMap


def get_unique_short_id() -> str:
    characters = string.ascii_letters + string.digits
    while True:
        result = "".join(random.choice(characters) for _ in range(LINK_LENGTH))
        if URLMap.query.filter_by(short=result).first() is None:
            return result


@app.route("/", methods=["GET", "POST"])
def add_short_link_view():
    form = UrlMapForm()
    if form.validate_on_submit():
        if URLMap.query.filter_by(short=form.custom_id.data).first() is not None:
            flash(DUPLICATE_MESSAGE.format(form.custom_id.data))
            return render_template("add_short_link.html", form=form)
        short = form.custom_id.data or get_unique_short_id()
        urlmap = URLMap(original=form.original_link.data, short=short)
        db.session.add(urlmap)
        db.session.commit()
        context = {"form": form, "urlmap": urlmap}
        flash(NEW_LINK_MESSAGE)
        return render_template("add_short_link.html", **context)
    return render_template("add_short_link.html", form=form)


@app.route("/<path:short>")
def open_short_view(short):
    urlmap = URLMap.query.filter_by(short=short).first_or_404()
    return redirect(urlmap.original)
