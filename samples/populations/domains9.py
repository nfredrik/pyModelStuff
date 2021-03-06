"""
PyModel configuration -- functions in domains
"""

import random
import populations

# functions that return domains, each function must return a collection

def random9():
    return [ random.randint(0,9) ] # returns singleton list

def current_population():
    return populations.population

# each domain must be a collection, or a callable that returns a collection

populations.domains = { populations.add: { 'ident': random9 }, # singleton
                        populations.remove: { 'ident': current_population } }
