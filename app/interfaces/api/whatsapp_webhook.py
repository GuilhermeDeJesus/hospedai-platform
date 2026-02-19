from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.application.use_cases.checkin_via_whatsapp import CheckInViaWhatsAppUseCase
from app.application.dto.checkin_request_dto import CheckinRequestDTO
from app.interfaces.dependencies import get_checkin_use_case

router = APIRouter()

class WhatAppMessage(BaseModel):
    phone: str
    message: str
    
@router.post("/webhook/whatsapp")

def whatsapp_webhook(payload: WhatAppMessage, use_case: CheckInViaWhatsAppUseCase = Depends(get_checkin_use_case)):
    # Simples lógica: se mensagem contém "checkin"
        if "checkin" in payload.message.lower():
            response = use_case.execute(
                CheckinRequestDTO(phone=payload.phone)
            )
            return {"reply": response.message}

        return {"reply": "Mensagem recebida."}