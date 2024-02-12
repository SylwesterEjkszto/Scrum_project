class ProductOwner:
    def __init__(self, name):
        self.accountability = {"Developing and explicitly communicating the Product Goal",
                               "Creating and clearly communicating Product Backlog items",
                               "Ordering Product Backlog items",
                               "Ensuring that the Product Backlog is transparent, visible and understood"}
        self.name = name


class ScrumMaster:
    def __init__(self, name):
        self.accountability = {"Scrum as defined in the Scrum Guide", "Scrum Team’s effectiveness",
                               "Ordering Product Backlog items"}
        self.name = name


class Developer:
    def __init__(self, name: str):
        self.accountability = {"Creating a plan for the Sprint, the Sprint Backlog",
                               "Instilling quality by adhering to a Definition of Done",
                               "Adapting their plan each day toward the Sprint Goal",
                               "Holding each other accountable as professionals"}
        self.name = name


class ScrumTeam:
    """
    The fundamental unit of Scrum is a small team of people, a Scrum Team. The Scrum Team consists of one Scrum
    Master, one Product Owner, and Developers. Within a Scrum Team, there are no sub-teams or hierarchies. It is a
    cohesive unit of professionals focused on one objective at a time, the Product Goal. Scrum Teams are
    cross-functional, meaning the members have all the skills necessary to create value each Sprint. They are also
    self-managing, meaning they internally decide who does what, when, and how.
    """

    def __init__(self, product_onwer: ProductOwner, scrum_master: ScrumMaster, developers=list):
        # The Scrum Team is small enough to remain nimble and large enough to complete
        # significant work within a Sprint, typically 10 or fewer people. . If Scrum Teams become too large,
        # they should consider reorganizing into multiple cohesive Scrum Teams
        self._maximum_size = 10
        self.product_owner = product_onwer
        self.scrum_master = scrum_master
        self.developers = developers
        self.scrum_team = [self.product_owner, self.scrum_master] + self.developers
