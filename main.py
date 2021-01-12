from flask import Flask, render_template, request, url_for, flash, redirect, send_from_directory, Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')