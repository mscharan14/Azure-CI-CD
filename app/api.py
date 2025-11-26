from flask import Blueprint, request, jsonify
from .models import get_db

bp = Blueprint('api', __name__)

@bp.route('/todos', methods=['GET'])
def list_todos():
    db = get_db()
    rows = db.execute('SELECT id, title, done FROM todos').fetchall()
    todos = [dict(id=r['id'], title=r['title'], done=bool(r['done'])) for r in rows]
    return jsonify(todos)

@bp.route('/todos', methods=['POST'])
def add_todo():
    data = request.get_json() or {}
    title = data.get('title')
    if not title:
        return jsonify({'error': 'title required'}), 400
    db = get_db()
    cur = db.execute('INSERT INTO todos (title, done) VALUES (?,?)', (title, 0))
    db.commit()
    return jsonify({'id': cur.lastrowid, 'title': title, 'done': False}), 201

@bp.route('/todos/<int:tid>', methods=['PUT'])
def update_todo(tid):
    data = request.get_json() or {}
    done = 1 if data.get('done') else 0
    db = get_db()
    db.execute('UPDATE todos SET done=? WHERE id=?', (done, tid))
    db.commit()
    return jsonify({'id': tid, 'done': bool(done)})

@bp.route('/todos/<int:tid>', methods=['DELETE'])
def delete_todo(tid):
    db = get_db()
    db.execute('DELETE FROM todos WHERE id=?', (tid,))
    db.commit()
    return '', 204
