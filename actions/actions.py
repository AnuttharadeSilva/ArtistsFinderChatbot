from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.events import EventType, AllSlotsReset
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet

# ALLOWED_mediumS = ["ඩිජිටල්", "සම්ප්‍රදායික"]
# ALLOWED_MEDIUMS = ["වර්ණවත්", "රේඛා"]
# # ALLOWED_FIGURES = ["එක", "දෙක", "තුන", "හතර", "1","2","3","4","යුගල","තනි","පවුලේ"]

# class ValidateArtistForm(FormValidationAction):
#     def name(self) -> Text:
#         return "validate_artist_form"

#     def validate_medium(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate `medium` value."""

#         if slot_value.lower() not in ALLOWED_mediumS:
#             dispatcher.utter_message(text=f"සමාවෙන්න. අපි සපයන්නේ මේ ශෛලීන් පමණයි. {'/'.join(ALLOWED_mediumS)}")
#             return {"medium": None}
#         dispatcher.utter_message(text=f"හරි. ඔබට අවශ්‍ය චිත්‍ර ශෛලිය: {slot_value}.")
#         return {"medium": slot_value}

#     def validate_medium(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         """Validate `medium` value."""

#         if slot_value not in ALLOWED_MEDIUMS:
#             dispatcher.utter_message(text=f"සමාවෙන්න. අපි සපයන්නේ මේ මාධ්‍යන් පමණයි. {'/'.join(ALLOWED_MEDIUMS)}.")
#             return {"medium": None}
#         dispatcher.utter_message(text=f"හරි. ඔබට අවශ්‍ය චිත්‍ර මාධ්‍ය:  {slot_value}.")
#         return {"medium": slot_value}

#     # def validate_figures(
#     #     self,
#     #     slot_value: Any,
#     #     dispatcher: CollectingDispatcher,
#     #     tracker: Tracker,
#     #     domain: DomainDict,
#     # ) -> Dict[Text, Any]:
#     #     """Validate `figures` value."""

#     #     if slot_value not in ALLOWED_FIGURES:
#     #         dispatcher.utter_message(text=f"සමාවෙන්න. උපරිම මිනිස් රූප ගණන 4යි.")
#     #         return {"figures": None}
#     #     dispatcher.utter_message(text=f"හරි. ඔබට අවශ්‍ය මිනිස් රූප ගණන: {slot_value}.")
#     #     return {"figures": slot_value}

class ActionResetAllSlots(Action):

    def name(self):
        return "action_reset_all_slots"

    def run(self, dispatcher, tracker, domain):
        return [AllSlotsReset()]



MEDIUMS = ["ඩිජිටල්", "Digital", "digital"]
STYLES = ["වර්ණවත්", "colored", "Colored","වර්නවත්"]
BACKGROUNDS = ["ඕනේ","ඔව්","අවශ්‍යයි","yes","yep","අදින්න","ඕ"]

class CalculatePrice(Action):

    def name(self):
        return "action_calculate_price"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        medium = tracker.get_slot("medium")
        style = tracker.get_slot("style")
        background = tracker.get_slot("background")
        price = 1000

        if medium in MEDIUMS:
            price += 500
        if style in STYLES:
            price += 500
        if background in BACKGROUNDS:
            price += 500

        return[SlotSet("price", price)]