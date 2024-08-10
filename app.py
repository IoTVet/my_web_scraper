from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def connect_db():
    return sqlite3.connect('scraped_data.db')

@app.route('/api/data', methods=['GET'])
def get_data():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('SELECT type, content FROM scraped_data')
    rows = cursor.fetchall()

    data = [{'type': row[0], 'content': row[1]} for row in rows]

    conn.close()
    return jsonify(data)

@app.route('/api/headings', methods=['GET'])
def get_headings():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT content FROM scraped_data WHERE type='Heading'")
    rows = cursor.fetchall()

    headings = [row[0] for row in rows]

    conn.close()
    return jsonify(headings)

@app.route('/api/paragraphs', methods=['GET'])
def get_paragraphs():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT content FROM scraped_data WHERE type='Paragraph'")
    rows = cursor.fetchall()

    paragraphs = [row[0] for row in rows]

    conn.close()
    return jsonify(paragraphs)

@app.route('/api/links', methods=['GET'])
def get_links():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT content FROM scraped_data WHERE type='Link'")
    rows = cursor.fetchall()

    links = [row[0] for row in rows]

    conn.close()
    return jsonify(links)

if __name__ == '__main__':
    app.run(debug=True)
