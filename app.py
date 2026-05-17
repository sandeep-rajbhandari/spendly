import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import check_password_hash
from database.db import get_db, init_db, seed_db, create_user, get_user_by_email

app = Flask(__name__)
app.secret_key = "dev-secret-key"

with app.app_context():
    init_db()
    seed_db()


# ------------------------------------------------------------------ #
# Routes                                                              #
# ------------------------------------------------------------------ #

@app.route("/")
def landing():
    return render_template("landing.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if session.get("user_id"):
        return redirect(url_for("landing"))
    if request.method == "POST":
        name     = request.form.get("name", "").strip()
        email    = request.form.get("email", "").strip()
        password = request.form.get("password", "")
        confirm  = request.form.get("confirm_password", "")

        if not name or not email or not password or not confirm:
            flash("All fields are required.")
            return render_template("register.html")

        if password != confirm:
            flash("Passwords do not match.")
            return render_template("register.html")

        try:
            create_user(name, email, password)
        except sqlite3.IntegrityError:
            flash("Email already registered.")
            return render_template("register.html")

        flash("Account created! Please sign in.")
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if session.get("user_id"):
        return redirect(url_for("landing"))
    if request.method == "POST":
        email    = request.form.get("email", "").strip()
        password = request.form.get("password", "")

        user = get_user_by_email(email)
        if user is None or not check_password_hash(user["password_hash"], password):
            flash("Invalid email or password.")
            return render_template("login.html")

        session["user_id"]   = user["id"]
        session["user_name"] = user["name"]
        return redirect(url_for("profile"))

    return render_template("login.html")


# ------------------------------------------------------------------ #
# Placeholder routes — students will implement these                  #
# ------------------------------------------------------------------ #

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("landing"))


@app.route("/profile")
def profile():
    if not session.get("user_id"):
        return redirect(url_for("login"))

    user = {
        "name": "Alex Rivera",
        "email": "alex@example.com",
        "member_since": "January 2024",
        "initials": "AR",
    }
    stats = {
        "total_spent": "₹24,850",
        "transaction_count": 47,
        "top_category": "Food & Dining",
    }
    transactions = [
        {"date": "May 15, 2025", "description": "Swiggy",              "category": "Food & Dining",  "slug": "food",          "amount": "₹340"},
        {"date": "May 14, 2025", "description": "Metro Card Recharge", "category": "Transport",       "slug": "transport",     "amount": "₹500"},
        {"date": "May 13, 2025", "description": "Netflix",             "category": "Entertainment",   "slug": "entertainment", "amount": "₹649"},
        {"date": "May 12, 2025", "description": "D-Mart Groceries",    "category": "Groceries",       "slug": "groceries",     "amount": "₹1,200"},
        {"date": "May 10, 2025", "description": "Gym Membership",      "category": "Health",          "slug": "health",        "amount": "₹2,000"},
    ]
    categories = [
        {"name": "Food & Dining",  "amount": "₹8,400", "pct": 34},
        {"name": "Transport",      "amount": "₹3,200", "pct": 13},
        {"name": "Entertainment",  "amount": "₹2,800", "pct": 11},
        {"name": "Groceries",      "amount": "₹5,600", "pct": 23},
        {"name": "Health",         "amount": "₹4,850", "pct": 19},
    ]

    return render_template(
        "profile.html",
        user=user,
        stats=stats,
        transactions=transactions,
        categories=categories,
    )


@app.route("/expenses/add")
def add_expense():
    return "Add expense — coming in Step 7"


@app.route("/expenses/<int:id>/edit")
def edit_expense(id):
    return "Edit expense — coming in Step 8"


@app.route("/expenses/<int:id>/delete")
def delete_expense(id):
    return "Delete expense — coming in Step 9"


@app.route("/terms")
def terms():
    return render_template("terms.html")


@app.route("/privacy")
def privacy():
    return render_template("privacy.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
