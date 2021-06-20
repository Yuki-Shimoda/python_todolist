from flask import Flask, render_template, request, redirect, make_response, jsonify
import json
import os
import psycopg2
import random
app = Flask(__name__)

def get_connection():
    localhost = 'localhost'
    port = '5432'
    users = 'postgres'
    dbnames = 'fr_test'
    passwords = 'postgres'
    return psycopg2.connect("host=" + localhost + " port=" + port + " user=" + users + " dbname=" + dbnames + " password=" + passwords)
@app.route('/', methods=['GET','POST'])
def create():
    # with get_connection() as conn:
    #     with conn.cursor() as cur:
    #         cur.execute('SELECT * FROM emp')
    #         result = cur.fetchall()
    #         print(type(result))
    #         print(result)
    #         en_result = json.dumps(result, indent=4)
    #         print(type(en_result))
    #         print(en_result)
    #     with open('test3.json', 'w') as f:
    #         json.dump(en_result, f, ensure_ascii=False)
    with get_connection() as conn:
        with conn.cursor() as cur:
            if request.method == 'POST':
                title = request.form.get('title')
                if title != '':
                    sql = "INSERT INTO todo (title) VALUES (%s)"
                    cur.execute(sql, (title,))
                    conn.commit()
                    redirect('/')
            cur.execute('SELECT * FROM todo')
            result = cur.fetchall()
            todo_result = dict(result)
            # cur.execute('SELECT * FROM emp')
            # result = cur.fetchall()
            #print(type(result))
            # print(result)
            # new_result = {}
            # id_list = []
            # name_list = []
            # age_list = []
            # gender_list = []
            # dep_id_list = []
            # for tp_list in result:
                # print(tp_list)
                # id_list.append(tp_list[0])
                # name_list.append(tp_list[1])
                # age_list.append(tp_list[2])
                # gender_list.append(tp_list[3])
                # dep_id_list.append(tp_list[4])
                # print(id_list)
                # print(name_list)
                # print(age_list)
                # print(gender_list)
                # print(dep_id_list)
            # count = 0
            # for id in id_list:
            #     new_result[id] = {}
            #     # print(new_result)
            #     new_result[id]['name'] = name_list[count]
            #     new_result[id]['age'] = age_list[count]
            #     new_result[id]['gender'] = gender_list[count]
            #     new_result[id]['dep_id'] = dep_id_list[count]
                # print(type(new_result[id]['name']))
            #     count += 1
            # print(new_result[10]['name'])
            # with open('test3.json', 'w') as f:
            #     json.dump(new_result, f, ensure_ascii=False, indent=4)
            # json_file = open('test3.json', 'r')
            # json_object = json.load(json_file)
            #
            # print(json_object)
            # print(type(json_object))
            #
            # for i in json_object:
            #     print(i)
    return render_template('index.html', result = result, todo_result = todo_result)
# def table():
#     with get_connection() as conn:
#         with conn.cursor() as cur:
#                 sql = "SELECT id, name, age, gender FROM test INNER JOIN test_dep ON test.id = test_dep.id"
#                 cur.execute(sql, (title,))
#                 conn.commit()
#                 redirect('/')
#             cur.execute('SELECT * FROM todo')
#             result = cur.fetchall()
#             todo_result = dict(result)
#             # cur.execute('SELECT * FROM emp')
#             # result = cur.fetchall()
#             #print(type(result))
#             # print(result)
#             # new_result = {}
#             # id_list = []
#             # name_list = []
#             # age_list = []
#             # gender_list = []
#             # dep_id_list = []
#             # for tp_list in result:
#                 # print(tp_list)
#                 # id_list.append(tp_list[0])
#                 # name_list.append(tp_list[1])
#                 # age_list.append(tp_list[2])
#                 # gender_list.append(tp_list[3])
#                 # dep_id_list.append(tp_list[4])
#                 # print(id_list)
#                 # print(name_list)
#                 # print(age_list)
#                 # print(gender_list)
#                 # print(dep_id_list)
#             # count = 0
#             # for id in id_list:
#             #     new_result[id] = {}
#             #     # print(new_result)
#             #     new_result[id]['name'] = name_list[count]
#             #     new_result[id]['age'] = age_list[count]
#             #     new_result[id]['gender'] = gender_list[count]
#             #     new_result[id]['dep_id'] = dep_id_list[count]
#                 # print(type(new_result[id]['name']))
#             #     count += 1
#             # print(new_result[10]['name'])
#             # with open('test3.json', 'w') as f:
#             #     json.dump(new_result, f, ensure_ascii=False, indent=4)
#             # json_file = open('test3.json', 'r')
#             # json_object = json.load(json_file)
#             #
#             # print(json_object)
#             # print(type(json_object))
#             #
#             # for i in json_object:
#             #     print(i)
#     return render_template('index.html', result = result, todo_result = todo_result)
# @app.route('/update/<int:key>', methods=['GET', 'POST'])
# def read(key):
#     with get_connection() as conn:
#         with conn.cursor() as cur:
#             if request.method == 'POST':
#                 update_title = request.form.get('update_title')
#                 if update_title != '':
#                     sql = 'UPDATE todo SET title = %s WHERE id = %s'
#                     cur.execute(sql, (update_title, key))
#                     conn.commit()
#                     return redirect('/')
#             cur.execute("SELECT * FROM todo WHERE id = %s", (key,))
#             result = dict(cur.fetchall())
#             print(result)
#     return render_template('update.html', result = result)
@app.route('/delete/<int:key>')
def delete(key):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM todo WHERE id = %s", (key,))
    return redirect('/')