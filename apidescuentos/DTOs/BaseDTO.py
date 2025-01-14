class BaseDTO:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_model(cls, model_instance):
        # Convertir modelo a DTO dinámicamente pasando los campos como kwargs
        return cls(**{field.name: getattr(model_instance, field.name) for field in model_instance._meta.fields.items()})