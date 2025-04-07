from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
class ActionSocial(Action):

    def name(self) -> Text:
        return "action_social"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name=tracker.get_slot("names")
        phone_no=tracker.get_slot("phone")
        if phone_no:
            dispatcher.utter_message(text=f"Thank You {name}, Our associates will return to you to help")
        else:
            dispatcher.utter_message(text="Sorry we are unable to help you")

        return []
class ActionNgo(Action):

    def name(self) -> Text:
        return "action_ngo"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name=tracker.get_slot("names")
        email_id=tracker.get_slot("email")
        if email_id:
            dispatcher.utter_message(text=f"Thank You {name}, for taking interest in us. Our team will verify your NGO and will return to you through email id {email_id}")
        else:
            dispatcher.utter_message(text="Sorry we are unable to help you")

        return []
