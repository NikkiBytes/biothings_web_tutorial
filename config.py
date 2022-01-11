import os
from biothings.web.settings.default import QUERY_KWARGS


ES_HOST = "localhost:9200" # optional
ES_INDICES = {"gene": "v1"}
ANNOTATION_DEFAULT_SCOPES = ["_id", "symbol"]
QUERY_KWARGS['*']['_source']['default'] = ['name', 'symbol', 'taxid', 'entrezgene']
ES_RESULT_TRANSFORM = "pipeline.MyFormatter"
ES_QUERY_BUILDER = "pipeline.MyQueryBuilder"
ES_QUERY_PIPELINE = "pipeline.MyQueryPipeline" #overwrites Pipeline class
