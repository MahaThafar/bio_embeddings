from flask_restplus import fields
from webserver.endpoints import api

sequence_post_parameters = api.model("EmbeddingParameters", {
    # In frontend: protein.sequence
    "sequence": fields.String(
        required=False,
        description="Protein sequence in AA format",
        example="PWIQHFFKYACFSWPFHLTKVLSMIQAYGDHVVPFVQNDWPKYQKGVVDPRFWHFEFSFRCSWTAWWCLYFHCYLMHLGFIGRIQESHRMMTTYSQGPQT"
                "YPLMYFHMWVCVQETTYRTTYGTLSGEKKRVWITCQMGCKNPVNPDVNKTDGAVERFMQQYPICHNRFPLPCAENPSADWVKCHCNPQYIPWTEDRPYHS"
                "EPILDHIGCLHIFQKTYIYGRTAELVGYAGWAEEGVYKEMTFQFFHGDQIYMDWEHILRQIQRIRHWTQFKRGKMFHCVGFIHGRGWPSGFSQDWPEQNI"
                "HQMVQQSCGSWCHKWFGIKYTFKLWIGWLGHTRLELSKVSWGEANECNLMRIVVNQEACSAHAERREMWQSWNRYQYCHNFWNSWDQGMYGYSDAYAFGW"
                "QTPILPYRCVHHFYKACG"
    )
})