# scrum/__init__.py

# Import modules to make them accessible directly from the package
from .backlog import ProductBacklogItem
from .sprint import Sprint
from .roles import ProductOwner, Developer, ScrumMater, ScrumTeam

__version__ = '1.0.0'


# Define the Scrum class
class Scrum:
    """
    Scrum is a lightweight framework that helps people, teams and organizations generate value through adaptive
    solutions for complex problems. https://scrumguides.org/scrum-guide.html

    In a nutshell, Scrum requires a Scrum Master to foster an environment where:

    A Product Owner orders the work for a complex problem into a Product Backlog.

    The Scrum Team turns a selection of the work into an Increment of value during a Sprint.

    The Scrum Team and its stakeholders inspect the results and adjust for the next Sprint.

    Repeat

    """

    def __init__(self, backlog: list = None, sprint_length: int = 4):
        # Each SCRUM project have backlog, you can learn more about this in Backlog class The Product Backlog is an
        # emergent, ordered list of what is needed to improve the product. It is the single source of work undertaken
        # by the Scrum Team.
        if backlog is None:
            backlog = []
        self.backlog = backlog

        # A sprint is a short, time-boxed period when a scrum team works to complete a set amount of work
        self.current_sprint = Sprint(sprint_length)

        # The fundamental unit of Scrum is a small team of people, a Scrum Team. The Scrum Team consists of one Scrum
        # Master, one Product Owner, and Developers. Within a Scrum Team, there are no sub teams or hierarchies. It
        # is a cohesive unit of professionals focused on one objective at a time, the Product Goal.
        self.teams = []
        self.Theory = {
            "Transparency": "The emergent process and work must be visible to those performing the work as well as "
                            "those receiving the work. With Scrum, important decisions are based on the perceived "
                            "state of its three formal artifacts. Artifacts that have low transparency can lead to "
                            "decisions that diminish value and increase risk. Transparency enables inspection. "
                            "Inspection without transparency is misleading and wasteful.",
            "Inspection": "The Scrum artifacts and the progress toward agreed goals must be inspected frequently and "
                          "diligently to detect potentially undesirable variances or problems. To help with "
                          "inspection, Scrum provides cadence in the form of its five events. Inspection enables "
                          "adaptation. Inspection without adaptation is considered pointless. Scrum events are "
                          "designed to provoke change.",
            "Adaptation": "If any aspects of a process deviate outside acceptable limits or if the resulting product "
                          "is unacceptable, the process being applied or the materials being produced must be "
                          "adjusted. The adjustment must be made as soon as possible to minimize further deviation. "
                          "Adaptation becomes more difficult when the people involved are not empowered or "
                          "self-managing. A Scrum Team is expected to adapt the moment it learns anything new through "
                          "inspection."}
        self.values = ("Commitment", "Focus", "Openness", "Respect", "Courage")

    # Scrum Events

    def sprint_planning(self):
        """
        Sprint Planning initiates the Sprint by laying out the work to be performed for the Sprint. This resulting
        plan is created by the collaborative work of the entire Scrum Team.

        The Product Owner ensures that attendees are prepared to discuss the most important Product Backlog items and
        how they map to the Product Goal. The Scrum Team may also invite other people to attend Sprint Planning to
        provide advice. Topic One: Why is this Sprint valuable? Topic Two: What can be Done this Sprint? Topic Three:
        How will the chosen work get done?

        """

        pass

    def daily_scrum(self):
        pass

    def sprint_review(self):
        pass

    def sprint_retrospective(self):
        pass

    def start_sprint(self, sprint_length):
        self.current_sprint = Sprint(sprint_length)

    def add_team(self, team):
        self.teams.append(team)
