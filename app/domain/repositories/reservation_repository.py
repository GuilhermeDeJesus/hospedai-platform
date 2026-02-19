from abc import ABC, abstractmethod
from app.domain.entities.reservation import Reservation

class ReservationRepository(ABC):
    @abstractmethod
    def save(self, reservation: Reservation) -> None:
        pass
    
    @abstractmethod
    def find_by_phone_number(self, phone_number: str) -> list[Reservation]:
        pass
