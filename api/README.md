# QrGen-Team_59 API

This app controls our API. The API shall be built on python's Django Rest Framework.

## Endpoints

It  shall have five (5) endpoints:
- /qrcodes/create/ [POST]
- /qrcodes/ [GET]
- /qrcodes/id/ [GET]
- /qrcodes/id/ [PUT]
- /qrcodes/id/ [DELETE]



## Authentication
The API shall use JWT (Json Web Tokens) for user authentication. Each request to a restricted endpoint shall require an 'Access (Bearer)' Header containing the user's access code. Hence, only registered users with active access codes can access these restricted endpoints.


