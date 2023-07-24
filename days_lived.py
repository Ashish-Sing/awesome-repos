from datetime import datetime



def get_days_lived(birth_date):

    today = datetime.today()

    days_lived = (today - birth_date).days

    return days_lived



def main():

    # Ask for the user's date of birth

    dob_str = input("Enter your date of birth (YYYY-MM-DD): ")



    # Convert the user's input into a datetime object

    dob = datetime.strptime(dob_str, "%Y-%m-%d")



    # Calculate the number of days lived

    days_lived = get_days_lived(dob)



    print(f"You have lived for {days_lived} days.")



if __name__ == "__main__":

    main()


