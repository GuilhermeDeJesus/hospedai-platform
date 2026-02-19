from app.infrastructure.persistence.memory.reservation_repository_memory import ReservationRepositoryMemory
from app.infrastructure.persistence.sql.reservation_repository_sql import ReservationRepositorySQL
from app.application.use_cases.checkin_via_whatsapp import CheckInViaWhatsAppUseCase
from app.infrastructure.cache.redis_repository import RedisRepository
from app.infrastructure.persistence.sql.database import SessionLocal

# def get_reservation_repository():

def get_checkin_use_case():
    session = SessionLocal()
      
    reservation_repo = ReservationRepositorySQL(session)
    conversation_cache_repo = RedisRepository()
    
    return CheckInViaWhatsAppUseCase(reservation_repository=reservation_repo, cache_repository=conversation_cache_repo)