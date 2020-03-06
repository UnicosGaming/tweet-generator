
# https://dev.to/mandrewcito/lazy-pub-sub-python-implementation-3fi8

class EventChannel():
    __instance = None

    def __init__(self):
        self.subscribers = {}

    def instance(self):
        if EventChannel.__instance is None:
            EventChannel.__instance = EventChannel()

        return EventChannel.__instance


    def subscribe(self, event, callback):
        if not callable(callback):
            raise ValueError("Callback must be callable")

        if event is None or event == "":
            raise ValueError("Event cannot be empty")

        if event not in self.subscribers.keys():
            self.subscribers[event] = [callback]
        else:
            if callback not in self.subscribers[event]:
                self.subscribers[event].append(callback)

    def unsubscribe(self, event, callback):
        if event is not None or event != "" and event in self.subscribers.keys():
            # self.subscribers[event] = list(filter(lambda x: x is not callback, self.subscribers[event]))
            if callback in self.subscribers[event]:
                self.subscribers[event].remove(callback)

    def publish(self, event, args = None):
        if event in self.subscribers.keys():
            for callback in self.subscribers[event]:
                if args is None:
                    callback()
                else:
                    callback(args)