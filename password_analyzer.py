import re
import secrets
import string
def analyze_password(password):
    score=0
    feedback=[]
    if len(password) >=12:
        score+= 2
    elif len(password) >=8:
        score +=1
    else:
        feedback.append("- Password length should be at least 8 characters")
    if re.search(r"[A-Z]" ,password):
        score +=1
    else:
        feedback.append("- Add at least one uppercase letter (A-Z)")
    if re.search(r"[a-z]", password):
        score +=1
    else:
        feedback.append("- Add at least one lowercase letter (a-z)")
    if re.search(r"\d", password):
        score +=1
    else:
        feedback.append("- Include at least one numeric digit(0-9)")
    if re.search(r"[@$!%*?#&^]", password):
        score +=1
    else:
        feedback.append("- Include at least one special character(eg., $, %, @, &, *)")
    if score >= 5:
        strength = "STRONG 🔒"
    elif 3 <= score < 5:
        strength = "MEDIUM "
    else:
        strength = "WEAK ❌"
    return strength, feedback

def generate_strong_alternative():
    uppercase = secrets.choice(string.ascii_uppercase)
    lowercase = secrets.choice(string.ascii_lowercase)
    digits = secrets.choice(string.digits)
    special = secrets.choice("@$!%*?&#")
    all_chars = string.ascii_letters + string.digits + "@$!%*?&#"
    remaining = "".join(secrets.choice(all_chars)for _ in range(8))

    password_list = list(uppercase + lowercase + digits + special + remaining)
    secrets.SystemRandom().shuffle(password_list)
    return "".join(password_list)

def main():
    print("="*50)
    print(" Thiranex Password Strength Analyzer ")
    print("="*50)

    while True:
        user_password = input("\n Enter a password to analyze (or type 'exit' to quit): ").strip()
        if user_password.lower() == 'exit':
            print("\n Thank you!")
            break
        if not user_password:
            print("Password should not be empty. Try again")
            continue
        strength, suggestions = analyze_password(user_password)
        print(f"\n Result Summary: {strength}")

        if suggestions:
            print("\n Suggestion to Improve:")
            for tip in suggestions:
                print(tip)
            print(f"\n Suggested alternative: {generate_strong_alternative()}")
        else:
            print("Excellent! Meeting all standard guidelines")
        print("-" * 50)

if __name__ == "__main__":
    main()


