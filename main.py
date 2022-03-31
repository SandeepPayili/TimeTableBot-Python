import telegram.ext
import timetable as tt
from datetime import datetime

with open("token.txt","r") as f:
    TOKEN = f.read()

def start(update,context):
    update.message.reply_text("Hello! 👋 Iam Time Table Bot.")
def help(update,context):
    update.message.reply_text("""
    The Following Commands are availabe :

    /start      -> Welcome Message
    /help       -> Help Message
    /timetable  -> View Time Table
    /now        -> Current Ongoing Class
    /next       -> Next Class
    /today      -> List Today's Classes
    /monday     -> View Monday's Classes
    /tuesday    -> View Tuesday's Classes
    /wednessday -> View Wednessday's Classes
    /thursday   -> View Thursday's  Classes
    /friday     -> View Friday's Classes

    """)

def timetable(update,context):
    to_display = "*********       E3S2 AB2-309 Class Time Table       *********\n"
    for key,value in tt.timetable.items():
        to_display += "\n" + key.upper() + " :-  \n"
        for i in value :
            to_display += i +"\n"
    to_display += "\n ☞ Be Crazy Have Fun!  ☜\n"
    update.message.reply_text(to_display)

def monday(update,context):
    to_display = "Monday :- \n"
    for value in tt.timetable["monday"]:
        to_display += value + "\n"
    update.message.reply_text(to_display)

def tuesday(update,context):
    to_display = "Tuesday :- \n"
    for value in tt.timetable["tuesday"]:
        to_display += value + "\n"
    update.message.reply_text(to_display)

def wednessday(update,context):
    to_display = "Wednessday :- \n"
    for value in tt.timetable["wednessday"]:
        to_display += value + "\n"
    update.message.reply_text(to_display)

def thursday(update,context):
    to_display = "Thursday :- \n"
    for value in tt.timetable["thursday"]:
        to_display += value + "\n"
    update.message.reply_text(to_display)

def friday(update,context):
    to_display = "Friday :- \n"
    for value in tt.timetable["friday"]:
        to_display += value + "\n"
    update.message.reply_text(to_display)

def today(update,context):
    days = ["Monday", "Tuesday", "Wednesday","Thursday", "Friday", "Saturday", "Sunday"]
    weekday = datetime.now().weekday()
    day = days[weekday].lower()
    if (day == "saturday" or day == "sunday"):
        update.message.reply_text("Chill 😎 You don't Have Classes today ^_^ ")
    else:
        globals()[day](update,context)

def now(update,context):
    days = ["Monday", "Tuesday", "Wednesday","Thursday", "Friday", "Saturday", "Sunday"]
    weekday = datetime.now().weekday()
    day = days[weekday].lower()
    if (day == "saturday" or day == "sunday"):
        update.message.reply_text("Chill 😎 You don't Have Classes today ^_^ ")
    else:
        current_hour = int(datetime.now().strftime("%H"))
        today_classes = tt.timetable[day]
        message = " "
        if current_hour < int("09") or current_hour >= int("17") :
            message += "Hurray ! You don't Have any class now."
        else:
            if (current_hour > 12) :
                current_hour -= 12
            for i in today_classes :
                if str(current_hour) in i :
                    message += i        
        update.message.reply_text(message)

def next(update,context):
    days = ["Monday", "Tuesday", "Wednesday","Thursday", "Friday", "Saturday", "Sunday"]
    weekday = datetime.now().weekday()
    day = days[weekday].lower()
    if (day == "saturday" or day == "sunday"):
        update.message.reply_text("Chill 😎 You don't Have Classes today ^_^ ")
    else:
        current_hour = int(datetime.now().strftime("%H"))
        today_classes = tt.timetable[day]
        message = " "
        if current_hour < int("08") or current_hour >= int("16") :
            message += "Hurray ! You don't Have any class next."
        else:
            current_hour +=1 # to get next hour
            if (current_hour > 12) :
                current_hour -= 12
            for i in today_classes :
                if str(current_hour) in i :
                    message += i
                    break        
        update.message.reply_text(message)

def error(update,context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater = telegram.ext.Updater(TOKEN,use_context=True)
    disp = updater.dispatcher

    disp.add_handler(telegram.ext.CommandHandler("start",start))
    disp.add_handler(telegram.ext.CommandHandler("help",help))
    disp.add_handler(telegram.ext.CommandHandler("today",today))
    disp.add_handler(telegram.ext.CommandHandler("now",now))
    disp.add_handler(telegram.ext.CommandHandler("next",next))
    disp.add_handler(telegram.ext.CommandHandler("timetable",timetable))
    disp.add_handler(telegram.ext.CommandHandler("monday",monday))
    disp.add_handler(telegram.ext.CommandHandler("tuesday",tuesday))
    disp.add_handler(telegram.ext.CommandHandler("wednessday",wednessday))
    disp.add_handler(telegram.ext.CommandHandler("thursday",thursday))
    disp.add_handler(telegram.ext.CommandHandler("friday",friday))

    disp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()