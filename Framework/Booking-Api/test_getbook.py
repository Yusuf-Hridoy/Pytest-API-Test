from utils.myutils import getAllBooking

base_url = "https://restful-booker.herokuapp.com/booking"

def test_get_all_booking():
    data = getAllBooking(base_url)
    print(data)