from mymodel import classes

from textx.metamodel import metamodel_from_file
from textx.scoping import MetaModelProvider
from textx.scoping.providers import PlainName

class ProblemRuleValProvider():
    def __call__(self, obj, attr, obj_ref):
        reference = obj.parent.reference
        if reference.predefined:
            # imagine meaningful code here
            obj.attribute = 42
        print(hasattr(obj, 'attribute')) # prints True
        return reference

if __name__ == '__main__':
    mm = metamodel_from_file('Grammar.tx', classes=classes)
    MetaModelProvider.add_metamodel('*.g', mm)

    mm.register_scope_providers({
        "ProblemRule.ref": ProblemRuleValProvider(),
        "*.*": PlainName(),
    })
    model = mm.model_from_file("mymodel.g")
    print(model)

