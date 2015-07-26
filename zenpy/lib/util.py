import collections
from json import JSONEncoder
import logging

__author__ = 'facetoe'
log = logging.getLogger(__name__)


class ApiObjectEncoder(JSONEncoder):
	""" Class for encoding API objects"""
	def default(self, o):
		return o.to_dict()


def cached(cache):
	"""
	Decorator for caching return values.
	:param cache: The cache for this decorated method
	"""
	def outer(func):
		def inner(*args):
			id = args[1]
			if id in cache:
				return cache[id]
			else:
				value = func(*args)
				log.debug("Caching: " + value.__class__.__name__)
				cache[id] = value
				return value

		return inner

	return outer