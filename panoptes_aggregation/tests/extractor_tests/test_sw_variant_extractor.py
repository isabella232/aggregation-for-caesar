import unittest
import json
import flask
from panoptes_aggregation import extractors
from panoptes_aggregation.extractors.test_utils import annotation_by_task

classification = {
    'annotations': [
        {
            "task": "T2",
            "value": [
                {
                    "text": "It sets ââ\u003cbrev-y\u003eth\u003c/brev-y\u003e\u003csl\u003ee\u003c/sl\u003eâ bodie all ina sweat present=\u003cbr\u003e",
                    "type": "text",
                    "complete": True,
                    "endPoint": {"x": 1023.08, "y": 1114.95},
                    "variants": ["ina"],
                    "startPoint": {"x": 146.41, "y": 1193.12}
                }, {
                    "text": "ly, and must bee vsed twice as it was\u003cbr\u003e",
                    "type": "text",
                    "complete": True,
                    "endPoint": {"x": 1007.25, "y": 1156.51},
                    "startPoint": {"x": 155.31, "y": 1241.61}
                }, {
                    "text": "with Mr. Combes: hee observd this âââ\u003cbrev-y\u003eth\u003c/brev-y\u003e\u003csw-ex\u003ea\u003c/sw-ex\u003e\u003csl\u003et\u003c/sl\u003eâ\u003cbr\u003e",
                    "type": "text",
                    "complete": True,
                    "endPoint": {"x": 1018.13, "y": 1204.99},
                    "variants": ["observd"],
                    "startPoint": {"x": 144.43, "y": 1281.18}
                }, {
                    "text": "afterword ââ\u003cbrev-y\u003eth\u003c/brev-y\u003e\u003csl\u003ee\u003c/sl\u003eâ skin: peeld off both vppon\u003cbr\u003e",
                    "type": "text",
                    "complete": True,
                    "endPoint": {"x": 1014.18, "y": 1243.58},
                    "variants": ["peeld"],
                    "startPoint": {"x": 155.31, "y": 1326.7}
                }, {
                    "text": "ââ\u003cbrev-y\u003eth\u003c/brev-y\u003e\u003csl\u003ee\u003c/sl\u003eâ oot and sole.\u003cbr\u003e",
                    "type": "text",
                    "complete": True,
                    "endPoint": {"x": 628.28, "y": 1333.63},
                    "startPoint": {"x": 165.21, "y": 1370.24}
                }, {
                    "text": "and it left ââ\u003cbrev-y\u003eth\u003c/brev-y\u003e\u003csl\u003ee\u003c/sl\u003eâ foot weak euer\u003cbr\u003e",
                    "type": "text",
                    "complete": True,
                    "endPoint": {"x": 1003.29, "y": 1350.45},
                    "startPoint": {"x": 247.33, "y": 1410.81}
                }, {
                    "text": "since now its remoud into ââ\u003cbrev-y\u003eth\u003c/brev-y\u003e\u003csl\u003ee\u003c/sl\u003eâ other:\u003cbr\u003e",
                    "type": "text",
                    "complete": True,
                    "endPoint": {"x": 1025.06, "y": 1387.06},
                    "variants": ["remoud"],
                    "startPoint": {"x": 242.39, "y": 1449.4}
                }, {
                    "text": "hee had rather deal with a fixt âââ\u003cbrev-y\u003eth\u003c/brev-y\u003e\u003csw-ex\u003ee\u003c/sw-ex\u003e\u003csl\u003en\u003c/sl\u003eâ \u003cbr\u003e",
                    "type": "text",
                    "complete": True,
                    "endPoint": {"x": 1009.23, "y": 1449.4},
                    "variants": ["fixt"],
                    "startPoint": {"x": 151.35, "y": 1494.91}
                }, {
                    "text": "with a runing gout:\u003cbr\u003e",
                    "type": "text",
                    "complete": True,
                    "endPoint": {"x": 926.11, "y": 1489.96},
                    "startPoint": {"x": 384.87, "y": 1500.85}
                }, {
                    "text": "Gout:",
                    "type": "text",
                    "complete": True,
                    "endPoint": {"x": 688.64, "y": 109.64},
                    "startPoint": {"x": 447.21, "y": 119.54}
                }
            ]
        }
    ]
}

expected = {
    'variants': [
        "ina",
        "observd",
        "peeld",
        "remoud",
        "fixt"
    ]
}

classification_blank = {
    'annotations': []
}

expected_blank = {}


class TextSWVariantExtractor(unittest.TestCase):
    def test_extract(self):
        result = extractors.sw_variant_extractor(classification)
        self.assertDictEqual(result, expected)

    def test_request(self):
        request_kwargs = {
            'data': json.dumps(annotation_by_task(classification)),
            'content_type': 'application/json'
        }
        app = flask.Flask(__name__)
        with app.test_request_context(**request_kwargs):
            result = extractors.sw_variant_extractor(flask.request)
            self.assertDictEqual(result, expected)

    def test_extract_blank(self):
        result = extractors.sw_variant_extractor(classification_blank)
        self.assertDictEqual(result, expected_blank)

    def test_request_blank(self):
        request_kwargs = {
            'data': json.dumps(annotation_by_task(classification_blank)),
            'content_type': 'application/json'
        }
        app = flask.Flask(__name__)
        with app.test_request_context(**request_kwargs):
            result = extractors.sw_variant_extractor(flask.request)
            self.assertDictEqual(result, expected_blank)
