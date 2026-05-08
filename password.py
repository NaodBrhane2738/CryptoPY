from zxcvbn import zxcvbn
from getpass import getpass
import bcrypt


def pass_strength(password):
    result = zxcvbn(password)
    score = result["score"]
    if score == 3:
        response = "Strong password: Score of 3"
    elif score == 4:
        response = "Very Strong password: Score of 4"
    else:
        feedback = result.get("feedback")
        warning = feedback.get("warning")
        suggestions = feedback.get("suggestions")
        response = "Weak password: Score of " + str(score)
        response += "\nwarning: " + warning
        response += "\nsuggestions: "
        for suggestion in suggestions:
            response += " " + suggestion
    return response

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed

def check_password(pass_attempt, hashed):
    if bcrypt.checkpw(pass_attempt.encode(), hashed):
        return "Password is correct!"
    else:
        return "Password is incorrect."


if __name__ == "__main__":
    while True:
        password = getpass("Enter Your Password: ")
        pass_msg = pass_strength(password)
        print(pass_msg)

        if pass_msg.startswith("Weak"):
            print(f"'{password}' is a Weak password, please try stronger password.")
        else:
            print("Strong Enough password!!!")
            break

    hashed_password = hash_password(password)
    print("The hashed password is: ", hashed_password)
    attempt = getpass("Re-enter the password to verify: ")
    print(check_password(attempt, hashed_password))
