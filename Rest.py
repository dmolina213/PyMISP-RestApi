# this will test simple event extraction in MISP
misp_url = 'https://misp1.kamuning176.com'
misp_key = 'sEAgO9AHWiC04xswoU2g3WQFYWaq4fTM5Hc8ZQ13'
misp_verifycert = True
relative_path = 'attributes/restSearch'
body = {
    "returnFormat": "json",
    "type": {
        "OR": [
            "ip-src",
            "ip-dst"
        ]
    },
    "tags": {
        "NOT": [
            "tlp:red"
        ],
        "OR": [
            "tlp:%"
        ]
    }
}

from pymisp import ExpandedPyMISP

misp = ExpandedPyMISP(misp_url, misp_key, misp_verifycert)
misp.direct_call(relative_path, body)
