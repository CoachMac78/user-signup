
def character_check(email):
    total_at = 0
    email = "amac78@gmail.com"
    for char in email:
        if char == "@":
            total_at += 1
        return total_at
        #if total_at > 1 or total_at < 1:
        #    error = "Too many @'s. Not a valid email. Please try again."
character_check("amac78@gmail.com")