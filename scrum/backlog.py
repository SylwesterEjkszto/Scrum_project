from .roles import ProductOwner, ScrumMaster, Developer
# The Product Backlog is an emergent, ordered list of what is needed to improve the product. It is the single source of work undertaken by the Scrum Team.
backlog = [{"Product Goal":"The Product Goal describes a future state of the product  is the long-term objective for the Scrum Team. They must fulfill (or abandon) one objective before taking on the next."}]

class ProductBacklogItem():
    """
    A Product Backlog Item (PBI) is a single element of work that exists in the product backlog.
    """
    def __init__(self, description:str, priority:int, size:int):
        # A description with enough information for the Scrum team to understand what is needed for implementation
        self.description = description
        # Product Backlog items are ordered according to their value to the product, with the highest priority at the top.
        self.priority = priority
        # The Product Owner is accountable for maximizing the value of the product resulting from the work of the Scrum Team, as the Product Owner is responsible for Baclkog, baclkogitems should have business value
        self.business_value = ""
        # not a part of the Scrum Guide - The Srum Guide says that the elements of the Product Backlog must be understood so that the Scrum team is able to understand what is needed to complete them. While there is no direct mention of "acceptance criteria," the idea is related to understanding what is expected to be completed for each PBI(Product Backlog Item)
        self.acceptance_critera =""
        # The Scrum Guide talks about the need to estimate Product Backlog elements so that teams are able to determine how much work they can accomplish in a sprint. Despite the lack of direct mention of "size," estimating Backlog elements is an important step in work planning.
        self.size = size