from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:Bulldogs08!@localhost:3306/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String (120))
    blog_post =  db.Column(db.String (120))
    
    def __init__(self, title, text):
        self.title = title
        self.blog_post = text



@app.route('/blog', methods=['GET'])
def blog():
    posts = Blog.query.all()
    if request.args.get('id'):
        post_id = request.args.get('id')
        individual_post = Blog.query.get(post_id)
        return render_template('individual_post.html', title={}, post=individual_post)

    return render_template('blog.html',title = "Blog Archive", 
        posts = posts)


@app.route('/new_post', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        post_title = request.form['title']
        blog_post = request.form['blog post']
        user_error = ""
        if post_title == user_error or blog_post == user_error:
            return render_template('new_post.html',title = "New Post", user_error = "please input text into approriate fields", blog_title = post_title, blog_post= blog_post)
        new_blog_post = Blog(post_title, blog_post)
        db.session.add(new_blog_post)
        db.session.commit()
        return redirect ('/blog?id={0}'.format(new_blog_post.id)) 
    return render_template('new_post.html',title = "New Post")


if __name__ == '__main__':
    app.run()

