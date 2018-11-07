
from .mymodel import getEClassifier, eClassifiers
from .mymodel import name, nsURI, nsPrefix, eClass
from .mymodel import Model, ProblemRule, TypeReference, Type, StructType, TypeDefinition, BasicType


from . import mymodel


classes = [Model, ProblemRule, TypeReference, Type, StructType, TypeDefinition, BasicType]


__all__ = ['Model', 'ProblemRule', 'TypeReference',
           'Type', 'StructType', 'TypeDefinition', 'BasicType']

eSubpackages = []
eSuperPackage = None
mymodel.eSubpackages = eSubpackages
mymodel.eSuperPackage = eSuperPackage

Model.type.eType = Type
Model.reference.eType = TypeReference
Model.problem.eType = ProblemRule
ProblemRule.ref.eType = TypeReference
ProblemRule.val.eType = Type
TypeReference.derived.eType = Type

otherClassifiers = [BasicType]

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)
