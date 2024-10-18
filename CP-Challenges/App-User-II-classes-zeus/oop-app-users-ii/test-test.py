#my own test "suite"


from User import User

def main():
    # Create a user
    user_name = input("Enter your name: ")
    user = User.create_user_with_name(user_name)

    while True:
        print("\nOptions:")
        print("1. Add a post")
        print("2. Delete a post")
        print("3. See my posts")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            content = input("Enter post content: ")
            user.create_a_post(content)
            print("Post added.")

        elif choice == "2":
            content = input("Enter the content of the post to delete: ")
            if user.delete_a_post(content):
                print("Post deleted.")
            else:
                print("Post not found.")

        elif choice == "3":
            print("Your posts:")
            user.see_my_posts()

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
