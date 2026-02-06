from Framework.utils.myConfigparser import getconfig
from utils.myutils import getAllBooking, updateBooking

#base_url = "https://restful-booker.herokuapp.com/booking"


base_url = getconfig()

def test_get_all_booking():
    data, timetaken = getAllBooking(base_url)
    print(f"Time taken for the request: {timetaken} seconds")
    print(data)

# update booking by id