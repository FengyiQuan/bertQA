from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods, require_GET, require_POST
import json

# Create your views here.
from transformers import BertForQuestionAnswering, AutoTokenizer

from transformers import pipeline

modelname = 'deepset/bert-base-cased-squad2'

model = BertForQuestionAnswering.from_pretrained(modelname)
tokenizer = AutoTokenizer.from_pretrained(modelname)

nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)
#
# context = "The Intergovernmental Panel on Climate Change (IPCC) is a scientific intergovernmental body under the auspices of the United Nations, set up at the request of member governments. It was first established in 1988 by two United Nations organizations, the World Meteorological Organization (WMO) and the United Nations Environment Programme (UNEP), and later endorsed by the United Nations General Assembly through Resolution 43/53. Membership of the IPCC is open to all members of the WMO and UNEP. The IPCC produces reports that support the United Nations Framework Convention on Climate Change (UNFCCC), which is the main international treaty on climate change. The ultimate objective of the UNFCCC is to \"stabilize greenhouse gas concentrations in the atmosphere at a level that would prevent dangerous anthropogenic [i.e., human-induced] interference with the climate system\". IPCC reports cover \"the scientific, technical and socio-economic information relevant to understanding the scientific basis of risk of human-induced climate change, its potential impacts and options for adaptation and mitigation.\""
#
# result = nlp({
#     'question': 'What organization is the IPCC a part of?',
#     'context': context
# })
#
# print(result)


def answer_question(question, context):
    result = nlp({
        'question': question,
        'context': context
    })
    return result


@require_GET
def home(request: HttpRequest):
    return HttpResponse("Hello, world. You're at the index.")


@require_GET
def ask(request: HttpRequest):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    question = body['question']
    in_context = body['context']
    # print(request.GET['question'])
    # print(request.GET['context'])
    res = answer_question(question, in_context)
    return JsonResponse(res, status=200)
