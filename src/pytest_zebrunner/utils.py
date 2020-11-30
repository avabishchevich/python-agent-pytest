class Singleton(type):
    __instance = None

    def __call__(cls, *args, **kwargs):  # type: ignore
        if not isinstance(cls.__instance, cls):
            cls.__instance = super(Singleton, cls).__call__(*args, **kwargs)

        return cls.__instance
