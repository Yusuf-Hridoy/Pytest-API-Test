from utils.myutils import getAllBooking

base_url = "https://restful-booker.herokuapp.com/booking"

def test_get_all_booking():
    data, timetaken = getAllBooking(base_url)
    print(f"Time taken for the request: {timetaken} seconds")
    print(data)