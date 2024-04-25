from flask import request
from flask_restful import Resource

items = []  # DB


class Item(Resource):
    def get(self, name):
        """특정 아이템 조회"""
        for item in items:
            if name == item["name"]:
                return {"msg": "found", "data": item}, 200

        return {"msg": "not found"}, 404

    def post(self, name):
        """아이템 생성
        TODO - name을 body에 넣도록 바꾸는 것이 좋을 것 같다.
        """
        global items
        data = request.get_json()
        item = {"name": name, "price": data["price"]}
        items.append(item)

        return {"msg": "succesfully posted!", "data": item}, 201

    def put(self, name):
        """아이템 수정"""
        data = request.get_json()
        for item in items:
            if item["name"] == name:
                item["price"] = data["price"]
                return item

        # 아이템이 존재하지 않으면 새로운 아이템을 추가
        new_item = {"name": name, "price": data["price"]}
        items.append(new_item)
        return new_item

    def delete(self, name):
        """아이템 삭제"""
        global items
        items = [x for x in items if x["name"] != name]
        return {"message": "Item deleted"}
