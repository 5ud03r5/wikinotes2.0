from fastapi import APIRouter

router = APIRouter(prefix='/articles', tags=['articles'])

@router.get('/')
async def get_all_articles():
    return [{'id': 1, 'title': 'art1', 'text': 'some text1', 'tags': [{'id': 1, 'name': 'tag1'}, {'id': 1, 'name': 'tag2'}]}, 
            {'id': 2, 'title': 'art2', 'text': 'some text2', 'tags': [{'id': 1, 'name': 'tag2'}, {'id': 1, 'name': 'tag3'}]},
            {'id': 3, 'title': 'art3', 'text': 'some text3', 'tags': [{'id': 1, 'name': 'tag3'}, {'id': 1, 'name': 'tag4'}]}]