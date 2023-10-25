# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
import smtplib

ALLOWED_ACTIVITES = ["agriculture_food_and_natural_resources", "architecture_and_construction", "arts_audio_video_technology_and_communications", "business_management_and_administration", "education_and_training", "finance", "government_and_public_administration", "health_science", "human_services", "information_technology", "law_public_safety_corrections_and_security", "manufacturing", "marketing", "stem", "transportation_distribution_and_logistics"]

class ValidateActivitiesForm(FormValidationAction):
    def name(self) -> Text:
         return "validate_activities_form"

    def validate_interest_careers(
        self,
        slot_value: Any,    
        dispatcher: CollectingDispatcher, 
        Tracker: Tracker, 
        domain: DomainDict, 
    ) -> Dict[Text, Any]:
        """Validate interest careers value."""
        if slot_value.lower() not in ALLOWED_ACTIVITES:
            dispatcher.utter_message(text=f"Try rephasing your question or check your spelling. If you have already tried this, please email your counselor")
            return {"interest_careers": None}
        dispatcher.utter_message(text=f"lets see")
        return {"interest_careers": slot_value}

# Creating new class to send emails.
class ActionEmail(Action):
  
    def name(self) -> Text:
        
          # Name of the action
        return "action_email"
  
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
  
        # Getting the data stored in the
        # slots and storing them in variables.
        user_name = tracker.get_slot("name")
        email_id = tracker.get_slot("email")
          
        # Code to send email
        # Creating connection using smtplib module
        s = smtplib.SMTP('smtp.com',587)
          
        # Making connection secured
        s.starttls() 
          
        # Authentication
        s.login("SENDER_EMAILID", "PASSWORD")
          
        # Message to be sent
        message = "Hello {} , This is a demo message".format(user_name)
          
        # Sending the mail
        s.sendmail("SENDER_EMAIL_ID",email_id, message)
          
        # Closing the connection
        s.quit()
          
        # Confirmation message
        dispatcher.utter_message(text="Email has been sent.")
        return []