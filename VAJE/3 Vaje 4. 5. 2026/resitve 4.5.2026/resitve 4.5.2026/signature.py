from pyasn1.type import univ, namedval, constraint
from pyasn1.type import  namedtype, tag, char
from pyasn1.type import useful


class RealSeq(univ.SequenceOf):
      componentType = univ.Real()

class Signals(univ.Sequence):
        componentType = namedtype.NamedTypes(
                namedtype.NamedType('id',char.PrintableString()),
                namedtype.OptionalNamedType('DI',univ.Integer()),
                namedtype.OptionalNamedType('RPM',univ.Real()),
                namedtype.NamedType('a',RealSeq()),
                )


class Record(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('id', univ.Integer()),
        namedtype.OptionalNamedType(
            'room', univ.Integer().subtype(
                implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)
            )
        ),
        namedtype.DefaultedNamedType(
            'house', univ.Integer(0).subtype(
                implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1)
            )
        )
    )


class Measurement(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('SensorID', univ.Integer()),
        namedtype.NamedType(
            'Type', char.UTF8String().subtype(
                subtypeSpec = constraint.SingleValueConstraint("Temperature", "Pressure")
            )
        ),
        namedtype.NamedType('Values', univ.SequenceOf(componentType = univ.Real())))