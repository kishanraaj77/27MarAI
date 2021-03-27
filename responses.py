from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi","whatsup"):
        return "hey ! Hows its going ?"
    if user_message in ("who are you", "who are you?"):
        return "I am KishanBOT"
    if user_message in ("time", "what is the time?", "what is the time","time?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y","%H:%M:%S")    

        return str(date_time)  

    return "i dont understnad you"  
