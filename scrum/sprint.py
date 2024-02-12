from .roles import *


class Sprint:
    """Sprints are the heartbeat of Scrum, where ideas are turned into value.

They are fixed length events of one month or less to create consistency. A new Sprint starts immediately after the
conclusion of the previous Sprint.

All the work necessary to achieve the Product Goal, including Sprint Planning, Daily Scrums, Sprint Review,
and Sprint Retrospective, happen within Sprints.

During the Sprint:

No changes are made that would endanger the Sprint Goal;

Quality does not decrease;

The Product Backlog is refined as needed; and,

Scope may be clarified and renegotiated with the Product Owner as more is learned.

"""

    def __init__(self, sprint_length: int):
        """
        Sprints enable predictability by ensuring inspection and adaptation of progress toward a Product Goal at
        least every calendar month. That's why max_length is 4 weeks A new Sprint starts immediately after the
        conclusion of the previous Sprint. - After sprint Retro / Sprint Planning initiates the Sprint by laying out
        the work to be performed for the Sprint. This resulting plan is created by the collaborative work of the
        entire Scrum Team.
        """
        self._max_length = 4
        if sprint_length > self._max_length:
            raise ValueError("Sprint length cannot be more than 4 weeks")
        self._length = sprint_length
        self.sprint_backlog = []
        # The Sprint Goal is the single objective for the Sprint. The Sprint Goal also creates coherence and focus,
        # encouraging the Scrum Team to work together rather than on separate initiatives.
        self.sprint_goal = ""
        self._sprint_goal_obsolete = False

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value: int):
        # Ensure that sprint is no longer than 4 weeks
        if value > self._max_length:
            raise ValueError("Sprint length cannot be more than 4 weeks")
        self._length = value

    @property
    def sprint_goal_obsolete(self):
        return self._sprint_goal_obsolete

    @sprint_goal_obsolete.setter
    def sprint_goal_obsolete(self, value: bool):
        if not isinstance(value, bool):
            raise ValueError("Sprint goal obsolete must be a boolean value")
        self._sprint_goal_obsolete = value

    def ready_to_work(self):
        return bool(self.sprint_backlog and self.sprint_goal)

    def set_sprint_goal(self, sprint_goal: str):
        self.sprint_goal = sprint_goal

    def sprint_cancellation(self, requester: ProductOwner):
        """
        A Sprint could be cancelled if the Sprint Goal becomes obsolete. Only the Product Owner has the authority to
        cancel the Sprint.
        """
        if isinstance(requester, ProductOwner) and self._sprint_goal_obsolete:
            return True
        else:
            return False
