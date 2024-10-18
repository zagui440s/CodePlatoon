import pytest
from User import User

# Initialize user instances
user = User("John", "john@email.com", "FDUI87")
user2 = User("Mike", "mike@email.com", "FDUI87")
user3 = User("Zack", "zack@email.com", "FDUI87")

@pytest.fixture
def user_with_posts():
    user = User("John", "john@email.com", "FDUI87")
    user.create_a_post("First post")
    user.create_a_post("Second post")
    user.create_a_post("Third post")
    return user

def test_init_user():
    assert user.name == "John"
    assert user.email == "john@email.com"
    assert user.drivers_license == "FDUI87"

@pytest.fixture
def test_create_post(monkeypatch, capsys):
    input_data = iter(["Johns †i†le", "I Just joined OOPX"])
    monkeypatch.setattr("builtins.input", lambda _x: next(input_data))
    user.create_a_post("Johns †i†le")  # Pass the content
    assert len(user.posts) == 1
    assert len(User.all_posts) == 1  # Check class-level posts
    user.see_my_posts()
    out, err = capsys.readouterr()
    assert "Johns †i†le" in out

def test_delete_post(monkeypatch, capsys):
    # Create a post to delete
    user.create_a_post("Post to delete")
    assert len(user.get_posts()) == 1
    assert len(User.all_posts) == 1

    user.delete_a_post("Post to delete")  # Correctly call with content
    assert len(user.get_posts()) == 0
    assert len(User.all_posts) == 0  # Check class-level posts
    user.see_my_posts()
    out, err = capsys.readouterr()
    assert out == ""

def test_see_all_posts(monkeypatch, capsys):
    assert len(user.get_posts()) == 0
    assert len(user.posts) == 0
    user.see_my_posts()
    out, err = capsys.readouterr()
    assert out == ""

    # Adding posts for user3
    user3.create_a_post("cats meow")
    assert len(user3.get_posts()) == 1  # Check user3's posts
    assert len(user.get_posts()) == 0   # user should still have 0 posts

    # Adding posts for user2
    user2.create_a_post("rabble")
    assert len(user2.get_posts()) == 1  # Check user2's posts
    assert len(user.get_posts()) == 0   # user should still have 0 posts

    # Adding posts for user
    user.create_a_post("I Just joined OOPX")
    assert len(user.get_posts()) == 1   # Now user should have 1 post

def test_see_my_posts(monkeypatch, capsys, user_with_posts):
    user = user_with_posts  # Use the user created by the fixture
    assert len(user.get_posts()) == 3  # Check user posts

    user.create_a_post("Zack åttåck")  # Pass content directly
    assert len(user.get_posts()) == 4  # Now user should have 4 posts

    user.create_a_post("Mikes πost")  # Pass content directly
    assert len(user.get_posts()) == 5  # Now user should have 5 posts

    user.create_a_post("Johns †i†le")  # Pass content directly
    assert len(user.get_posts()) == 6  # Now user should have 6 posts
