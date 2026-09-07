from app.Cinema.bar import CinemaBar
from app.Cinema.hall import CinemaHall
from app.People.customer import Customer
from app.People.cinema_staff import Cleaner


def cinema_visit(
        movie: str, customers: list, hall_number: int, cleaner: str,
) -> None:
    customer_objects = []

    for customer in customers:
        customer_ob = Customer(
            customer["name"],
            customer["food"]
        )

        CinemaBar.sell_product(customer["food"], customer_ob)

        customer_objects.append(customer_ob)

    hall = CinemaHall(hall_number)
    cleaner_ob = Cleaner(cleaner)

    hall.movie_session(movie, customer_objects, cleaner_ob)
