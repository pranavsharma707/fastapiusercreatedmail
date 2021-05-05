from fastapi import FastAPI, BackgroundTasks, UploadFile, File, Form
from starlette.responses import JSONResponse
from starlette.requests import Request
from fastapi_mail import FastMail, MessageSchema,ConnectionConfig
from pydantic import BaseModel, EmailStr
from typing import List
from api import schema


conf = ConnectionConfig(
    MAIL_USERNAME = "javashrm@gmail.com",
    MAIL_PASSWORD = "corejava@1234",
    MAIL_FROM = "javashrm@gmail.com",
    MAIL_PORT = 587,
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_TLS = True,
    MAIL_SSL = False,
)

async def send_mail(request:schema.NewUser)->JSONResponse:

  
    template = """
        <html>
        <body>
          
    <p>Hi !!!
        <br>Thanks for using fastapi mail, keep using it..!!!</p>
  
        </body>
        </html>
        """
  
    message = MessageSchema(
        subject="Fastapi-Mail module",
        recipients=request.dict().get("email"),  # List of recipients, as many as you can pass 
        body=template,
        subtype="html",
    )


    

    fm = FastMail(conf)
    await fm.send_message(message)
    # return JSONResponse(status_code=200, content={"message": "email has been sent"})