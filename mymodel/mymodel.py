"""Definition of meta model 'mymodel'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *


name = 'mymodel'
nsURI = 'http://www.mymodel.com'
nsPrefix = 'mymodel'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)


class EEnum(Ecore.EEnum):

    def __init__(self, name=None, default_value=None, literals=None, **kwargs):
        super().__init__(name, default_value, literals)
        self.__dict__.update(kwargs)

    @property
    def value(self):
        ''' returns the value of the attribute '''
        for attr in [a for a in self.__dict__ if
                     not a.startswith('__') and not
                     a.startswith('_tx_')]:
            obj = getattr(self, attr)
            if obj and isinstance(obj, str):
                return obj


BasicTypeENUM = EEnum('BasicType', literals=['Boolean', 'String', 'Integer'])


class BasicType(EEnum):

    def __init__(self, name=None, default_value=None, literals=None, **kwargs):
        super().__init__(**kwargs)
        self.__dict__.update(BasicTypeENUM.from_string(self.value).__dict__)


class EObject(Ecore.EObject):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for key in kwargs:
            if self.__dict__.get(key, False):
                continue
            setattr(self, key, kwargs[key])


class Model(EObject, metaclass=MetaEClass):

    type = EReference(ordered=True, unique=True, containment=True, derived=False)
    reference = EReference(ordered=True, unique=True, containment=True, derived=False)
    problem = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, type=None, reference=None, problem=None, **kwargs):
        super().__init__(**kwargs)

        if type is not None:
            self.type = type

        if reference is not None:
            self.reference = reference

        if problem is not None:
            self.problem = problem


class ProblemRule(EObject, metaclass=MetaEClass):

    ref = EReference(ordered=True, unique=True, containment=False, derived=False)
    val = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, ref=None, val=None, **kwargs):
        super().__init__(**kwargs)

        if ref is not None:
            self.ref = ref

        if val is not None:
            self.val = val


class TypeReference(EObject, metaclass=MetaEClass):

    predefined = EAttribute(eType=BasicType, derived=False, changeable=True)
    derived = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, predefined=None, derived=None, **kwargs):
        super().__init__(**kwargs)

        if predefined is not None:
            self.predefined = predefined

        if derived is not None:
            self.derived = derived


class Type(EObject, metaclass=MetaEClass):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class StructType(Type):

    name = EAttribute(eType=EString, derived=False, changeable=True)

    def __init__(self, *, name=None, **kwargs):
        super().__init__(**kwargs)

        if name is not None:
            self.name = name


class TypeDefinition(Type):

    name = EAttribute(eType=EString, derived=False, changeable=True)

    def __init__(self, *, name=None, **kwargs):
        super().__init__(**kwargs)

        if name is not None:
            self.name = name
