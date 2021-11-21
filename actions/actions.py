from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

ALLOWED_STYLES = ["digital", "traditional", "cartoon", "realistic"]
ALLOWED_MEDIUMS = ["colored", "line", "water color", "color pencil", "pencil", "oil color"]
ALLOWED_FIGURES = ["one", "two", "three", "four", "1","2","3","4","couple","single","family"]

class ValidateArtistForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_artist_form"

    def validate_style(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `style` value."""

        if slot_value.lower() not in ALLOWED_STYLES:
            dispatcher.utter_message(text=f"We only provide styles: digital, traditional, cartoon, realistic")
            return {"style": None}
        dispatcher.utter_message(text=f"OK! You want to have a {slot_value} drawing.")
        return {"style": slot_value}

    def validate_medium(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `medium` value."""

        if slot_value not in ALLOWED_MEDIUMS:
            dispatcher.utter_message(text=f"I don't recognize that type. We provide {'/'.join(ALLOWED_MEDIUMS)}.")
            return {"medium": None}
        dispatcher.utter_message(text=f"OK! You want to have a {slot_value} drawing.")
        return {"medium": slot_value}

    def validate_figures(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `figures` value."""

        if slot_value not in ALLOWED_FIGURES:
            dispatcher.utter_message(text=f"Sorry. We don't provide more than 4 figures.")
            return {"figures": None}
        dispatcher.utter_message(text=f"OK! You want to have a {slot_value} figures/drawing.")
        return {"figures": slot_value}