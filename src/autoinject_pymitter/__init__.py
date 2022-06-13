""" Simple module that allows using pymitter as an auto-injected dependency """
from autoinject import injector as _injector
from pymitter import EventEmitter


@_injector.register(EventEmitter)
def _create_event_emitter():
    return EventEmitter(wildcard=True)

__version__ = "1.0.0"
