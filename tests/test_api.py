import json
from app import create_app

def test_add_list_delete():
    app = create_app()
    client = app.test_client()
    # add
    r = client.post('/api/todos', data=json.dumps({'title':'x'}), content_type='application/json')
    assert r.status_code == 201
    obj = r.get_json()
    tid = obj['id']
    # list
    r = client.get('/api/todos')
    assert r.status_code == 200
    assert any(t['id'] == tid for t in r.get_json())
    # delete
    r = client.delete(f'/api/todos/{tid}')
    assert r.status_code == 204
