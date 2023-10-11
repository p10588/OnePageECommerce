from flask import make_response, request, Flask
import json


class CookieService:

    def SetCookie(self, key, value, expires):
        response = make_response('set cookies success')
        response.set_cookie(key, json.dumps(value), expires)
        return response
    
    def GetCookie(self, key):
        cookie = request.cookies.get(key)
        if cookie:
            try:
                return json.loads(cookie)
            except json.JSONDecodeError as e:
                print('Error: {e}')
                return None
        else:
            print('No Cookies')
            return None
 
        
    def RemoveCookie(self,key):
        response = make_response('remove cookies success')
        response.delete_cookie(key)
        return response