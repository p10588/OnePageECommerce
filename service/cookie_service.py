from flask import make_response, request, Flask
import json


class CookieService:

    def set_cookie(self, key, value, expires):
        response = make_response('set cookies success')

        data = json.dumps(value)
        response.set_cookie(key, data, expires)
        return response
    
    def get_cookie(self, key):
        cookie = request.cookies.get(key)
        if cookie:
            return json.loads(cookie)
        else:
            ex = f'Cant find Cookies {key}'
            print(ex)
            raise Exception(ex)
 
        
    def delete_cookie(self,key):
        response = make_response('remove cookies success')
        response.delete_cookie(key)
        return response