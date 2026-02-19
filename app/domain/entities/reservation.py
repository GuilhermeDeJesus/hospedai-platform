from app.domain.value_objects.phone_number import PhoneNumber
from app.domain.enums.reservation_status import ReservationStatus

class Reservation:
    def __init__(self, reservation_id: str, guest_phone: PhoneNumber, status: ReservationStatus):
        self.id = reservation_id
        self.guest_phone = guest_phone
        self.status = status
        
    def check_in(self):
        if self.status != ReservationStatus.CREATED:
            raise ValueError("Cannot check in. Reservation is not in 'created' status.")
        self.status = ReservationStatus.CHECKED_IN

    def to_dict(self):
        return {
            "id": self.id,
            "guest_phone": str(self.guest_phone),
            "status": self.status.name
        }