# QrGen-Team_59 API

This app controls our API. The API shall be built on python's Django Rest Framework.

## Endpoints

It  shall have five (5) endpoints:
- /qrcodes/ [POST]          -   to create a QR Code (restricted)
- /qrcodes/ [GET]           -   to get all QR Codes on the system (unrestricted)
- /qrcodes/id/ [GET]        -   to get one QR Code by the id (unrestricted)
- /qrcodes/id/ [PUT]        -   to edit one QR Code by the id (restricted)
- /qrcodes/id/ [DELETE]     -   to delete one QR Code by the id (restricted)



## Authentication
The API shall use JWT (Json Web Tokens) for user authentication. Each request to a restricted endpoint shall require an 'Access (Bearer)' Header containing the user's access code. Hence, only registered users with active access codes can access these restricted endpoints.


