class User:
    all_posts = []  # Static variable to store all posts

    def __init__(self, name, email=None, drivers_license=""):
        self._name = name
        self._email = email
        self._drivers_license = drivers_license
        self._posts = []

    @property
    def name(self):
        return self._name
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError("Invalid email address")
        self._email = value
    
    @property
    def drivers_license(self):
        return self._drivers_license
    
    @property
    def posts(self):  # Add this property
        return self._posts
    
    @classmethod
    def create_user_with_name(cls, name):
        return cls(name)

    def create_a_post(self, content):
        post = {'content': content, 'user': self._name}  # Simple dictionary for the post
        self._posts.append(post)  # Add post to the user's list
        User.all_posts.append(post)  # Add post to the class-level list

    def delete_a_post(self, content):
        for post in self._posts:
            if post['content'] == content:
                self._posts.remove(post)
                User.all_posts.remove(post)
                return True
        return False
       

    def get_posts(self):
        return self._posts  # Return the user's posts
    
    def see_my_posts(self):
        if not self._posts:
            return ""
        else:
            for post in self._posts:
                print(post['content'])


    def __repr__(self):
        return f"User(name={self._name}, email={self._email})"