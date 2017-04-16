
class User(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.posts = [] # list of Post objects
        self.following = [] # list of User objects
        
    def __eq__(self, other):
        return (self.first_name == other.first_name and
                self.last_name == other.last_name and
                self.email == other.email)

    def add_post(self, post):
        self.posts.append(post)
        self.posts[-1].set_user(self)

    def get_timeline(self):
        # return all posts from people I'm following
        # sort by most recent to least
        timeline = []
        for followee in self.following:
            for followee_post in followee.posts:
                timeline.append(followee_post)
        return sorted(timeline, key=lambda post: post.timestamp, reverse=False)

    def follow(self, other):
        self.following.append(other)