from fastapi import APIRouter

router = APIRouter(prefix='/notes', tags=['notes'])

@router.get('/')
async def get_all_notes():
    return [{'id': 1, 'text': 'some text1', 'tags': [{'id': 1, 'name': 'tag1'}, {'id': 1, 'name': 'tag2'}]}, 
            {'id': 2, 'text': 'some text2', 'tags': [{'id': 1, 'name': 'tag2'}, {'id': 1, 'name': 'tag3'}]},
            {'id': 3, 'text': 'some text3', 'tags': [{'id': 1, 'name': 'tag3'}, {'id': 1, 'name': 'tag4'}]}]