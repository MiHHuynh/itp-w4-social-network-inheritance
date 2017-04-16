from datetime import datetime

class Post(object):
    def __init__(self, text, timestamp=None):
        self.text = text
        self.timestamp = timestamp
        self.user = None

    def set_user(self, user):
        self.user = user

class TextPost(Post):  # Inherit properly
    def __init__(self, text, timestamp=None):
        super(TextPost, self).__init__(text, timestamp)
        self.user = None

    def __str__(self):
        actual_post = '@{} {}: "{}"\n\t{}, {} {}, {}'
        return actual_post.format(
            self.user.first_name, 
            self.user.last_name,
            self.text,
            self.timestamp.strftime("%A"),
            self.timestamp.strftime("%b"), 
            self.timestamp.strftime("%d"),
            self.timestamp.strftime("%Y"))
            
    def __repr__(self):
        return str(self)
            
    def __eq__(self, other):
        """
        Equality of the objects are defined by equal attributes in case
        copies of objects are made.
        """
        return (self.user == other.user and 
                self.text == other.text and
                self.timestamp == other.timestamp)
        

class PicturePost(Post):  # Inherit properly
    def __init__(self, text, image_url, timestamp=None):
        super(PicturePost, self).__init__(text, timestamp)
        self.image_url = image_url
        self.user = None

    def __str__(self):
        actual_post = '@{} {}: "{}"\n\t{}\n\t{}, {} {}, {}'
        return actual_post.format(
            self.user.first_name,
            self.user.last_name,
            self.text,
            self.image_url,
            self.timestamp.strftime("%A"),
            self.timestamp.strftime("%b"), 
            self.timestamp.strftime("%d"),
            self.timestamp.strftime("%Y"))


class CheckInPost(Post):  # Inherit properly
    def __init__(self, text, latitude, longitude, timestamp=None):
        super(CheckInPost, self).__init__(text, timestamp)
        self.latitude = latitude
        self.longitude = longitude
        self.user = None

    def __str__(self):
        actual_post = '@{} Checked In: "{}"\n\t{}, {}\n\t{}, {} {}, {}'
        return actual_post.format(
            self.user.first_name,
            self.text,
            self.latitude,
            self.longitude,
            self.timestamp.strftime("%A"),
            self.timestamp.strftime("%b"), 
            self.timestamp.strftime("%d"),
            self.timestamp.strftime("%Y"))