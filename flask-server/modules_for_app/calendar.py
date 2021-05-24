import os
import sys
from flask_restx import reqparse, Api, Resource
from flask import Blueprint, jsonify, url_for, send_file
from werkzeug.datastructures import FileStorage
from app import get_database
import uuid

# # 카카오 로그인 API를 통해 유저 정보 가져오기
# from .kakao_login import logged_in_as, kakao_user_info

# pymongo cursor 객체 인코딩
from bson import json_util
from .json_encoder_for_pymongo import MongoEngineJSONEncoder

# 상위 디렉토리 import를 위한 경로 설정
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

# DB 및 Collection 연결
database = get_database()
calendar_collection = database['Calendar']

# 블루프린트/API 객체 생성 및 인코더 연결
calendar = Blueprint('calendar', __name__)
calendar.json_encoder = MongoEngineJSONEncoder
api = Api(calendar)

# 도큐먼트 형식(참고)
'''
test_callendar_doc = {
    'user_id': '60a22ad2a453e4e5ba8d203f',
    'date': '2021-04-01',
    'ootd_path': 'img_path/in/blob/storage',
    'clothes_feature': {
        'color': 'red',
        'fabric': 'cotton',
        'sleeve': 'long',
        'etc': '...etc'
    }
}
'''

# request 요청 변수 parser
parser_calendar = reqparse.RequestParser()
parser_calendar.add_argument('user_id')
parser_calendar.add_argument('date')
parser_calendar.add_argument(
    'ootd_img', type=FileStorage, location='files')

# clothes_feature
parser_calendar.add_argument('fabric')
parser_calendar.add_argument('color')
parser_calendar.add_argument('sleeve')

# 캘린더 화면 OOTD 등록 표시용
parser_calendar.add_argument('month')

# 캘린더 CRUD

'''
blob storage에 저장될 이미지 파일에 대한 처리는 추후 배포용 VM 수령 후 진행
'''


class Calendar(Resource):
    # Create
    def post(self):
        args = parser_calendar.parse_args()

        '''
        Validation 추가 예정
        '''

        # 테스트용, 이후 Blob Storage Upload 부분 추가 예정
        local_file_name = str(uuid.uuid4()) + '.png'
        local_file_path = os.path.join('ootd_storage', local_file_name)
        args['ootd_img'].save(local_file_path)

        document = {
            'user_id': args['user_id'],
            'date': args['date'],
            'ootd_path': local_file_name,
            'clothes_feature': {
                'fabric': args['fabric'],
                'color': args['color'],
                'sleeve': args['sleeve']
            }
        }

        calendar_collection.insert_one(document)
        del document['_id']

        return jsonify(
            status=200,
            ootd_created=document
        )

    # Read

    def get(self):
        args = parser_calendar.parse_args()
        # user_id, date가 함께 params로 요청되는 경우 : OOTD 이미지 반환
        if args['date']:
            query = {'user_id': args['user_id'], 'date': args['date']}
            ootd_info_from_db = list(calendar_collection.find(query))
            local_file_name = str(ootd_info_from_db[0]['ootd_path'])
            local_file_path = os.path.join('ootd_storage', local_file_name)

            return send_file(local_file_path)
        # user_id, month가 전달되는 경우 : 유저가 OOTD를 등록한 날짜 리스트 반환
        else:
            query = {'user_id': args['user_id'], 'date': {
                '$regex': '-' + args['month'] + '-'}}
            ootd_infos_from_db = list(calendar_collection.find(query))
            ootd_enrolled_dates = list()
            for ootd_info in ootd_infos_from_db:
                ootd_enrolled_dates.append(ootd_info['date'])

            return jsonify(
                status=200,
                ootd_enrolled_dates=ootd_enrolled_dates
            )

    # Update

    def put(self):
        args = parser_calendar.parse_args()

        query = {'user_id': args['user_id'], 'date': args['date']}

        old_local_file_name = str(
            list(calendar_collection.find(query))[0]['ootd_path'])
        old_local_file_path = os.path.join('ootd_storage', old_local_file_name)
        os.remove(old_local_file_path)

        new_local_file_name = str(uuid.uuid4()) + '.png'
        new_local_file_path = os.path.join('ootd_storage', new_local_file_name)
        args['ootd_img'].save(new_local_file_path)

        new_values = {"$set": {"ootd_path": new_local_file_name}}

        calendar_collection.update_one(query, new_values)
        ootd_updated = list(calendar_collection.find(query))[0]
        del ootd_updated['_id']

        return jsonify(
            status=200,
            ootd_updated=ootd_updated
        )

    # Delete
    # def delete(self):
    #     args = parser_calendar.parse_args()
    #     query = {'user_id': args['user_id'], 'ootd': args['ootd']}
    #     calendar_collection.delete_one(query)

    #     return jsonify(
    #         status=200,
    #         ootd_deleted=query
    #     )


api.add_resource(Calendar, '/calendar')