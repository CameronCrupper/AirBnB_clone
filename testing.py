#!/usr/bin/python3

from models.base_model import BaseModel
from uuid import uuid4
from datetime import datetime as dt

print(str(dt.isoformat(dt.now())))

yesterday = "1965-09-13T14:57:02.311267"

eleven11 = "2011-11-11T11:11:11.123456"

future = "2034-06-26T09:56:21.654321"

dt1111 = dt.fromisoformat(eleven11)

# print(dteleven11.__class__.__name__ == "datetime")
# print(dt.fromisoformat(eleven11))

# thisinvalid = "2011-16-11T11:11:11.123456"
""" otherinvalid = "somethingwrong"
# foi = dt.fromisoformat(otherinvalid) """
# formatted = dt.fromisoformat(thisinvalid)

# print(dteleven11.__class__.__name__ == "datetime")

""" print(foi) """
""" print(formatted)
 """
newargs = {'id': uuid4(), 'created_at': yesterday}

tno = BaseModel(**newargs)
newargs = {'id': uuid4(), 'updated_at': future}
tno.update(**newargs)
print(str(tno))
