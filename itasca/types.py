import itasca
from typing import Union

# There may be many contacts, however, I only use the following two contacts.
# You can artificially specify contact types like the following code:
# ```
# for contact in itasca.contact.list():
#     contact: Union[itasca.BallFacetContact, itasca.BallBallContact]
# ```
Contacts = Union[itasca.BallBallContact, itasca.BallFacetContact]
