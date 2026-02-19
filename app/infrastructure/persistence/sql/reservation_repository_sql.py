from app.domain.entities.reservation import Reservation
from app.domain.repositories.reservation_repository import ReservationRepository
from .models import ReservationModel

class ReservationRepositorySQL(ReservationRepository):
    def __init__(self, session):
        self.session = session
        
    def find_by_phone_number(self, phone_number: str) -> Reservation:
        reservation_model = self.session.query(ReservationModel).filter_by(guest_phone=phone_number).first()
        if reservation_model:
            return Reservation(
                reservation_id=str(reservation_model.id),
                guest_phone=reservation_model.guest_phone,
                status=reservation_model.status
            )
        return None