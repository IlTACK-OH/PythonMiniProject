def make_result(a_followers, b_followers, answer):        
    if answer == 'A':
        if a_followers > b_followers:
            return True
        return False
    
    elif answer == 'B':
        if a_followers < b_followers:
            return True
        return False