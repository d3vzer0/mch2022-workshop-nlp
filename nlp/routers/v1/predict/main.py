
from fastapi import Depends, APIRouter, Security
from typing import List, Dict
from pydantic import BaseModel
from .utils.transforms import Transform
from .utils.extract import Extract, nlp
import spacy
from spacy_html_tokenizer import create_html_tokenizer
from selectolax.parser import HTMLParser


router = APIRouter()

class ExtractModel(Basemodel):
    text: str

class Clean(BaseModel):
    text: str


@router.post('/clean')
async def clean_data(data: Clean):
    ''' Return HTML stripped data '''
    nlp.tokenizer = create_html_tokenizer()(nlp)
    # about_page_text = HTMLParser(data.text).text()
    return {'text': Transform(data.text).clean }


@router.post('/extract')
async def extract(data: ExtractModel):
    document_object = Extract(doc=nlp(data.text))
    return {
        'entities': document_object.entities(),
        'props': document_object.props()
    }
